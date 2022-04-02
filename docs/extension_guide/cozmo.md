# Cozmo

## 介绍
![](https://wwj718.github.io/post/img/cozmo92f55c7b.png)

[Cozmo](https://www.digitaldreamlabs.com/pages/cozmo) 是一个可编程的 AI 机器人

这个憨态可掬的机器人，有些像微缩版的瓦力，不过它可没瓦力乖巧

它从睡眼惺忪中醒来，伸伸懒腰，便下床(充电座)自顾自地玩耍，它有自个儿的玩具(发光方块)，如果你有时间，愿意陪它做游戏，它会很开心，赢了得意忘形，输了就捶胸顿足，得失心这么重，恐怕不适合炒股

如果你没空陪它，也无妨，它闲庭信步，吹吹口哨、哼哼小曲儿;闲着无聊，便来回搬运自己的玩具，堆叠起来或是一把推翻，自得其乐。除了不尿裤子，其他方面都像极了你六岁时的样子

---


## hello world

### 连接
详尽的文档参考 [人工智能机器人Cozmo的连接说明（by 英荔）](https://adapter.codelab.club/src/8.%20%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E6%9C%BA%E5%99%A8%E4%BA%BA%20Cozmo.pdf)

以下是简略说明。

#### 运行 SDK 模式
将 Cozmo 接入移动设备（手机/平板），并进入 SDK 模式。

使用数据线将手机/平板接入电脑。

详情参考: [官方文档](http://cozmosdk.anki.com/docs/initial.html)

以下是平板设备与电脑的配对信息，有些组合需要安装驱动。

|        | Windows      |  MacOS   | Linux  |
|  ----  | ----         |  ----  | ----  |
| iOS    | [需要安装iTunes, 比较麻烦，不推荐使用](http://cozmosdk.anki.com/docs/install-windows.html#mobile-device-setup)| 开箱可用  | [手动安装](http://cozmosdk.anki.com/docs/install-linux.html) |
| Android| 开箱可用      | 开箱可用  | [手动安装](http://cozmosdk.anki.com/docs/install-linux.html) |


<!--
### find your local python3 path(Windows users can skip this step)
edit `~/codelab_adapter/extensions/extension_vector.py`, replace python3_path with your local python3 path: `which python3`.

![](/video/scratch-python3-path_37d6feee.png)

restart Codelab Adapter.
-->

#### 打开 Scratch Cozmo 插件
![](/img/68fd005464646ab0bea163f601ce02fd.png)

点击扫描图标, 连接 Cozmo

![](/img/71765d0fd445e3d66ff471b0c6e93f68.png)

让 Cozmo 说出 hello world:

![](/img/ca5b78159b3250516e45f4e52bd99d68.png)

## 积木说明
![](/img/9c5ea552081f04138f6d2e059d93c6ca.png)

!!! tip
    [行为名字API文档](http://cozmosdk.anki.com/docs/generated/cozmo.anim.html#cozmo.anim.Triggers)  
    浏览这些丰富的行为可以使用这个工具：[Cozmo-Explorer-Tool](https://github.com/GrinningHermit/Cozmo-Explorer-Tool)。

!!! tips
    [API 文档](http://cozmosdk.anki.com/docs/api.html)  
    [机器人的所有方法](http://cozmosdk.anki.com/docs/generated/cozmo.robot.html#cozmo.robot.Robot)

基于`执行`积木，你可以轻松构建自定义积木:

![](/img/cecd9fbb3aea5e8f17438c1636178369.png)

##  项目链接
暂无

## FAQ
### 如何排查 无法发现设备 的问题？
参考[这里](https://adapter.codelab.club/user_guide/FAQ/#_9)

### 在 notebook 中运行 [cozmo cli](https://github.com/anki/cozmo-python-sdk/blob/master/examples/apps/cli.py)

如果你在notebook中使用，可直接使用内置的notebook: `notebooks/cozmo_lab.ipynb`（最后一个例子）

如果你期待在交互性的 IPython 环境中探索 Cozmo，在Adapter 内置的 jupyterlab 中打开 Terminal，然后使用内置Python解释器运行的 cli 脚本:

*  macOS
    *  `./Support/bin/python3 ~/codelab_adapter/src/cozmo_cli.py`

### 如何在 Adapter jupyterlab 中使用
参考 [Cozmo API](http://cozmosdk.anki.com/docs/api.html)，建议在  [jupyterlab](/extension_guide/jupyterlab/) 中做实验(已经内置好了Cozmo环境)

!!! 提醒
    如果你希望做一些更复杂的事，建议直接使用社区里的 Python SDK与 设备交互，之后使用 [Adapter Node](/dev_guide/Adapter-Node/) 将其接入Adapter环境中。

### linux 用户如何使用

#### 安装 codelab_adapter_client

Python >= `3.6`

`python3 -m pip install codelab_adapter_client --upgrade --user`

#### 测试运行

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

<!--
### 亚马逊 fire 平板上无法安装 Cozmo APP
可以先下载安装第三方应用市场APKpure，在上面可以安装 Cozmo APP
-->

## 参考
*  [cozmo系列之入门 - 有性格且可编程的机器人](https://wwj718.github.io/post/%E5%B0%91%E5%84%BF%E7%BC%96%E7%A8%8B/cozmo-hello-world/)

<!--
官方的 [cozmo cli](https://github.com/anki/cozmo-python-sdk/blob/master/examples/apps/cli.py) 需要在独立进程中运行，需要做以下修改才能在 notebook 里运行（ 这是jupyterlab 进程模型导致的 ）


```py
# pip install "cozmo[3dviewer]"
import multiprocessing
import time
from IPython.terminal.embed import InteractiveShellEmbed

import cozmo

# Creating IPython's history database on the main thread
ipyshell = InteractiveShellEmbed()
    
def cozmo_program(robot: cozmo.robot.Robot):
    ipyshell()  #  注意 tab补全不生效

cozmo.robot.Robot.drive_off_charger_on_connect = False

def main():
    cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)

p = multiprocessing.Process(target=main, args=())
p.daemon = True
p.run()
```
-->