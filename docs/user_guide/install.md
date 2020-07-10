# 安装（install）

CodeLab Adapter v3 目前发布了 Mac、Windows（支持 windows 7 及以上版本）、Ubuntu、Raspbian（树莓派）的客户端.

## 下载（最新版本：3_3_2）

你可以免费下载（点击对应的操作系统链接）：


*  [macOS（64bit）](https://scratch3-files.just4fun.site/codelab-adapter-mac-3_3_2.zip)
    *  macOS 10.13.5+
    *  如果你点击应用闪退，请参考：[打开来自身份不明开发者的应用](https://support.apple.com/kb/PH25088?locale=zh_CN&viewlocale=zh_CN)
* Windows（Windows 7 及以上）
    * [Windows](https://scratch3-files.just4fun.site/codelab-adapter-win_3_3_2.zip)：Windows 7、Windows10 已测试（32 位和 64 位都可用）
        *  Windows 7下最好以管理员权限运行。
* [Linux](https://scratch3-files.just4fun.site/codelab-adapter-kali_3_3_2.zip)
    *  构建于 Kali linux
    *  在Ubuntu 20.04下测试可用
    *  在Ubuntu 16.04下可能无法自动打开浏览器。建议在命令行下启动它，你将看到`https://codelab-adapter.codelab.club:12358/?token=TOKEN`, 这个链接即是 WebUI
* [Raspbian](https://scratch3-files.just4fun.site/codelab-adapter-rpi-3_3_1.zip)(构建中...)
    * 在 Raspbian buster 版本中构建, Raspbian的版本低于 buster 可能无法使用。
    * 下载，解压，赋予运行权限：`chmod +x xxx`

<!--
## 更新

{!utils/update.md!}
-->

## 兼容性

目前，Windows 和 Mac 的版本测试过的机器比较多。

Linux  测试了 
    *  Ubuntu 
        *  16.04
        *  20.04
    *  kali
    *  如果你在使用其他 linux 发行版，欢迎尝试


Raspbian 我们只测试了最新版本，如果有系统兼容性问题，欢迎[联系我们](/about/contact/)。

<!--
ps: macOS 10.14 下，按钮无法显示文字, 但不影响正常使用 (按钮文字 可以参考下图)

<img src="../../img/adapter-exit-button.png" width=400 />
-->
