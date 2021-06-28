# 小象机械臂

## 介绍

![](https://www.elephantrobotics.com/wp-content/uploads/2021/04/IMG_8220.jpg)

>  人人都可以学习玩耍的入门级协作机器人

>  myCobot的设计初衷是为了让对六自由度串联机械臂感兴趣的朋友，可以从0到1的了解、学习和操作机械臂，创造前所未有的机械臂使用体验与教学价值。

---

### 接管机械臂的思路

由于小象机械臂内置了树莓派（用于驱动机械臂），我们将在树莓派里运行一个 [Adapter Node](https://adapter.codelab.club/dev_guide/Adapter-Node/)，以便于用户可以在 CodeLab Scratch 中驱动机械臂。

这个例子展示 Adapter Node 的一种典型用法： Adapter Node与Adapter可以不在同一个主机上。

## hello world

### 用户电脑配置
假设用户使用自己的电脑编程(运行 Adapter 和 Scratch)

在运行Adapter之前，设置[配置项](https://adapter.codelab.club/user_guide/settings/) `OPEN_MESSAGE_HUB = true`

之后运行 CodeLab Adapter.

### 树莓派配置
在机械臂树莓派里安装 [codelab_adapter_client_python](https://github.com/CodeLabClub/codelab_adapter_client_python): `pip3 install codelab_adapter_client`

创建 `node_mycobot.py` :

```py
import time
from loguru import logger

from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD  # 当使用树莓派版本的mycobot时，可以引用这两个变量进行MyCobot初始化

from codelab_adapter_client import AdapterNode

# 初始化一个MyCobot对象
mc = MyCobot(PI_PORT, PI_BAUD)

class PythonKernelExtension(AdapterNode):

    NODE_ID = "eim/mycobot"
    HELP_URL = "http://adapter.codelab.club/"
    WEIGHT = 95
    VERSION = "0.1"  # extension version
    DESCRIPTION = "mycobot"

    def __init__(self, **kwargs):
        adapter_host = "192.168.31.164"  # 运行Adapter的计算机IP
        super().__init__(codelab_adapter_ip_address = adapter_host, **kwargs)
        # self.PyHelper = PyHelper()

    def run_python_code(self, code):
        try:
            # eval(expression, globals=None, locals=None)
            output = eval(code, {"__builtins__": None}, {
                # "PyHelper": self.PyHelper,
                # "requests": requests,
                "mc": mc,
                "Angle": Angle
            })
        except Exception as e:
            output = str(e)
        return output

    # @verify_token
    def extension_message_handle(self, topic, payload):
        logger.info(f'python code: {payload["content"]}')
        python_code = payload["content"]
        output = self.run_python_code(python_code)
        try:
            output = str(output)  # 不要传递复杂结构
        except Exception as e:
            output = str(e)
        payload["content"] = output
        message = {"payload": payload}
        self.publish(message)

    def run(self):
        "避免插件结束退出"
        while self._running:
            time.sleep(0.5)

node = PythonKernelExtension()
node.receive_loop_as_thread()
node.run()
```

在树莓派里运行它。

之后即可在 CodeLab Scratch 对机械臂编程。

参考这个 [Demo](https://create.codelab.club/projects/12360/editor/)

## 积木说明

## 项目链接

## FAQ


## 参考
*  [mycobot-RPi](https://www.elephantrobotics.com/mycobot-RPi/)
*  [机械臂左右摆动](https://www.elephantrobotics.com/docs/myCobot/1-introduction/6-raspberry_mycobot/pymycobot/1-arm_swing.html)