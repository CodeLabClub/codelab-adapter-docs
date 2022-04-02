# 特殊版本

## windows

-   [mediapipe](https://scratch3-files.just4fun.site/codelab-adapter-4_9_6-mediapipe-win64.zip)
-   [mediapipe-cvzone](https://scratch3-files.just4fun.site/codelab-adapter-4_9_6-mediapipe-cvzone-win64.zip)
    -   用于 1117 的 AI 演示

## macos

-   [mediapipe-cvzone](https://scratch3-files.just4fun.site/codelab-adapter-4_9_6-mac-mediapipe-cvzone.zip)
    -   如果无法双击打开，可进入软件包内部打开: 右键显示包内容, `Contents/MacOS/CodeLab-Adapter`

<!--
https://scratch3-files.just4fun.site/codelab-adapter-4_9_6-mac-mediapipe.zip
-->

## FAQ

### import mediapipe 失败
在有些 windows 系统上可能会发生这个问题(DLL加载失败)，尚不清楚这个问题。 <!--重新安装mediapipe也无效-->

如果你只需要在 jupyterlab 里使用 mediapipe，而无需 Adapter 的其他功能。可下载官方的 [jupyterlab-desktop](https://github.com/jupyterlab/jupyterlab-desktop/releases)， 然后使用安装依赖。

```py
import pip
pip.main(['install', 'mediapipe', '-i', 'https://pypi.douban.com/simple'])
```
