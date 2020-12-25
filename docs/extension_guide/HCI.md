# Tutorial

## 依赖

{!utils/dependence.md!}

## 步骤 1：安装依赖
Windows 和 Mac 用户开箱可用。 Linux需要安装依赖:

参考 [PyAutoGUI Install](https://pyautogui.readthedocs.io/en/latest/install.html)

`pip3 install codelab_adapter_client --upgrade`

ps: 使用 Python3

!!! 提醒
    MacOS 升级到最新版本后，可能会导致部分控制类积木无法使用，使系统安全机制升级造成的（我也是可悲的 Mac 用户，下个计算机一定要使用开源系统。）。详情参考:[Pyautogui doesn't seem to work on macOS Mojave](https://github.com/asweigart/pyautogui/issues/247)。 相关问题: [Catalina does not allow to capture the screen](https://github.com/BoboTiG/python-mss/issues/134)。这个问题的结局方案似乎是让系统信任Adapter内置的Python: `codelab-adapter-3_7_3-mac.app/Contents/Resources/Support/bin/python3`

## 步骤 2：打开 Codelab Adapter

{!utils/open_adapter.md!}

## 步骤 3：打开 Codelab Scratch3

{!utils/open_scratch.md!}

## 步骤 4：加载 HCI 插件

在 Web UI 中点击加载 HCI 插件

## 步骤 5：Scratch3 HCI 插件

选择对应的 Scratch3 插件：HCI

# demo
尚雅学校目前在使用 CodeLab Adapter，有位老师想使用魔杖激活开场视频，使用 HCI 插件可以轻松做到:

<video width=80% src="/video/1608689235907497.mp4" controls="controls"></video>

以下是源码:

[魔杖播放视频](https://create.codelab.club/projects/8499/)

<!--
[Scratch-魔杖播放视频](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-wand-player2.sb3)
-->

!!!提醒
    windows 10 的用户可能会遇到如下问题: 每次打开的都是文档文件夹。原因可能是中文编码问题。 解决方案:确保文件路径没有中文（建议放在D盘根目录下）诸如: `PyHelper.open(r'D:\cozmo.mp4')`

!!!改进
    如果你的播放器不直接弹出到桌面（诸如window10，默认显示在页脚），可以考虑使用网页打开视频: PyHelper.open_url(video_url), video_url 是这个视频的 url 地址


## 高阶用法
HCI 插件允许你写 Python 代码，[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/index.html) 文档中的所有功能你都可以在 Scratch 中使用。

!!! tips
    如果你想使用HCI接管游戏，要注意`press`是瞬间行为（一般无效），一般游戏是在大循环中检测的你是否按下某个按键，所以建议按下一段时间（使用keyDown和keyUp，中间间隔一会儿。）