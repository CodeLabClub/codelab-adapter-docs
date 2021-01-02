# Tutorial

Hey siri

## 介绍

使用该插件，可将 Siri 接入到 CodeLab Scratch，并与 CodeLab 可编程空间里的一切互动。

### 演示

<video width=80% src="/video/1593431022011083.mp4" controls="controls"></video>

## 插件说明

-   使用方式: 到[插件市场](/extension_guide/extension_market/)下载插件, 搜索 **siri**
-   插件类型: [Adapter Extension](/dev_guide/helloworld/)
-   插件源码: [extension_Siri.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_Siri.py)

## 依赖

{!utils/dependence.md!}


## 步骤 1：打开 Codelab Adapter

{!utils/open_adapter.md!}

## 步骤 2：打开 Codelab Scratch

{!utils/open_scratch.md!}

在 Codelab Scratch 里加载 Siri 插件, 点击绿旗，运行 Adapter Siri 插件。

![](/img/3a2539ceababd25a668c6c7de55c6f63.png)

## 步骤 3：在 iOS(iPhone/iPad)的[快捷指令](https://apps.apple.com/cn/app/%E5%BF%AB%E6%8D%B7%E6%8C%87%E4%BB%A4/id915249334)里自定义指令

确保 iOS 设备和 Adapter 所在设备处在同一个局域网

### `对话模式`(语音输入)指令
!!! 提醒
    建议iOS版本在13以上，不然URL内容获取块可能无法手动输入URL

创建一个`对话模式`指令, 该指令的功能是将 Siri 提示输入(`什么内容`)的内容输入到 CodeLab Scratch

![](/img/IMG_0019.PNG)

使用语音 `Hey siri，对话模式`，将激活刚才自定义的`对话模式`指令

在 Scratch 中接受来自 Siri 的输入内容(`早上好`)

![](/img/996865a70715aa502268139ebe01d3e5.png)

### `控制乐高`(列表选择)指令

对着iOS设备说 `Hey siri，控制乐高`，将激活刚才自定义的`控制乐高`指令

创建一个`控制乐高`指令, 该指令的功能是将 Siri 提示输入(`哪一个`)的内容输入到 CodeLab Scratch

![](/img/IMG_0022.PNG)

在 Scratch 中接受来自 Siri 的输入内容(`顺时针旋转`)

![](/img/5c60c4484b208935f5bf6f3ced9752d1.png)

# 原理说明
*  [CodeLab ❤ Siri](https://www-old.codelab.club/blog/codelab-like-siri/)
