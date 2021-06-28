# pi-top

# 介绍

![](https://www.pi-top.com/hubfs/Homepage%20CES%202021/Homepage_ProjectKits-FK-min.png)

## 接管 pi-top 的思路

参考[机械臂](https://adapter.codelab.club/extension_guide/robotic-arm/)，因其都是树莓派。


## hello world

### 用户电脑配置

假设用户使用自己的电脑编程(运行 Adapter 和 Scratch)

在运行Adapter之前，设置[配置项](https://adapter.codelab.club/user_guide/settings/) `OPEN_MESSAGE_HUB = true`

之后运行 CodeLab Adapter.

### 树莓派配置

在机械臂树莓派里安装 [codelab_adapter_client_python](https://github.com/CodeLabClub/codelab_adapter_client_python): `pip3 install codelab_adapter_client`

创建 `node_PiTop.py` :

```py
# fork 自: https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_python.py
import time
from loguru import logger

from codelab_adapter_client import AdapterNode

from pitop import Pitop


# Set up pi-top
pitop = Pitop()

# Say hi!
# pitop.miniscreen.display_text("Hello!")

class PythonKernelExtension(AdapterNode):

    NODE_ID = "eim/PiTop"
    HELP_URL = "http://adapter.codelab.club/"
    WEIGHT = 95
    VERSION = "0.1"  # extension version
    DESCRIPTION = "PiTop"

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
                "pitop": pitop,
            })
        except Exception as e:
            output = str(e)
        return output

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

之后即可在 CodeLab Scratch 对pi-top编程。

参考这个 [Demo](https://create.codelab.club/projects/12380/)

<video width=80% src="/video/1623132452266836.mp4" controls="controls"></video>


## 参考
*  [API - pi-top Device](https://pi-top-pi-top-python-sdk.readthedocs-hosted.com/en/stable/api_pitop_device.html#pitop)