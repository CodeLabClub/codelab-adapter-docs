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

CodeLab Adapter killer 特性之一是允许普通用户（Scratcher）[使用 Python 拓展 Scratch 的能力](https://blog.just4fun.site/scratch-adapter-eim-script.html)。

CodeLab Adapter killer 特性之二是允许开发者和公司使用 Python 构建自定义的插件，轻松将任何硬件/AI/IOT 设备接入到 Scratch 3.0 中。

Scratch 官方计划开源 [Scratch Link](https://scratch.mit.edu/microbit)，一旦它们开源，我们将在 CodeLab Adapter 通过插件实现 Scratch Link 的所有功能。

如果你目前要使用以下三种硬件，我们推荐你先使用 Scratch Link。未来我们会和官方的功能完全一样。

- [Wedo2.0](https://scratch.mit.edu/wedo)
- [micro:bit](https://scratch.mit.edu/microbit)
- [EV3](https://scratch.mit.edu/ev3)

Scratch Link 和 CodeLab Adapter 可以协同工作。

CodeLab Adapter 致力于提供更好的跨平台支持和开放的[插件系统](https://github.com/CodeLabClub/codelab_adapter_extensions)，CodeLab Adapter 的目标是连接万物，不只是连接教育硬件。

## CodeLab Adapter 与 [CodeLab Scratch3](https://scratch3v3.codelab.club/) 是否连接成功？

CodeLab Adapter 启动之后，可以看到 [CodeLab Scratch3](https://scratch3v3.codelab.club/) 指示灯显示绿色，代表连接成功。

<img alt="" src="../../../img/scratch3-home-connect.png">

## 启动 CodeLab Adapter 后，与 scratch3 无法通信怎么办？

检查下是不是打开了科学上网的软件。

## CodeLab Adapter 可以支持其他平台吗？

CodeLab Adapter 可以支持其他编程平台吗？而不只是在 CodeLab 的平台上使用。

可以的！

CodeLab Adapter 几乎支持任何平台，无论是 Scratch 3.0 构建的还是 blockly 构建的（如 Tynker 和 code.org）的，或者你用其他什么黑魔法构建的，都没问题！

这是目前的接入文档：[codelab-adapter 支持第三方平台](https://blog.just4fun.site/post/少儿编程/codelab-adapter-open-plan/)。

相关的合作条款我们正在构建中。

期待接入 CodeLab Adapter 的公司或组织，欢迎联系我们：`wuwenjie718@gmail.com`

来信请注明公司/组织的一些基本信息，以及你们正在做的事情 ：）

## Python 版本(CodeLab Adapter 3.0.0)

我们在不同操作系统打包时，使用的 Python 版本不同。

- Windows：3.7.4
- macOS：3.7.2
- Raspbian：3.7.3
- Ubuntu：3.7.5

## 如何使用 Python 拓展 Scratch 的能力？

- [json message](/dev_guide/json-message/)。
- 参考[使用 Python 拓展 Scratch 的能力](https://blog.just4fun.site/scratch-adapter-eim-script.html#_4)。

## 如何找到 Adapter 主目录
Adapter 主目录，也是 Adapter 的日志目录，这儿存放了 Adapter 运行时使用的数据。

Mac/Linux 用户的 Adapter 主目录在：`~/codelab_adapter`，如果找不到插件目录（如 Windows 用户），可以通过 CodeLab Adapter Web UI 工具栏里的`插件->打开插件目录`打开它。

## 如何找到插件目录

Mac/Linux 用户的插件目录在：`~/codelab_adapter/extensions`，如果找不到插件目录（如 Windows 用户），可以通过 CodeLab Adapter Web UI 工具栏里的`插件->打开插件目录`打开它。

![](/img/webui_helper.png)

## 用户配置文件放在哪儿

`~/codelab_adapter/user_settings.py`.

Windows 用户如果找不到用户配置文件目录，可以通过 CodeLab Adapter Web UI 工具栏里的`插件->打开插件目录` 先打开插件目录，用户配置文件在它的外层。

## CodeLab Adapter 网址是什么

[scratch3v3.codelab.club](https://scratch3v3.codelab.club/)，你不需要记住， 可以在 Web UI 中打开它。

## 目前都支持哪些插件

[extensions_v2](https://github.com/CodeLabClub/codelab_adapter_extensions/tree/master/extensions_v2)。

## 支持移动端吗（iPad/手机）
支持。

这是一个[例子](/video/codelab_ipad.mp4)。

## 如何开机自启
从 2.6.2 开始， 支持 headless 模式（[点击下载 Raspbian 版本](/video/codelab-adapter-rpi-2_6_2.zip)），用于开机自启、无人值守的环境。

```
chmod +x codelab-adapter
./codelab-adapter --cli
```

推荐配置为：

```python
# doc: https://adapter.codelab.club/user_guide/settings/
OPEN_MESSAGE_HUB = True
USE_SSL = False
AUTO_OPEN_WEBUI = False
PYTHON3_PATH = None
DEFAULT_ADAPTER_HOST = "codelab-adapter.codelab.club"
OPEN_WEBSOCKET_API = True
OPEN_REST_API = False
TOKEN = "ls3fb138c4124027"
```

之后打开 `http://raspberrypi.local:12358/?token=ls3fb138c4124027`

## 自定义存储目录
2.6.3 开始支持这项功能。

使用环境变量`ADAPTER_HOME_PATH`来软件 home 目录，

例子：`ADAPTER_HOME_PATH=/tmp/my_adapter_home ./codelab-adapter --cli`

## 离线使用
CodeLab Adapter 支持离线使用，目前有 2 种方式使用它。

 1. 配合 [CodeLab Scratch Desktop（离线版）](https://www.codelab.club/blog/codelab-download/)使用。
 2. 将 Web UI 里的`codelab-adapter.codelab.club`替换为`127.0.0.1`，形如 `https://codelab-adapter.codelab.club:12358/?token=YOUR_TOKEN`，重新刷新页面。

推荐使用`方法 1`。

典型的应用场景是在电脑无法联网时，诸如使用 [Tello](/extension_guide/tello/) 时。

## 查看本地环境

![](/img/bdc2f794bd15ed3faab14165b72badc2.png)

你将看到:

![](/img/54cef2d640ff035f772a64425811d6aa.png)

其中包含了当前 Adapter 所处的计算机环境相关的信息。

## 软件意外退出
当最后一个 client(webui) 关闭时，Adapter将退出。

所以你在刷新webui时也能导致它退出(刷新意味着某个时刻断开)

## 分布式使用 CodeLab Adapter
[@在梦里 同学](https://rcfclass7.wordpress.com/author/muleizhang/) 提到在树莓派里运行 Scratch 比较卡(需要WebGL)。

CodeLab Adapter 有很好的分布式支持:

1. [Adapter Node](https://adapter.codelab.club/dev_guide/Adapter-Node/) 可以与 CodeLab Adapter 分布式协同
2. CodeLab Adapter 可以与 Scratch 分布式协同

为了解决 **树莓派里运行 Scratch 比较卡** 的问题，我们 可以让Adapter 运行在树莓派里，Scratch 则运行在本机上。

首先在树莓派中运行CodeLab Adapter，复制 WebUI 的URL, 形如: `https://codelab-adapter.codelab.club:12358/?token=765b3d2901ef47a0`

![](/img/60e122ecf8f946ba72fdc13fe838abfd.png)

将 codelab-adapter.codelab.club 修改为 树莓派的 IP 地址: `https://192.168.21.104:12358/?token=765b3d2901ef47a0`。

现在你可以在 PC 里打开 树莓派里的 Adapter(需要安全校验) :

![](/img/5ca765bc4fc70ad0120f42102a3abc0d.png)

接着让我们在 CodeLab Scratch 里使用它, 打开: `https://scratch3v3.codelab.club/?adapter_host=192.168.21.104` (adapter_host 是 adapter 所在计算机的 IP，即树莓派的 IP， 它甚至可以运行在互联网的任何设备，任何位置！包括手机！)

![](/img/6836f24ab4bcfd48cb648d68e98b190a.png)

!!! tips
    考虑到隐私，CodeLab Neverland 自建了聊天服务器，利用的正是以上机制，CodeLab办公室里的计算机都接入 树莓派上的 Adapter。