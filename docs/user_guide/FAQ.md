# FAQ

## 与官方的 [Scratch Link](https://scratch.mit.edu/microbit) 有什么差异？

兼容性方面：

[Scratch Link](https://scratch.mit.edu/microbit) 目前有以下依赖：

- Windows 10 version 1709+
- macOS 10.13+
- Bluetooth 4.0

CodeLab Adapter 对平台和操作系统没有这么高的要求，我们支持：

- Windows 7、Windows 8、Windows 10（32 位/64 位都支持）
- macOS 大多数版本
- Ubuntu
- 树莓派
- 其他 linux 发行版

[Scratch Link](https://scratch.mit.edu/microbit)
；
在连接能力上，[Scratch Link](https://scratch.mit.edu/microbit) 目前只支持 BLE，CodeLab Adapter 支持任何的连接：

- USB
- WIFI
- Bluetooth 2.0/Bluetooth 4.0
- 大多数的协议（http/websocket/mqtt/ZeroMQ/socket……）
- ...

CodeLab Adapter killer 特性之一是允许普通用户（Scratcher）[使用 Python 拓展 Scratch 的能力](https://wwj718.github.io/scratch-adapter-eim-script.html)。

CodeLab Adapter killer 特性之二是允许开发者和公司使用 Python 构建自定义的插件，轻松将任何硬件/AI/IOT 设备接入到 Scratch 3.0 中。

Scratch 官方计划开源 [Scratch Link](https://scratch.mit.edu/microbit)，一旦它们开源，我们将在 CodeLab Adapter 通过插件实现 Scratch Link 的所有功能。

如果你目前要使用以下三种硬件，我们推荐你先使用 Scratch Link。未来我们会和官方的功能完全一样。

- [Wedo2.0](https://scratch.mit.edu/wedo)
- [micro:bit](https://scratch.mit.edu/microbit)
- [EV3](https://scratch.mit.edu/ev3)

Scratch Link 和 CodeLab Adapter 可以协同工作。

CodeLab Adapter 致力于提供更好的跨平台支持和开放的[插件系统](https://github.com/CodeLabClub/codelab_adapter_extensions)，CodeLab Adapter 的目标是连接万物，不只是连接教育硬件。

## CodeLab Adapter 与 [CodeLab Scratch3](https://scratch-beta.codelab.club/) 是否连接成功？

CodeLab Adapter 启动之后，可以看到 [CodeLab Scratch3](https://scratch-beta.codelab.club/) 指示灯显示绿色，代表连接成功。

<img alt="" src="/img/scratch3-home-connect.png">

## 启动 CodeLab Adapter 后，与 scratch3 无法通信怎么办？

检查下是不是打开了科学上网的软件， 不要使用全局模式。

## CodeLab Adapter 可以支持其他平台吗？

CodeLab Adapter 可以支持其他编程平台吗？而不只是在 CodeLab 的平台上使用。

可以的！

CodeLab Adapter 几乎支持任何平台，无论是 Scratch 3.0 构建的还是 blockly 构建的（如 Tynker 和 code.org）的，或者你用其他什么黑魔法构建的，都没问题！

这是目前的接入文档：[codelab-adapter 支持第三方平台](https://wwj718.github.io/post/少儿编程/codelab-adapter-open-plan/)。

相关的合作条款我们正在构建中。

期待接入 CodeLab Adapter 的公司或组织，欢迎联系我们：`wuwenjie718@gmail.com`

来信请注明公司/组织的一些基本信息，以及你们正在做的事情 ：）

## Python 版本(CodeLab Adapter 4.5)

我们在不同操作系统打包时，使用的 Python 版本不同。

- Windows：3.7.6
- macOS：3.8.7
- Raspbian：3.7
- Ubuntu：3.7

详情可以查看WebUI菜单里的 `环境 > 查看`

## 如何使用 Python 拓展 Scratch 的能力？

-   [Python对象的连接器：EIM 插件](/project_tutorial/eim_pt/)
-   [hello world(Adapter Extension)](/dev_guide/helloworld/)
-   [Adapter Node](/dev_guide/Adapter-Node/)

## 如何找到 Adapter 主目录
Adapter 主目录，也是 Adapter 的日志目录，这儿存放了 Adapter 运行时使用的数据。

*  Windows: `C:\Users\<CurrentUserName>\codelab_adapter`
*  Mac/Linux: `~/codelab_adapter`

如果找不到插件目录（如 Windows 用户），可以通过 CodeLab Adapter Web UI 工具栏里的`插件->打开插件目录`打开它。

## 如何找到插件目录

Mac/Linux 用户的插件目录在：`~/codelab_adapter/extensions`，如果找不到插件目录（如 Windows 用户），可以通过 CodeLab Adapter Web UI 工具栏里的`插件->打开扩展目录`打开它，之后找到`extensions`文件夹。

![](/img/70554ac8052ccaf33175aa851893fd6c.png)

## 用户配置文件放在哪儿

`~/codelab_adapter/user_settings.py`.

Windows 用户如果找不到用户配置文件目录，可以通过 CodeLab Adapter Web UI 工具栏里的`插件->打开插件目录` 先打开插件目录，用户配置文件在它的外层。

## CodeLab Adapter 网址是什么

[scratch-beta.codelab.club](https://scratch-beta.codelab.club/)，你不需要记住， 可以在 Web UI 中打开它。

## 目前都支持哪些插件

[codelab_adapter_extensions](https://github.com/CodeLabClub/codelab_adapter_extensions)。

## 支持移动端吗（iPad/手机）
Adapter 无法直接运行在移动端（可以运行在安卓的linux模拟器（如Termux）上）

在移动端上使用 Adapter 的方式是，将 Adapter 运行在计算机(如树莓派)上，之后通过url参数指向它:  `https://scratch-beta.codelab.club/?adapter_host=192.168.31.140`

但由于不同平台对 https 的限制策略不同，可能需要一些处理技巧。

这是一个[例子](/video/codelab_ipad.mp4)。

## 自定义存储目录

使用环境变量`ADAPTER_HOME_PATH`来软件 home 目录，

例子：`ADAPTER_HOME_PATH=/tmp/my_adapter_home ./codelab-adapter --cli`

## 离线使用
CodeLab Adapter 支持离线使用，目前有 3 种方式使用它。

1. (推荐) 修改host，添加一条`127.0.0.1 codelab-adapter.codelab.club` , [详情](#codelab-adapter_3)
2. 配合 [CodeLab Scratch Desktop（离线版）](https://www.codelab.club/blog/2020/08/20/tools/)使用。
3. 将 Web UI 里的`codelab-adapter.codelab.club`替换为`127.0.0.1`，形如 `https://codelab-adapter.codelab.club:12358/?token=YOUR_TOKEN`，重新刷新页面。

推荐使用`方法 1`。

典型的应用场景是在电脑无法联网时，诸如使用 [Tello](/extension_guide/tello/) 时。

## 查看本地环境

![](/img/34ab42207fe08a68b255f117ae82a99d.png)

你将看到:

![](/img/54cef2d640ff035f772a64425811d6aa.png)

其中包含了当前 Adapter 所处的计算机环境相关的信息。

## 软件意外退出
当最后一个 client(webui) 关闭时，Adapter将退出。

所以你在刷新webui时也能导致它退出(刷新意味着某个时刻断开)

## 分布式使用 CodeLab Adapter
[@在梦里 同学](https://rcfclass7.wordpress.com/author/muleizhang/) 提到在树莓派里运行 Scratch 比较卡(需要WebGL)。

CodeLab Adapter 有很好的分布式支持:

1. [Adapter Node](/dev_guide/Adapter-Node/) 可以与 CodeLab Adapter 分布式协同
2. CodeLab Adapter 可以与 Scratch 分布式协同

为了解决 **树莓派里运行 Scratch 比较卡** 的问题，我们 可以让Adapter 运行在树莓派里，Scratch 则运行在本机上。

首先在树莓派中运行CodeLab Adapter，复制 WebUI 的URL, 形如: `https://codelab-adapter.codelab.club:12358/?token=765b3d2901ef47a0`

将 codelab-adapter.codelab.club 修改为 树莓派的 IP 地址: `https://192.168.21.104:12358/?token=765b3d2901ef47a0`。

现在你可以在 PC 里打开 树莓派里的 Adapter(需要安全校验) :


接着让我们在 CodeLab Scratch 里使用它, 打开: `https://scratch-beta.codelab.club/?adapter_host=192.168.21.104` (adapter_host 是 adapter 所在计算机的 IP，即树莓派的 IP， 它甚至可以运行在互联网的任何设备，任何位置！包括手机！)

![](/img/6836f24ab4bcfd48cb648d68e98b190a.png)

!!! tips
    考虑到隐私，CodeLab Neverland 自建了聊天服务器，利用的正是以上机制，CodeLab办公室里的计算机都接入 树莓派上的 Adapter。

## 如何在离网状态下使用CodeLab Adapter
在某些情况下，可能处于离网状态（诸如控制[tello](/extension_guide/tello/)时，需要连接到tello网络)

@RedYin 给出了一个技巧: 修改hosts

添加如下host规则:

`127.0.0.1 codelab-adapter.codelab.club`

以下是不同系统的hosts文件所在位置

*  Windows: `C:\Windows\System32\drivers\etc\hosts`
*  Android: `/system/etc/hosts`
*  Mac/Linux: `/etc/hosts`
*  iPhone: `/etc/hosts`

## Windows 系统常见文件

### 提示`缺少Python3`

可能是你把 Adapter 当到了带有 **空格** 的文件夹里了。

## 如何获取文件路径
以下是windows 10 下的操作: `右键目标文件 -> 属性`

![](/img/56e266852fbc94ef92d7b5d3f3125d38.png)

## 为何有些网络下会无法Adapter发现/连接wifi设备
这种情况，可能发生在wifi设备（悟空机器人、Romomaster EP）

当你换一个网络就可用时， 那么问题可能是在某个网络启动Adapter，系统询问你是否允许其连接公共网络，你没有同意。

可能的操作方法为: [Win10系统禁止/恢复某个程序连接网络的方法](https://jingyan.baidu.com/article/22a299b5e6fa909e18376a55.html)

允许 adapter 内置的Python连网络（Python路径可在WebUI中看到）

## 如何排查 无法发现设备 的问题？

打开Adapter内置的 jupyterlab 插件，打开 `notebooks目录 > devices-connect-test.ipynb`，测试对应设备的连接，如果此处显示 **发现** 设备，但Adapter插件无法与设备连接，说明是Adapter插件问题，请[给我们反馈bug, 最好配上截图或视频](https://discuss.codelab.club/)； 如果此处显示 **未发现** 设备，则与Adapter无关，请检查你的网络、USB连接、以及设备是否正常。

## MacOS 应用程序没有响应
如果你遇到以下情况

![](/img/346c5c462dd40a400190776d20f557d2.png)

可以通过以下方式重新打开Adapter: `右键 -> 显示包内容 -> Contents -> MacOS -> CodeLab-Adapter`

![](/img/a6d9b53aeb3130be823d00f3459c1aef.png)

点击运行目录里的 CodeLab-Adapter

![](/img/543790264e75c9e3b679c954fa8fdd39.png)

如果因此导致无法关机， `control + command + 电源键` 或者 `长按电源键`

## webUI 无法退出Adapter （token错误）
### MacOS
![](/img/e6eb3d2326b6a661f39ff99a44bb9298.png)

### Windows 
图标在页面右下角, 右键退出。

### Linux & RPI
`pkill -f codelab-adapter`

## 之前安装过旧版本的Adapter，使用新的版本出现问题
退出Adapter。

手动删除 [Adapter 主目录](#adapter)， 位置在:

*  Windows: `C:\Users\<当前用户名>\codelab_adapter`
*  Mac/Linux: `~/codelab_adapter`

## MacOS 11 无法扫描蓝牙设备
现象: 使用蓝牙设备(诸如overdrive) ，系统会提示蓝牙未开启。

原因: MacOs 权限管理更为严格，需要授权。

解决方案: 从软件包里打开 Adapter，然后授权。

可以通过以下方式重新打开Adapter: `右键 -> 显示包内容 -> Contents -> MacOS -> CodeLab-Adapter`

![](/img/a6d9b53aeb3130be823d00f3459c1aef.png)

点击运行目录里的 CodeLab-Adapter

![](/img/543790264e75c9e3b679c954fa8fdd39.png)