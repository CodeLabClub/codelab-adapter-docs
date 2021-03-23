
# 更新提醒(2021-03-18)
新的版本加入了与Scratch UI兼容的功能，相对于旧的版本要复杂些。

# 前言

开发一个 CodeLab Adapter 插件，往往会涉及两部分的工作:

*  在 CodeLab Adapter 里写一个Python插件
*  在 Scratch里写一个 js 插件

类似前后端的配合，只是他们通过消息通信，而不是 REST API。

本文侧重讨论Python插件部分。

CodeLab Adapter 自带一个消息系统，理论上，任何语言都可以与之通信，任何有开放接口的事物都可以接入其中。

本文仅讨论如何在 Scratch 上构建客户端（Scratch Extension，基于 JavaScript），使其与 CodeLab Adapter 通信(收发消息)来扩展 Scratch 的能力。当然，你也可以在任何语言中做这件事。

<!--
Scratch3 插件
python 插件

tello2

microbit简化

Cozmo

将能力推往客户端
-->

# 思路

一个 Adapter 插件（plugin）被视为 Adapter 系统的一个节点(Node), 通过这些节点去适配不同的外部硬件/软件，进而将其接入到系统中。

![](https://adapter.codelab.club/img/codelab-adapter_35cfa251.png)

在系统中，流动的一切都是消息，所以由这些插件连接的事物(软件/硬件)可以彼此沟通（talk），系统得以持续生长。

希望使用 Adapter 某个插件的能力时(如在 Scratch 中)，只需要发送消息与 Adapter 对话即可。

# 开始

## 案例（Tello）

本文采用案例式教学。

近期我们重写了 Adapter Tello 插件，本文将以此为例，介绍 **开发一个 CodeLab Adapter 插件** 的典型流程。

该流程是完全通用的。

### 如何交互？

首先考虑第一个问题：你想接入什么东西？与之交互的方式是什么？(Adapter 是一个利用消息[不停交互的系统](/post/%E5%B0%91%E5%84%BF%E7%BC%96%E7%A8%8B/hardware-programming-style/))

如果你想接入的东西是硬件（如 Tello），那么与之通信的方式可能是调用它们的开放 SDK 。

如果你想接入的东西是软件（如 [Teachable Machine](https://adapter.codelab.club/extension_guide/teachable_machine/)），那么与之通信的方式可能是基于某些标准协议(如 http/websocket).

如果你想接入的东西是一门编程语言的内核（如 Python），那么与之通信的方式可能是 `eval`

#### 寻找 SDK

在本文中，我们 **想接入什么东西** 是 Tello。 我们在 Github 上找到与之通信的 Python SDK: [DJITelloPy](https://github.com/damiafuentes/DJITelloPy)

与 Tello 通信的方式是利用 socket， [DJITelloPy](https://github.com/damiafuentes/DJITelloPy)封装了细节，使我们可以以面向对象的风格与之交互， 我们来一撇 SDK 的使用方式。

```python
from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.move_forward(100)

tello.land()
```

语义清晰，非常简易。

### 构建 Adapter 插件

一个 Adapter 插件不是一个孤岛，它试图与其他事物交谈(talk), 对外部的请求做出回应。

实现这件事的方式很多，软件工程有大量工作围绕这块: **对请求作出回应，提供服务**，我们会想到 RESTful API、RPC...

Adapter 如果完成以上目标？ 我们采取的策略是: **收发消息**。我们把一切看作消息, 并且倾向于晚绑定(late binding)

回到正题。我们先来快速浏览一下 Tello 插件的代码（不必弄懂它，稍后会讲解）。

```py
import json
import time

from codelab_adapter_client import AdapterNode
from codelab_adapter_client.thing import AdapterThing
from djitellopy import Tello  # https://github.com/wwj718/DJITelloPy/archive/master.zip
from loguru import logger


class TelloProxy(AdapterThing):
    '''
    该类的主要职责是实现与 Scratch UI 的兼容性
    '''
    def __init__(self, node_instance):
        super().__init__(thing_name="Tello", node_instance=node_instance)

    def list(self, timeout=5) -> list:
        # 必须实现
        # scratch scan 会触发这个函数，返回值将进入 Scratch 扫描到的设备列表中。
        if not self.thing:
            self.thing = Tello()
        self.thing.RESPONSE_TIMEOUT = timeout
        logger.debug(f"self.thing: {self.thing}")
        try:
            self.thing.connect()  # 返回True有问题，如果没有飞机，就会except
            return ["192.168.10.1"]
        except Exception as e:
            logger.debug(f'error: {str(e)}')
            self.node_instance.pub_notification(str(e), type="ERROR")
            return []

    def connect(self, ip, timeout=5):
        # 必须实现
        # 用户在 scratch 界面点击连接时，会触发该函数
        if not self.thing:
            self.thing = Tello()
        is_connected = self.thing.connect()  # 幂等操作 ，udp
        self.is_connected = is_connected
        return True

    def status(self) -> bool:
        # 必须实现
        # return self.thing.connect()
        pass

    def disconnect(self):
        # 必须实现
        # Scratch 断开连接
        self.is_connected = False
        try:
            if self.thing:
                self.thing.clientSocket.close()
        except Exception:
            pass
        self.thing = None


class Tello3Node(AdapterNode):
    NODE_ID = "eim/node_tello3"
    HELP_URL = "https://adapter.codelab.club/extension_guide/tello3/"
    DESCRIPTION = "tello 3.0"  # list connect
    VERSION = "3.0.0"

    def __init__(self, **kwargs):
        super().__init__(logger=logger, **kwargs)
        self.tello = TelloProxy(self)

    def run_python_code(self, code):
        '''
        此处定义了与外部系统（诸如Scratch）沟通的有效消息
        list: Scratch 发现设备
        connect: scratch 建立连接
        disconnect: scratch 断开连接
        tello: 可调用的对象，一般被scratch具体功能积木调用，消息是传递面向对象风格的Python代码，如 tello.takeoff()
        '''
        try:
            output = eval(
                code,
                {"__builtins__": None},
                {
                    "tello": self.tello.thing,
                    "connect": self.tello.connect,
                    "disconnect": self.tello.disconnect,
                    "list": self.tello.list,
                })
        except Exception as e:
            output = e
        return output

    def extension_message_handle(self, topic, payload):
        # 必须实现
        # 与当前插件有关的消息都流入该函数
        self.logger.info(f'code: {payload["content"]}')
        python_code = payload["content"]
        output = self.run_python_code(python_code)
        try:
            output = json.dumps(output)
        except Exception:
            output = str(output)
        payload["content"] = output
        message = {"payload": payload}
        self.publish(message)

    def run(self):
        # 用于block进程，当收到进程停止消息（将切换self._running状态），则结束阻塞
        while self._running:
            time.sleep(0.5)

    def terminate(self, **kwargs):
        # 必须实现
        # 插件退出钩子，可以执行所需的资源清理（诸如释放设备）
        try:
            self.tello.disconnect()
        except Exception:
            pass
        super().terminate(**kwargs)


def main(**kwargs):
    #  入口函数，启动插件时将以独立 Python 进程运行。
    try:
        node = Tello3Node(**kwargs)
        node.receive_loop_as_thread()
        node.run()
    except Exception as e:
        if node._running:
            node.pub_notification(str(e), type="ERROR")
            time.sleep(0.1)
            node.terminate()


if __name__ == "__main__":
    main()
```

你可以使用 [Adapter 内置的 JupyterLab](https://adapter.codelab.club/extension_guide/jupyterlab/) 浏览/修改 这些插件源码, 保存并重启插件之后，即刻生效（不需要重启 Adapter）

![](/post/img/feb2a3d0fffb174e45009560e05e32e2.png)

我们来看看 tello 插件各部分代码的含义和功能是什么（主要关心 Tello3Node）

![](/post/img/feb2a3d0fffb174e45009560e05e32e2-note.png)


可是，并没有见到跟 Tello 有关的业务逻辑啊？

是的，这正是我们想法的核心部分: `晚绑定(late binding)`, 将功能描述不断后推，交给 client（甚至是用户）。

Adapter Tello 插件看起来颇像一个 REPL，它解释(run_python_code)收到的消息(副作用是 tello 飞行器的行为), Tello 的行为将由输入的消息决定，消息携带语义。我们贪图便利，直接将 Python 代码视为消息(因其能很好携带语义)

### 客户端

接下来我们来构建一个客户端来使用 Adapter Tello 插件。

前头提到，我们计划在 Scratch 里构建一个客户端，它是一个 Scratch Extension。

#### Scratch Extension

如果你对构建 Scratch Extension 不熟悉，请参考: [创建你的第一个 Scratch3.0 Extension](/post/%E5%B0%91%E5%84%BF%E7%BC%96%E7%A8%8B/create-first-scratch3-extension/)

我们已经将 Scratch Tello 插件开放在这儿: [scratch3_tello3](https://github.com/CodeLabClub/scratch3_tello3)

##### 如何交互(talk)?

前头提到:

> 一个 Adapter 插件不是一个孤岛，它试图与其他事物交谈(talk), 对外部的请求做出回应。

Scratch Tello 插件（JavaScript）是如何与 Adapter 插件（Python）交互的呢？

它们通过 websocket(socketio)沟通, 但你不需要在意和弄懂它们沟通的细节，我们已经构建了一个 [Adapter js client](https://github.com/CodeLabClub/scratch3_eim/blob/v3/codelab_adapter_base.js)，抽象掉了 talk 的细节，让你可以基于它轻松在 js 里与 Adapter 交互。 (注意:你的开发环境里，需要有[scratch3_eim](https://github.com/CodeLabClub/scratch3_eim))

##### 源码解读

接下来，一起深入到源码里看看。

我们通过阐述这两块积木，来看看引擎盖后发生的事情。

![](/post/img/ce07d13ba0fc32677474fa7a76693e0d.png)

首先看看，当我们 **起飞** 积木运行的时候发生了什么:

![](/post/img/ef01b07d369d15db57a2c2f48b642735.png)

实际上，当 Scratch 中， **起飞** 积木运行时，消息 `tello.takeoff()` 将发送到 Adapter Tello 插件，插件将解释这则消息-- eval(执行)这段 Python 代码。

接着我们来看看 **设置速度** 积木（带有参数）运行的时候发生了什么:

![](/post/img/219a985303170e825a0570d089c17972.png)

可以看出，我们试图将参数拼凑到 Python 代码里。

`this.client.emit_with_messageid` 是与 Adapter 通信的关键，这部分也很简单，只是发送消息，如果你兴趣不大，不需要弄懂它, 将其视为模版代码，跟着既有的插件(我们开放了插件)填空即可。

需要注意的是，发往插件的消息并不一定是 Python 代码，它只要携带语义就行。

[AdapterBaseClient](https://github.com/CodeLabClub/scratch3_tello3/blob/main/index.js#L13) 类是与 Adapter 通信的唯一入口。 AdapterBaseClient在[初始化的时候](https://github.com/CodeLabClub/scratch3_tello3/blob/main/index.js#L152), 允许传入一些回调函数，获取来自Adapter一侧的消息。


## 发布 Adapter 插件

如果你构建了新的 Adapter 插件，欢迎提交到[插件市场](https://adapter.codelab.club/extension_guide/extension_market/)

# 调试

为了方便开发 Adapter 插件，一些[调试技巧](https://adapter.codelab.club/dev_guide/debug/)可能对你有用

# 进阶 && 进一步阅读

-   [scratch3_python_kernel](https://github.com/CodeLabClub/scratch3_python_kernel)
-   [scratch3_usb_microbit](https://github.com/CodeLabClub/scratch3_usb_microbit)
-   [scratch3_microbit_radio](https://github.com/CodeLabClub/scratch3_microbit_radio)
-   [Python 对象的连接器：EIM 插件](https://adapter.codelab.club/project_tutorial/eim_pt/)
-   [scratch3_cozmo](https://github.com/CodeLabClub/scratch3_cozmo)
-   [Scratch 拓展最佳实践 -- 以 Cozmo 为例](https://codelab.club/blog/2020/04/26/%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/)

# FAQ
## 我手头没有 Tello，怎么更方便调试
你可以自定义一个一个Tello类替代 `from djitellopy import Tello`， 只需要实现js积木里调用的方法即可,诸如 `takeoff`， 这种方式有助于你理解沟通过程。

当然，你也可以使用我们构建了一个模拟设备的例子: 

*  Adapter nodes: [node_thingDemo.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_thingDemo.py)
*  Scratch extension: [scratch3_thingDemo](https://github.com/CodeLabClub/scratch3_thingDemo)

<!--
## 如何以 Scratch 的风格连接硬件？

![](https://adapter.codelab.club/img/443ca8f702f12723b7794bdd5df4ddef.png)

这部分主要是通过与 Scratch 的 runtime 交互实现的，更多细节参考以下两个Scratch 插件的 `scan` 函数

参考:

*  [scratch3_usb_microbit](https://github.com/CodeLabClub/scratch3_usb_microbit)
*  [scratch3_microbit_radio](https://github.com/CodeLabClub/scratch3_microbit_radio)
-->

## 如何刷入自定义固件

-   [from codelab_adapter.utils import list_microbit, flash_usb_microbit, flash_makecode_file](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_usb_microbit.py#L7)

## Adatper 内置了哪些第三方库

[wiki](https://github.com/CodeLabClub/codelab_adapter_extensions/wiki)

## 如何引入新的 Python 第三方库

Adapter 允许[再分发](https://adapter.codelab.club/dev_guide/%E5%AE%9A%E5%88%B6%E4%B8%8E%E5%88%86%E5%8F%91/), 把需要的第三方库放在相应目录下，再分发即可

放在目录下即可，再分发

更多 [FAQ](https://adapter.codelab.club/dev_guide/FAQ/)

# 参考

-   [创建你的第一个 Scratch3.0 Extension](/post/%E5%B0%91%E5%84%BF%E7%BC%96%E7%A8%8B/create-first-scratch3-extension/)
-   [scratch3_tello2](https://github.com/CodeLabClub/scratch3_tello2)
-   [scratch3_eim](https://github.com/codelabclub/scratch3_eim)
-   [scratch3_python_kernel](https://github.com/CodeLabClub/scratch3_python_kernel)
-   [scratch3_usb_microbit](https://github.com/CodeLabClub/scratch3_usb_microbit)
-   [scratch3_microbit_radio](https://github.com/CodeLabClub/scratch3_microbit_radio)
-   [Python 对象的连接器：EIM 插件](https://adapter.codelab.club/project_tutorial/eim_pt/)
-   [scratch3_cozmo](https://github.com/CodeLabClub/scratch3_cozmo)
-   [Scratch 拓展最佳实践 -- 以 Cozmo 为例](https://codelab.club/blog/2020/04/26/%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/)
-   [jsonrpc.js](https://github.com/LLK/scratch-vm/blob/acc2e6dba2e5a32668f0b26f0b2c4dfdecbe1023/src/util/jsonrpc.js)
-   [codelab_adapter_base.js](https://github.com/CodeLabClub/scratch3_eim/blob/v3/codelab_adapter_base.js#L291)
-   [建立在异步消息之上的同步指令](/post/%E7%BC%96%E7%A8%8B/async-msg-sync-cmd/)
-   [两种硬件编程风格的比较](/post/%E5%B0%91%E5%84%BF%E7%BC%96%E7%A8%8B/hardware-programming-style/)
