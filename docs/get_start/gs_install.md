# 安装 Codelab Adapter

## 版本介绍

经过Adapter的概览，我们了解了Adapter的大致功能，以及插件和节点的功能。 下面我们来安装CodeLab Adapter（简称Adapter）。

目前 CodeLab Adapter v3 可以在Mac、 Windows、 Linux、Raspbian（树莓派） 平台上正常运行。Adapter目前有分为两个版本可供小伙伴们选择 **完整版** 和 **精简版**。这两个版本该如何选择呢？

|   版本   | Adapter Extension（插件） | Adapter Node（节点） |  目标用户 |
| :--: | :---:| :---:| :--:|
| 完整版 | Yes | Yes  | 初学者 |
| 精简版 | Yes| No(需要Python依赖) | 喜欢折腾和自定义的用户 |

附：Adpater完整版所用到的[Python第三方库](https://github.com/CodeLabClub/codelab_adapter_extensions/wiki/%E5%AE%8C%E6%95%B4%E7%89%88%E5%86%85%E7%BD%AE%E5%BA%93(Node))

---

## Codelab Adapter下载链接 {#download}

最新版本: `4.5.0` ([changelog](https://adapter.codelab.club/changelog/))

|     操作系统     |     完整版     |    精简版      |     系统要求   |      安装注意事项      |
| :--------: | :---------: | :--------: | -------- | ---------- |
| macOS  | [macFull.zip](https://scratch3-files.just4fun.site/codelab-adapter-4_5_0-mac.zip) | 无 | macOS 10.13.5（64位）+    | [mac安装步骤](#mac)   |
| Windows  | [winFull.zip](https://scratch3-files.just4fun.site/codelab-adapter-4_5_0-win.zip)   | 无  | Win 7 /8 /10  （32位/64位）| [win安装步骤](#win)      |
| Linux     | 无   | [linux.zip(4.4.0)](https://scratch3-files.just4fun.site/codelab-adapter-4_4_0-linux.zip)   | 经测试发行版Ubuntu、Kail、ArchLinux | [linux安装步骤](#linux) |
| Raspbian（树莓派） | 无   | [rpi.zip(4.2.1)](https://scratch3-files.just4fun.site/codelab-adapter-4_2_1-rpi.zip)   | 低于buster的版本可能无法运行  | [树莓派安装步骤](#rpi) |

附:各个版本的哈希值(Sha256)

<!--

|版本|Sha256|
|--|--|
|macFull|5717ad47203854b9df0656a0e4240eff30d359b9e0c260ca227b3de54a6e19de|
|macLite|bd9302cd3ea9bb2675da1f7ff4381bc8f23f1ad4e1d059d7130100035f552342|
|winFull|0866f971df0885475065bcfe0cc9e4f5d813e2d0c9f7539da46184c7b86a4ffe|
|winLite|fbdf7162ba1701487632ee14317524588c9c02c8119e2829a2ed01a2a2a4f922|
|linux|f7d76b35f3f5eaf4beb337b238e91e2911adf9c8a11070e7c6ef15a21db6b8cb|
|rpi|8115d955b965ecd5099cb0f64828137b46b1010af54ef1fcf337d8ab3408b0fd|
-->

|版本|Sha256|
|--|--|
|macFull|f3455a33f2a1be50af5d615ec6fa1ccfdf0d02d493185ccf2c52054f80e543cd|
|winFull|c9036a8302e57dad7174b2d5d32189b712809c5458f542b9d9bb3db3d4ad4ee9|
|linux|5c6ad1f2f7cdfeca8214b44550f344151d7e5c2864d5a278ced30636da1d4f6e|
|rpi|ce186cbdaf8b45d94aaa43131b17b0da7ce20674474b58a982a16b805325f874|


---

## 在Mac中安装Adapter {#mac}

1. [下载](#download)
2. 双击.zip格式文件就会得到可执行的Adapter
    ![mac1](/img/install_mac1.png)
3. 点击右键打开，会出现
    ![mac2](/img/install_mac2.png)

    点击打开就会弹出Adapter的浏览器页面
    ![success](/img/getstart_adapter.png)

到此在Mac中安装Adapter完成。

温馨提示：在 macOS 10.15 打开软件可能会比较慢(有时需要3-5秒)，问题目前在定位中，但在打开后不影响使用。

## 在Windows中安装Adapter {#win}

1. [下载](#download)
    ![win1](/img/install_win_1.png)
2. 右键解压,然后进入解压后的文件夹, 双击 CodeLab-Adapter 文件。（提醒: 最好不要重命名文件夹，如果要重命名，确保名字中没有中文和空格）
    ![win2](/img/6f482f9d136a541b4df590c9aebade6f.png)

<!--2. 双击安装软件(如果之前安装过，请先卸载旧软件), 安装完成后，可以从 **开始** 菜单栏里启动
    ![win2](/img/7994f69a436f68cc67429fdfac2ade0d.png)-->

3. 运行Adapter，会自动弹出默认浏览器（推荐使用Firefox或者Chrome浏览器）。
    如果出现防火墙的警报，点击允许访问就好了。
    ![win3](/img/install_win_3.png)

    看到一下界面就说明安装成功了。
    ![win4](/img/getstart_adapter.png)
    
<!--
2. 右键解压,然后进入解压后的文件夹（为了方便使用，可以将adapter添加到桌面）
    ![win2](/img/install_win_2.png)
3. 进入解压后的文件夹点击运行Adapter，会自动弹出默认浏览器（推荐使用Firefox或者Chrome浏览器）。
    如果出现防火墙的警报，点击允许访问就好了。
    ![win3](/img/install_win_3.png)

    看到一下界面就说明安装成功了。
    ![win4](/img/getstart_adapter.png)
-->

温馨提示：Windows 7下最好以管理员权限运行。

## Linux中安装Adapter {#linux}

1. [下载](#download)
2. 用unzip命令解压
3. 在命令行中运行Adapter就会自动弹出

温馨提示：

- 无法运行请赋予可执行权限`chmod u+x Adapter软件名`
- 在Ubuntu 16.04下可能无法自动打开浏览器。建议在命令行下启动它，你将看到`https://codelab-adapter.codelab.club:12358/`, 这个链接即是 WebUI
- 当前经测试的发行版有Ubuntu，Kali，ArchLinux
- Linux下需要自行在本地Python环境(`/usr/bin/python3`, 也可以手动设置`PYTHON3_PATH`参数) 安装 Jupyterlab 和 Adapter Node 相关依赖

## 在Raspbian中安装Adapter(build中...) {#rpi}

1. 下载
2. 解压
3. 赋予运行权限：`chmod +x Adapter软件名`，再双击运行
    *  也可以右键修改文件权限，使其可运行

---

## 界面概览

在安装完Adapter之后，我们来看看Adapter的使用界面。
![ui](/img/getstart_adapter_ui.png)

围绕着两个核心组件来看， 整个Adapter的界面就是关于 **插件** 和 **节点** 的管理。比如说，在控制台里， 我们可以查看插件和节点的启用状态，以及打开和关闭我们的插件。然后在创作平台中去使用它们。

以extension开头的就是插件，以node开头的就是节点。

接下来我们将进入使用Adapter的环节，通过两个例子看看Adapter可以做些什么吧。

在安装中如果遇到问题，欢迎[在Codelab社区](https://discuss.codelab.club/)中提出。

# FAQ

<!--
### macOS 安全性
macOS 系统新版本（13.14之后）安全性提高，如果无法运行hack后的软件(Mac应用已损坏，打不开)，如果可能需要先运行: `sudo spctl --master-disable` 或者  `sudo xattr -rd com.apple.quarantine 软件的路径`

jinlei case 
    macOS
        10.15
    之前打不开 后来又好了
        中间做的工作
            sudo chmod -R 777 ./Support
            重启 adapter
    jupyterlab resources
    https://support.apple.com/en-hk/guide/mac-help/mchlp1038/10.15/mac/10.15
    https://www.reddit.com/r/MacOS/comments/caiue5/macos_catalina_readonly_file_system_with_sip/et9a4o1/
-->