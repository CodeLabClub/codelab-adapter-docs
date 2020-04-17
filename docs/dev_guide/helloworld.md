# hello world
我们来写一个自定义插件，实现`hello world`。

## 一些唠叨
如果你不爱听唠叨，这部分可以跳过：）

在[架构图](/dev_guide/Architecture/)中，可以看到一个完整的插件包含两个部分：

1.  Scratch 3.0 网页中的插件（内应）
2.  在 CodeLab Adapter 中写一个插件，代理硬件设备、AI 或其他程序

关于第一部分，尽管 Scratch3 官方的 extensions 机制已经可用了，我们也在 Scratch 3.0 中写了很多插件，但社区里文档不多，不大建议大家来踩坑，如果愿意折腾，可以参考[创建你的第一个 Scratch 3.0 Extension](https://blog.just4fun.site/create-first-Scratch3-Extension.html)。

我们在 [CodeLab Scratch3](https://scratch3v3.codelab.club)中构建了一些通用的消息积木（EIM），我们尽量将它做的通用，让开发者只需在 CodeLab Adapter 自定义插件，即可在 Scratch3 中使用。

这块的核心概念很简单，如 EIM 所代表的含义：`Everything Is Message`，消息是一种极其强大的概念，如 Alan Kay 说的：

>  The big idea is messaging.

如果你用过 ZeroMQ 或者 Erlang 大概深有体会。

## 正式开始
EIM 插件很适合作为示例，来讲解如何创建自定义 CodeLab Adapter 插件。

## 使用 EIM 插件
在开始讲解 EIM 源码之前，你先使用一下 EIM 插件，看下它是个啥：[EIM 使用教程](/extension_guide/eim/)

EIM 插件的功能很简单：

*  EIM 每秒钟更新一次数值，将数值报告给 Scratch3（CodeLab Adapter -> Scratch）
*  接收来自 Scratch 的消息，将其记录在日志中（Scratch -> CodeLab Adapter）

括号中注明了消息的流向。


## Talk is cheap, show me the code
EIM 插件的源码在这儿：[extension_eim.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v2/extension_eim.py)

```python
'''
EIM: Everything Is Message
'''
import time
from codelab_adapter.core_extension import Extension


class EIMExtension(Extension):
    '''
    Everything Is Message
    '''

    def __init__(self):
        super().__init__()
        self.EXTENSION_ID = "eim"

    def extension_message_handle(self, topic, payload):
        self.logger.info(f'eim message:{payload}')
        self.publish({"payload": payload})

    def run(self):
        '''
        run 会被作为线程调用
        '''
        i = 0
        while self._running:
            message = self.message_template()
            message["payload"]["content"] = str(i)
            self.publish(message)
            time.sleep(1)
            i += 1
            '''
            if i%5 == 0:
                self.pub_notification(content=i)
            '''

export = EIMExtension
```

代码很简单，而且大部分是样板代码，有几点值得注意：

*  `EXTENSION_ID` 默认为 `EIM`，可以不写。
*  `extension_message_handle` 是个回调函数，处理从 Scratch 过来的消息（一般由积木触发）
*  `run` 是插件的主体代码，当你在 Web UI 中选择插件时，发生的事情是：
    *  首先实例化插件类（在此是`export = EIMExtension`）
    *  之后将`run`运行为线程。run 方法一般使用 `while self._running` 来阻塞，`run` 方法一旦结束，该插件的生命周期就结束了。

至于你要在`extension_message_handle`和`run`中写什么 Python 代码则是完全自由的。


## 自定义插件
讲解完 EIM 插件，我们来实现一个自定义插件：`helloworld extension`

我们构建这样一个自定义插件，它的功能为：

*  将 Scratch 发过来的字符串逆转，如果 Scratch 发过来的字符串为`hello world`，我们则向Scratch发送：`dlrow olleh`

该插件的源码为：

```python
import time
from codelab_adapter.core_extension import Extension


class HelloWorldExtension(Extension):
    def __init__(self):
        super().__init__()
        self.EXTENSION_ID = "eim"

    def send_message_to_scratch(self, content):
        message = self.message_template()
        message["payload"]["content"] = content
        self.publish(message)

    def extension_message_handle(self, topic, payload):
        self.logger.info(f'the message payload from scratch: {payload}')
        content = payload["content"]
        if type(content) == str:
            content_send_to_scratch = content[::-1] # 反转字符串
            self.send_message_to_scratch(content_send_to_scratch)

    def run(self):
        while self._running:
            time.sleep(1)

export = HelloWorldExtension
```

将插件命名为`extension_hello_world.py`，将其放到插件目录里，Mac/Linux 用户的插件目录在：`~/codelab_adapter/extensions`，如果找不到插件目录（如 Windows 用户），可以通过 CodeLab Adapter 菜单栏上的 `插件->查看目录` 打开它。

刷新 Web UI，点击运行`extension_hello_world.py`，接着你就可以在 Scratch 中与你的插件交互了。

<img width="800px" src="../../img/v2/helloworld_extension.png"/>

恭喜你，已经能够让 Scratch 与 Python 对话了，你现在可以用你的 Python 技能来为 Scratch 写拓展啦！

## 调试技巧
建议你在写 Python 插件的时候，先做好单元测试，然后再作为插件放到插件目录里运行。

如果你喜欢在真实环境里开发，可以使用`self.logger.info`来打日志（就像前头的代码里做的），你可以实时查看日志：`tail -f ~/codelab_adapter/info.log`，日志目录可以通过菜单里的`日志->目录`打开。

## 更多
你可以在插件中引用哪些 Python 库呢？

所有的 Python 内置库（json/re/math/……）以及这些第三方库：[第三方模块](https://github.com/CodeLabClub/codelab_adapter_extensions/wiki)。

如果你对 EIM 在 Scratch3 一侧的源码感兴趣，我们也开源出来了，可以自行阅读：[scratch3_eim](https://github.com/CodeLabClub/scratch3_eim)。

!!! 提醒
    [第三方模块](https://github.com/CodeLabClub/codelab_adapter_extensions/wiki)中有几个采用异步模式(async): aiohttp、hbmqtt、pymata-express。  
    自定义插件默认以线程运行 `run` 方法, 配合异步库使用的时候需要注意.  
    参考[extension_mqtt_broker.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v2/extension_mqtt_broker.py#L38)和[extension_arduino_uno.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v2/extension_arduino_uno.py#L34)

## 小结
从这个例子中，可以看出写一个自定义的插件是很简单的。而 CodeLab Adapter 对插件要做的事几乎没有任何限制，只要 Python 能做的事，插件系统都能做！就是说你可以自己写一个插件，让 Scratch3 来控制你的蓝牙设备、你的 ROS 机器人、你那跑着 OpenCV 的树莓派或者你童年那辆心爱的玩具四驱车。

enjoy it～
