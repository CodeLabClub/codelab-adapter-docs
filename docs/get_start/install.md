# 安装 Codelab Adapter

## 版本介绍

要使用 CodeLab Adapter（下面简称Adapter），第一步当然是安装Adapter。

目前 CodeLab Adapter v3 可以在Mac、 Windows、 Linux、Raspbian（树莓派） 平台上正常运行。Adapter目前有分为两个版本可供小伙伴们选择 **完整版** 和 **精简版**。这两个版本该如何选择呢？

在 Adapter 的介绍中，我们介绍 Adapter 两个核心组件“Extension（插件）” 和 “Node（结点）”的功能，不熟悉的小伙伴可以[回顾Adapter的介绍](null)。

Adapter两个版本的区别就在于 **完整版 Adapter** 能够**直接使用** Adapter Node 的功能而无需额外安装 Adapter Node 所需要的依赖（第三方Python库）。而**精简版 Adapter**需要使用者自行安装额外的依赖才能使用Adapter Node的功能。为了说明区别，请看下表 : )

|   版本   | Adapter Extension（插件） | Adapter Node（结点） |              目标用户               |
| --------- | ---------------------------------------- | --------------------------------- | ---------------------------------- |
| 完整版 | Yes                                         | Yes                                  | 初学者                                |
| 精简版 | Yes                                         | 需要另外安装依赖         | 喜欢折腾和自定义的用户 |

ps：开发者请参看[完整的版本介绍](null)

---

## Adapter下载链接 {#download}

|           操作系统           |                                                                   完整版                                                                   |                                                               精简版                                                               |                           系统要求                           |         安装注意事项         |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------- |
| macOS                       | [macFull.zip](https://scratch3-files.just4fun.site/codelab-adapter-3_5_1-mac-full.zip) | [macLite.zip](https://sratch3-files.just4fun.site/codelab-adapter-3_5_1-mac.zip) | macOS 10.13.5（64位）+                         | [mac安装步骤](#mac)   |
| Windows                    | [winFull.zip](https://scratch3-files.just4fun.site/codelab-adapter-3_5_1-win-full.zip)   | [winLite.zip](https://sratch3-files.just4fun.site/codelab-adapter-3_5_1-mac.zip)  | Win 7 /8 /10  （32位/64位）                    | [win安装步骤](#win)      |
| Linux                           | 无                                                                                                                                             | [linux.zip](https://scratch3-files.just4fun.site/codelab-adapter-3_5_1-linux.zip)   | 经测试发行版Ubuntu、Kail、ArchLinux | [linux安装步骤](#linux) |
| Raspbian（树莓派） | 无                                                                                                                                             | [rpi.zip](https://scratch3-files.just4fun.site/codelab-adapter-3_5_1-rpi.zip)          | 低于buster的版本可能无法运行               | [树莓派安装步骤](#rpi) |

---

## 在Mac中安装Adapter {#mac}

1. [下载](#download)
2. 双击.zip格式文件就会得到可执行的Adapter
    ![mac1](/img/install_mac1.png)
3. 点击右键打开，会出现
    ![mac2](/img/install_mac2.png)

    点击打开就会弹出Adapter的浏览器页面
    ![success](/img/getstart_adapter_ui.png)

到此在Mac中安装Adapter完成。

温馨提示：在 macOS 10.15 打开软件可能会比较慢(有时需要3-5秒)，问题目前在定位中，但在打开后不影响使用。

## 在Windows中安装Adapter {#win}

1. [下载](#download)
    ![win1](/img/install_win_1.png)
2. 右键解压,然后进入解压后的文件夹（为了方便使用，可以将adapter添加到桌面）
    ![win2](/img/install_win_2.png)
3. 进入解压后的文件夹点击运行Adapter，会自动弹出默认浏览器（推荐使用Firefox或者Chrome浏览器）。
    如果出现防火墙的警报，点击允许访问就好了。
    ![win3](/img/install_win_3.png)

    看到一下界面就说明安装成功了。
    ![win4](/img/getstart_adapter_ui.png)

温馨提示：Windows 7下最好以管理员权限运行。

## Linux中安装Adapter {#linux}

1. [下载](#download)
2. 用unzip命令解压
3. 在命令行中运行Adapter就会自动弹出

温馨提示：

- 无法运行请赋予可执行权限`chmod u+x xxx`
- 在Ubuntu 16.04下可能无法自动打开浏览器。建议在命令行下启动它，你将看到`https://codelab-adapter.codelab.club:12358/?token=TOKEN`, 这个链接即是 WebUI
- 欢迎测试其他Linux发行版，有问题点击下方的联系我们:)

## 在Raspbian中安装Adapter(build中...) {#rpi}

1. 下载
2. 解压
3. 赋予运行权限：`chmod +x xxx`，运行

---

接下来我们将进入使用Adapter的环节，通过两个例子看看Adapter可以做些什么吧。

在安装中如果遇到问题，欢迎[联系我们](/about/contact/)。
