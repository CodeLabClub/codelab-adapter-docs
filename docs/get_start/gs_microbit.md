# Adapter插件——Micro:bit say：“Hello”

在上一个项目中，我们使用了Adapter插件让小猫帮我们打开了网页，这一次 **我们用Adapter插件将创作平台和Micro:bit连接起来。让我们在创作平台操控Micro:bit。**

## Micro:bit概览

> Micro:bit是一个小型的可编程计算机，旨在使学习与教学变得轻松有趣

![](/img/gs_microbit-overview.png)

Micro:bit就是一块小小的电路板，我们可以用它显示一个爱心和各种好玩的图案，还可以用它来控制创作平台的小猫。当然它功能远不止这些。想了解更多可以到[Micro:bit学习资源](https://github.com/wwj718/awesome-microbit-zh)。

## Micro:bit：“Hello”

现在我们开始使用Adapter来连接Micro:bit，让Micro:bit显示出“Hello”。

### 第一步：连接Micro:bit

使用数据线将 micro:bit 接入电脑，这时候会看到Micro:bit的黄灯闪烁一会，就停止了。随后打开Codelab Adapter。

温馨提示：Windows 7 用户注意（Mac 和 Windows 10 用户可以跳过），为了能发现并连接 micro:bit，需要[安装驱动](/img/mbedWinSerial_16466.exe)（下载后运行即可）

### 第二步：添加MicroBit扩展

![](/img/gs_microbit1.gif)

在点击刷入固件之后， 会看到Micro:bit一直闪烁， 稍等片刻，固件就刷好了。这时我们就将创作平台和Micro:bit连接起来了。

温馨提示：Linux 非root用户注意，在刷入固件之前，使用 usb 串口需要做权限设置：`sudo chmod 666 /dev/ttyACM0`。

### 第三步：开始编程

我们尝试用积木块使Micro:bit say：“Hello”

![](/img/gs_microbit2.gif)

在点击积木块后，Micro:bit就会显示出“Hello”了。

还可以做些什么呢？我们还可以尝试显示一个爱心。还可以。。。请你发挥你的想象力吧!

### 最后

我们尝试用Adapter将创作平台和Micro:bit连接起来，并让Micro:bit Say：“Hello”。

Adapter还可以做些什么呢？ 让我们接下来跟着探索吧。
