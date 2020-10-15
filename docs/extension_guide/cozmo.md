# Cozmo
目前仅在mac下做到了开箱可用。

windows和linux用户在Codelab Adapter 启动之后，自行在本地运行 [node_cozmo](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_cozmo.py): `python node_cozmo.py`, [windows & linux user](#windows-linux-user)

### Download Codelab Adapter

<a href="https://adapter.codelab.club/user_guide/install/">Download Codelab Adapter</a>

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

# windows & linux user

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