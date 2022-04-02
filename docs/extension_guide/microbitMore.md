# Tutorial
在 Scratch 中释放 microbit v2 的更多潜力:  可以在Scratch中使用 micro:bit V2 所具备的所有传感器和输出功能。

!!! 提醒
    在 Chrome 浏览器中使用。  
    同时支持 USB 和 蓝牙 两种模式。默认使用蓝牙连接。 连接时，按住 `shift`，可选择USB连接方式。  
    如果你的浏览器不支持 web 蓝牙，又想使用无线连接，则需要安装 Scratch link。  
    Linux 用户，在 `chrome://flags` 中启用 `# experimental-web-platform-features`

![](/img/7909117426fc267dbb28c104bfc140bb.png)


# 刷入固件

点击 **刷入固件** 积木手动往 microbit 里刷入[固件](/hex/microbit-pxt-mbit-v23-compass.hex), 也可以使用 Scratch 里的 **刷入固件** 积木，自动刷入。

!!!提醒
    如果你需要在makecode里扩展新的能力（通过Scratch的`发送:标签`调用自定义的功能）。 请使用[这个固件](/hex/microbit-mbit-more-v2-0_2_3.hex)

# 初始化
刷入固件后，需要初始化。 LED 屏幕上会显示  **TILT to FILL SCREEN** (耐心等待播放完)。之后将 micro:bit 前后左右倾斜，直到所有 LED 都处于亮起状态， 完成之后，开始连接。

# FAQ
## 两个 microbit 通信
目前请使用 [micro:bit radio](https://adapter.codelab.club/extension_guide/microbit_radio/)

## 文档
参考 [docs](https://microbit-more.github.io/docs)