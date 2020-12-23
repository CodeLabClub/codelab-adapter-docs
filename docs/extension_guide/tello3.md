# Tello 3.0

Tello 插件的 3.0 版本， 基于 DJI 官方的 SDK: [RoboMaster SDK](https://robomaster-dev.readthedocs.io/zh_CN/latest/python_sdk/beginner_drone.html)库。

能够充分利用设备的能力。

相比于 [Tello 2.0 插件](/extension_guide/tello2/)，3.0能够[控制 LED](https://robomaster-dev.readthedocs.io/zh_CN/latest/python_sdk/beginner_drone.html#led)

# 使用说明
目前该插件并未内置到 Adapter 中（因其复杂的打包依赖，而且跨平台兼容性不好）。

我们目前将插件构建为 [Adapter Node](https://adapter.codelab.club/dev_guide/Adapter-Node/)，可以在Adapter外部以普通Python文件运行，一旦运行起来，与普通Adapter插件是一样的，能够与Adapter体系的所有事物交互。

## Python环境
首先你本地需要有 Python 环境（`Python>=3.6`）

你可以到 [Python 官方](https://www.python.org/)下载，也可以使用 CodeLab放在[国内的版本(Python3.7)](https://www.codelab.club/blog/2020/08/20/tools#python)

!!! 提醒
    Mac 用户和 Linux 本地很可能内置了 Python3

### 安装依赖
```bash
pip install robomaster codelab_adapter_client --upgrade 
```

## 开始！

!!! 提醒
    Tello 会占用 wifi，导致电脑无法联网，请使用 CodeLab Adapter 的离线模式: [FAQ：离线使用](/user_guide/FAQ/#_6) (在`>=3.4.0`的版本中可用)。  
    更好的方式可能是将Tello接入路由器上，或者使用USB无线网卡，避免电脑无法上网。


### 步骤 1：打开 [CodeLab Scratch](https://scratch-beta.codelab.club)
运行CodeLab Adapter， 确保在线平台与Adapte连接正常。

看到 [CodeLab Scratch](https://scratch-beta.codelab.club) 指示灯显示绿色，代表连接成功。

![](/img/v2/codelab-scratch3.png)

<!--
下载 [CodeLab Scratch Desktop(离线版)](https://www-old.codelab.club/blog/2020/08/20/tools/)，并运行它。

![](../img/scratch3-home.png)
-->
### 步骤 1：运行[node_tello3.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_tello3.py)

将 [node_tello3.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_tello3.py) 插件下载到本地（随便放在一个文件夹里），在命令行中进入到这个文件夹，使用 `python node_tello3.py` 运行它。

### 步骤 2：连接 Tello

将电脑连上 Tello 的 wifi 热点。（操作细节可以参考 Tello 说明书）


### 步骤 3: 起飞吧!

选择 scratch3 中的 EIM 插件.

<!--<img width="600px" src="/img/scratch3_tello.png"/>-->

以下是一个简单 demo: 

![](/img/d5f48154f5c40003eeb416137b1055ad.png)


[tello3-demo](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-tello3.sb3)


<!--![](/img/870f31bff87dc33c9640280c786ca483.png)-->

<!--<img width="600px" src="/img/46f87c6602288de4df896243fc87a3dc.png"/>-->

起飞吧！

# 进阶

更多API参考文档: [RoboMaster SDK](https://robomaster-dev.readthedocs.io/zh_CN/latest/python_sdk/beginner_drone.html)