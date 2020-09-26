# Cozmo
!!! 提醒
    3.2.0 版本的cozmo插件有个错误， 你需要到插件市场下载最新的cozmo插件。
    我们会在近期的3.2.2版本中修复它

!!!提醒
    如果你当前的 Adapter 版本低于`3.1.0`，想在[CodeLab Scratch](https://scratch-beta.codelab.club/)体验最新的event、sensor类型积木(像我们在博客文章[Scratch 拓展最佳实践 -- 以 Cozmo 为例]()里提到的)，需要在[插件市场](/extension_guide/extension_market/)里下载最新版本的[node_cozmo.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_cozmo.py)插件。

# Tutorial

### install codelab_adapter_client

Python >= `3.6`

Linux/MacOS user: `python3 -m pip install codelab_adapter_client --upgrade --user`

windows user: `python -m pip install codelab_adapter_client --upgrade --user`

### Install the SDK on your system

Follow Cozmo official tutorial: [Initial Setup](http://cozmosdk.anki.com/docs/initial.html)

If the following code (`hello_world.py`) runs smoothly, go to the next step.

```python
'''
MacOS:
    /usr/local/bin/python3 hello_world.py
linux:
    /usr/bin/python3 hello_world.py
Windows:
    python hello_world.py
'''

import cozmo
from codelab_adapter_client import AdapterNode

def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Hello World").wait_for_completed()

cozmo.run_program(cozmo_program)
```

### Download Codelab Adapter

<a href="https://adapter.codelab.club/user_guide/install/">Download Codelab Adapter</a>

run it

<img width=300 src="/img/v2/adapter_scratch_style_ui.png"/>

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

!!!注意
    Mac 下，使用安卓手机驱动 Cozmo 需要从命令行启动 CodeLab Adapter（因为依赖shell环境变量）。  
    参考 [Android Debug Bridge](http://cozmosdk.anki.com/docs/adb.html#android-debug-bridge)

!!! tip
    Cozmo 有数百种动作/行为（它们只是字符串），可以使用`运行`和`执行`积木触发。浏览这些丰富的行为可以使用这个工具：[Cozmo-Explorer-Tool](https://github.com/GrinningHermit/Cozmo-Explorer-Tool)。

# Advanced
You can create your own custom  blocks based on the **exec block**. Almost all [Cozmo SDK API](http://cozmosdk.anki.com/docs/index.html) work.


![](/img/cecd9fbb3aea5e8f17438c1636178369.png)