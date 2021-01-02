# DJI Tello

!!! tello
    请使用 [tello2.0](/extension_guide/tello/)

<!--
可以在[插件市场](/extension_guide/extension_market/)中下载 Tello 插件。
添加注释-->

!!! 提醒
    Tello 会占用 wifi，导致电脑无法联网。有两种方式在 CodeLab Scratch 使用它:  
    1. 打开 `https://scratch-beta.codelab.club?adapter_host=127.0.0.1`  
    2. 使用 CodeLab Adapter 的离线模式：[FAQ：离线使用](/user_guide/FAQ/#_6) (在`>=3.4.0`的版本中可用)

以下是在线版使用教程，离线版基本相似。


### 步骤 1：打开 [CodeLab Scratch](https://scratch-beta.codelab.club?adapter_host=127.0.0.1)
运行CodeLab Adapter， 确保在线平台与Adapte连接正常。

第一次运行请点击`verify`积木，信任该网站。(离线版不需要)

看到 [CodeLab Scratch](https://scratch-beta.codelab.club?adapter_host=127.0.0.1) 指示灯显示绿色，代表连接成功。

![](/img/v2/codelab-scratch3.png)

<!--
下载 [CodeLab Scratch Desktop(离线版)](https://www-old.codelab.club/blog/2020/08/20/tools/)，并运行它。

![](../img/scratch3-home.png)
-->

### 步骤 2：连接 Tello

将电脑连上 Tello 的 wifi 热点。（操作细节可以参考 Tello 说明书）

### 步骤 3：开始使用

选择 scratch3 中的 Tello 插件：

<img width="600px" src="/img/scratch3_tello.png"/>



运行 Tello 插件。

![](/img/870f31bff87dc33c9640280c786ca483.png)

之后依次点击 `控制飞机` 、 `起飞`

<img width="600px" src="/img/46f87c6602288de4df896243fc87a3dc.png"/>

起飞吧！

# 一些案例:

## DJI Tello x Leap Motion

<video width=300px src="/video/tello_leapmotion.mp4" controls="controls"></video>

## DJI Tello x Switch Labo

<video width=300px src="/video/tello_labo.mp4" controls="controls"></video>

## DJI Tello x Switch Joy-Con

<video width=300px src="/video/tello_joy_con.mp4" controls="controls"></video>

# 改进
目前 Tello 的插件都已开源，很久没更新，稳定性不高，大家可以一起改进它

*  [extension_tello](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_tello.py)
*  [scratch3_tello](https://github.com/CodeLabClub/scratch3_tello)

!!! 提醒
    如果你希望做一些更复杂的事，建议直接使用社区里的 Python SDK与 设备交互，之后使用 [Adapter Node](/dev_guide/Adapter-Node/) 将其接入Adapter环境中。

## Tello api 文档
*  [SDK 2.0](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf)
*  [DJITelloPy](https://github.com/damiafuentes/DJITelloPy)
<!--
*  [TelloPy](https://github.com/hanyazou/TelloPy)
*  [Tello-Python](https://github.com/dji-sdk/Tello-Python)
-->
*  [multi_robot_drone_example](https://robomaster-dev.readthedocs.io/zh_CN/latest/python_sdk/multi_robot_drone_example.html)