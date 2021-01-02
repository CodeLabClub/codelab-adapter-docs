# RoboMaster
RoboMaster EP

!!!提醒
    目前只支持RoboMaster EP(暂不支持S1)，受限于大疆的开放接口: [RoboMaster SDK 新手入门 - EP 篇](https://robomaster-dev.readthedocs.io/zh_CN/latest/python_sdk/beginner_ep.html)

# Tutorial
## 依赖

{!utils/dependence.md!}

## 步骤 1：打开 Codelab Adapter

{!utils/open_adapter.md!}

## 步骤 2：打开 Codelab Scratch3

{!utils/open_scratch.md!}

## 步骤 3：将 RoboMaster 接入局域网里
开启 RoboMaster ，[将其接入局域网里](https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/connection.html#id5)

## 步骤 4：hello world
现在让我们利用 Scratch3 控制 RoboMaster: 使用键盘的上下左右/空格来控制机器人移动和发射水弹。

![](/img/f0828fd6c8ca1f7b1fb731554da427b9.png)

<!--
![](/img/9325aa8542cc752d4cea3d2c636b9449.png)

点击打开项目: [robotmaster-helloworld](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-RoboMaster-helloworld.sb3){target=_blank}
-->

## 更多
协议细节参考[ robomaster-dev 协议内容](https://robomaster-dev.readthedocs.io/zh_CN/latest/sdk/protocol_api.html)

!!! 提醒
    如果你希望做一些更复杂的事，建议直接使用社区里的 Python SDK与 设备交互，之后使用 [Adapter Node](/dev_guide/Adapter-Node/) 将其接入Adapter环境中。
