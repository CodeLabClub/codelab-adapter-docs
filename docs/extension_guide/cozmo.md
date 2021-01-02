# Cozmo

|        | Windows      |  MacOS   | Linux  |
|  ----  | ----         |  ----  | ----  |
| iOS    | [需要安装iTunes](http://cozmosdk.anki.com/docs/install-windows.html#mobile-device-setup)| 开箱可用  | [手动安装](http://cozmosdk.anki.com/docs/install-linux.html) |
| Android| 开箱可用      | 开箱可用  | [手动安装](http://cozmosdk.anki.com/docs/install-linux.html) |


### 运行 SDK 模式
将 Cozmo 接入移动设备（手机/平板），并进入SDK模式。

使用数据线将手机/平板接入电脑。

详情参考: [官方文档](http://cozmosdk.anki.com/docs/initial.html)


### Download Codelab Adapter

<a href="/get_start/gs_install/">Download Codelab Adapter</a>

run it

<!--
### find your local python3 path(Windows users can skip this step)
edit `~/codelab_adapter/extensions/extension_vector.py`, replace python3_path with your local python3 path: `which python3`.

![](/video/scratch-python3-path_37d6feee.png)

restart Codelab Adapter.
-->

### Open Scratch 3.0

open [CodeLab Scratch3](https://scratch-beta.codelab.club/)

### Open extension_cozmo

open extension_cozmo in CodeLab Adapter

Enjoy it :)

!!! tip
    Cozmo 有数百种动作/行为（它们只是字符串），可以使用`运行`和`执行`积木触发。浏览这些丰富的行为可以使用这个工具：[Cozmo-Explorer-Tool](https://github.com/GrinningHermit/Cozmo-Explorer-Tool)。

# Advanced
You can create your own custom  blocks based on the **exec block**. Almost all [Cozmo SDK API](http://cozmosdk.anki.com/docs/index.html) work.


![](/img/cecd9fbb3aea5e8f17438c1636178369.png)

---

# linux user

### install codelab_adapter_client

Python >= `3.6`

Linux/MacOS user: `python3 -m pip install codelab_adapter_client --upgrade --user`

### Install the SDK on your system

Follow Cozmo official tutorial: [Initial Setup](http://cozmosdk.anki.com/docs/initial.html)

If the following code (`hello_world.py`) runs smoothly, go to the next step.

```python
'''
linux:
    /usr/bin/python3 hello_world.py
'''

import cozmo
from codelab_adapter_client import AdapterNode

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello World").wait_for_completed()

cozmo.run_program(cozmo_program)
```

# 进阶
参考 [Cozmo API](http://cozmosdk.anki.com/docs/api.html)，建议在  [jupyterlab](/extension_guide/jupyterlab/) 中做实验(已经内置好了Cozmo环境)

!!! 提醒
    如果你希望做一些更复杂的事，建议直接使用社区里的 Python SDK与 设备交互，之后使用 [Adapter Node](/dev_guide/Adapter-Node/) 将其接入Adapter环境中。
