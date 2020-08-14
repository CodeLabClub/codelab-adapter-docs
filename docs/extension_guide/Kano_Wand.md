# Tutorial

## 依赖

{!utils/dependence.md!}

## 步骤 1：Hack Kano Code

尽管社区有很多针对 Kano 设备的硬件和协议破解（Kano 官方也十分具有 hacker 精神，它们分享了很多 hack 技巧），但我偏好破解 kano 的软件(因其十分优秀，希望基于它的 UI 来编程，而通过 hack 增强它的能力)。

Hack [Kano Code](https://kano.me/us/landing/app)，使其与 CodeLab Adapter 兼容。

目前我对 Mac 和 Windows 的[Kano Code](https://kano.me/us/landing/app)做了简单 hack，使其能够接入 Adapter。

!!! tips
    mac系统新版本（13.14之后）安全性提高，如果无法运行hack后的软件(Mac应用已损坏，打不开)，如果可能需要先运行: `sudo spctl --master-disable` 或者  `sudo xattr -rd com.apple.quarantine 空格 软件的路径`
    
## 步骤 2：打开 与 Adapter 兼容的 Kano Code

在 Kano Code 里编程

![](/img/19d2272252efe03397fab32c58032ac0.png)

以上程序的含义是: `当实施图示魔法时，将魔法(id为1)发射到Adapter`。

接下来在 CodeLab Scratch 中对魔法编程（handle）。

## 步骤 3：打开 Codelab Adapter

{!utils/open_adapter.md!}

## 步骤 4：打开 Codelab Scratch3

{!utils/open_scratch.md!}

## 步骤 5：加载 Kano Code 插件

在 Web UI 中点击加载 Kano Code 插件。

开始编程

![](/img/ac8dd3f9aed953ff0926e6b59987b947.png)

以上积木的含义: `当魔法(id为1的魔法)触发时，发出猫叫声`

!!! tips
    建议把 Scratch 页面和 kano 软件并置在桌面。处于后台的浏览器，可能会休眠(有些系统的默认行为)。

## Demo

https://adapter.codelab.club/user_guide/gallery/#kano-wand
