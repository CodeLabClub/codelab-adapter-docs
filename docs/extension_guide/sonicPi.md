# Tutorial

![](/img/44fe13429c50c93fcef527360c1ae6ac.png)

## 介绍
![](https://upload.wikimedia.org/wikipedia/en/a/aa/Sonic-pi-v3.2.0-gui-screenshot.png)

Sonic Pi 是一个基于代码的音乐创作和表演工具。

拥有超过180万用户的多元社区。

基于 Ruby 开发，最初设计用于支持学校的计算和音乐课程，由剑桥大学计算机实验室的 Sam Aaron 与树莓派基金会联合开发。可在主流操作系统中使用。

### 外部环境依赖

需要下载[Sonic Pi](https://sonic-pi.net/)。

## 开始使用

运行 Sonic Pi。

启动 CodeLab Adapter，运行 node_sonicPi 插件。

打开 Scratch 编程界面，我们已经制作了一个 demo:[Scratch-SonicPi](https://scratch-beta.codelab.club?sb3url=https://adapter.codelab.club/sb3/Scratch-SonicPi.sb3)。

<video src="/video/1588741044537372.mp4" controls="controls"></video>


## 进阶

更多可用的指令，参考[python-sonic](https://github.com/gkvoelkl/python-sonic)。

如果你想深入了解[Sonic Pi](https://sonic-pi.net/)，可以跟着 Sonic Pi 软件内置的文档学习。

### 发送消息
`>= 3.7.2` 的 Adapter 支持使用Scratch积木发送OSC消息，消息的参数(args)是一个 list(采用json语法，字符串使用 **双引号** )

### Receiving OSC
[Sonic Pi Receiving OSC](https://sonic-pi.net/tutorial.html#section-12-1)

参考这个文档，你也可以基于[python-sonic](https://python-osc.readthedocs.io/en/latest/client.html#example)构建一个[自定义插件](/project_tutorial/eim_pt/#python)直接与Sonic Pi沟通。

## FAQ

### Linux用户
Windows 和 Mac 用户开箱可用。Linux用户将自动安装依赖。

Linux （Ubuntu 20.0）环境下安装完 Sonic Pi 后可能会出现程序无法启动的问题，这可能是因为 JACK 与 PulseAudio 在使用声卡上存在冲突造成的，参见 Sonic-Pi 仓库内这个 [issue 对该问题的讨论及最终的解决方法](https://github.com/sonic-pi-net/sonic-pi/issues/1025) 以及 [JACK 官方文档对相关问题的解释](https://jackaudio.org/faq/pulseaudio_and_jack.html)。具体的操作是：

1. 在启动 Sonic-Pi 之前，先打开 QjackCtl（安装 Sonic-pi 时会自动安装），在 `Settings-Advanced`页面下，在 `Input Device` 中选择一个声卡，同时将 `Server Prefix` 修改为 `pasuspender -- /usr/bin/jackd`（我对此操作的理解是明确地为 JACK 选择一个声卡，同时暂停 PulseAudio 对它的可能占用。）
2. 设置完成后保存，然后在控制页面上点击开始按钮，如果一切顺利终端内没有报错的话，这时再去运行 Sonic Pi 应该就会正常启动了。

![Selection_023](https://user-images.githubusercontent.com/61407739/115480135-7b1bdc80-a27c-11eb-8b49-29a84f04ad7e.png)

## 参考

-   [Sonic Pi](https://sonic-pi.net/)
-   [python-sonic](https://github.com/gkvoelkl/python-sonic)
