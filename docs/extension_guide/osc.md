# OSC (Open Sound Control)

## 介绍

[OSC (Open Sound Control)](http://opensoundcontrol.org/introduction-osc)是一种用于将声音合成器、计算机和其他多媒体设备联网的协议，用于音乐表演或表演控制等目的。OSC 的优势包括互操作性，准确性，灵活性以及增强的组织和文档。

最新版的 CodeLab Adapter 内置了 OSC 服务，端口为`12361`

CodeLab Adapter即可充当 OSC server，又可充当 OSC client， 两类积木都提供了

## hello world
使用 OSC 客户端(诸如Syntien) 往 Adapter 发送消息。

在 Scratch OSC 插件积木里接收消息。

## 积木说明

![](/img/2a3227e7409216a400663f2bff7f7ab0.png)

## 项目链接

### demo

<video width=80% src="/video/1603105233433018.mp4" controls="controls"></video>

### osc 手写板

[osc 手写板](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/osc-画笔.sb3)

![](/img/79b20aed4bfe26ff5e8f1510e6414246.png)

如果你使用 IPhone 或者其他支持压力输入的屏幕，则可以通过按压力度控制画笔粗细。

### 操作说明

下载 OSC 软件(演示视频里用的是`Syntien`), 将其配置到 Adapter OSC Server 上（`Adapter_IP:12361`）

<img width="350" src="/img/WechatIMG1681.jpeg"/>

之后进入 interface，开始操作即可。

输出的 osc 信号将进入 Adapter，继而可以在 Scratch 的 OSC 积木中访问它。

一则 osc 消息由 2 部分构成:

-   address(地址，类似 url)
-   args（参数，是个 list）, 每一个参数的含义请参考具体 OSC 软件的文档说明

address 和 args 可以在具体 osc 软件中找到。

## FAQ

### 有什么推荐的 OSC 面板(client)
我目前最喜欢的 OSC client 是:

*  `Syntien`
*  `Unipad`

#### Syntien
Syntien 提供了丰富的控制面板

<img width="350px" src="/img/WechatIMG1686.jpeg"/>
<img width="350px" src="/img/WechatIMG1687.jpeg"/>
<img width="350px" src="/img/WechatIMG1688.jpeg"/>

<img width=80% src="/img/WechatIMG1685.jpeg"/>

它甚至允许你自定义面板！

<img width=80% src="/img/WechatIMG1690.jpeg"/>



#### Unipad

<img width=80% src="/img/WechatIMG1693.jpeg"/>

<img width=80% src="/img/WechatIMG1692.jpeg"/>

<img width="350px" src="/img/WechatIMG1691.jpeg"/>


Unipad 提供多种游戏手柄界面，这些可以很好地跟Scratch项目结合！ OSC 如此高的刷新率，几乎没有任何延迟

### 有什么推荐的兼容 OSC 的软件

*  音乐: [SonicPi](/extension_guide/sonicPi/)
*  AI：[Wekinator](http://www.wekinator.org/)
*  blender/unity