# Tutorial

## 依赖

{!utils/dependence.md!}

## 步骤 1：打开 Codelab Adapter

{!utils/open_adapter.md!}

## 步骤 2：打开 Codelab Scratch3

{!utils/open_scratch.md!}

<!--
### 步骤 3：https 检验（只需要验证一次）
如果你是第一次使用 scratch3_adapter，则需要点击 scratch3_adapter 菜单栏中的 `https 检验`

<img width="400px" src="../../img/scratch3-adapter-verify.png"/>

在自动打开的页面里依次点击`高级 > 继续前往 127.0.0.1（不安全）`

<img width="500px" src="../../img/scratch3_adapter_agree.png"/>

完成之后，scratch3_adapter 就可以与 Scratch3 Lab 建立连接了
-->

## 步骤 3：连接设备，加载插件

### 步骤 3.1：为 Arduino UNO 烧入固件：FirmataExpress

安装 [Arduino IDE](https://www.arduino.cc/en/Main/Software)

![](/img/arduino_ide.png)

将 **FirmataExpress** 安装到 IDE 中

打开 Arduino IDE 并选择工具/管理库（Tools/Manage）。当出现库管理器时，在搜索框中输入 **FirmataExpress** ，然后单击安装。

<img src="/img/manage_libraries.png" width=400 />

![](/img/install_firmata_express.png)

安装超声波库：FirmataExpress 还依赖 Erick Simões 的超声库。再次使用 Arduino 库管理器搜索超声波，选择 Erick Simoes 的版本。

![](/img/Ultrasonic.png)

将 FirmataPlus 编译并上传到 Arduino：

选择文件/示例（File/Examples），然后从下拉列表中选择 FirmataExpress。



<img src="/img/select_firmata_express.png" width=500 />

上传到 Arduino。

<img src="/img/compile.png" width=500 />

至此，我们就完成了 Arduino 相关的工作。

### 步骤 3.2：重置 Arduino
每次使用前，按下 Arduino 的重置按钮。

### 步骤 3.3：加载插件
在 CodeLab Adapter 中点击加载 Arduino UNO 插件：

![](/img/4cc77e77a8df89bf1a2a872a259efb46.png)

点击加载插件之后，你应该会看到板子上的 LED 闪烁。如果一切正常，大约 5 秒钟之后（连接时间由 [pymata_express](https://github.com/MrYsLab/pymata-express) 决定），你将看到连接 Arduino UNO 成功的提醒。现在你可以开始在 Scratch 里编程了。

ps: Linux 用户注意，scratch3_adapter 使用 USB 串口与 Arduino 连接，Linux 下，使用 USB 串口需要做权限设置：`sudo chmod 666 /dev/ttyACM0`

## 步骤 4：hello world

现在让我们利用 CodeLab Scratch3 控制 Arduino。

选择对应的 Scratch3 插件：Arduino UNO。

<img width="600px" src="/img/2ee4ea6c32f5612c9a2cf1331d0929dd.png"/>

选择对应拓展积木，点击运行。

<img width="600px" src="/img/3978ac4efbffe08ec9870e31303c18d0.png"/>

!!! 提醒
    引脚在设置具体值之前，不允许读取，否则会出现tx/rx持续轮询被占用(你可以观察到板子上的灯常亮)，这是 [pymata_express](https://github.com/MrYsLab/pymata-express) 的机制决定的。遇到这种情况，请按下重置按钮重新连接。

## 感谢
感谢 mryslab 在硬件驱动上的工作，该插件从他的工作中移植过来。

## 结语

这个例子完整展示了 CodeLab Adapter 的使用流程

- 打开 CodeLab Adapter
- 打开 CodeLab Scratch3
- 接入你的设备（可以是任何开源硬件）
- 打开对应插件
- 选择对应拓展积木，在 Scratch 3.0 中与设备交互

如果你想接入的设备目前没有默认插件支持它（诸如 Arduino 的其他版本：Nano 之类的），你可以自己来写，CodeLab Adapter 允许你将任何硬件接入 Scratch 3.0 中，别害怕，需要的代码很少也很简单，详情参见[开发手册](/dev_guide/helloworld/)。我们支持使用任何编程语言来写拓展，目前我们自己主要使用 Python。

我们也将在 [extension guide](/extension_guide/introduction/) 中介绍各种社区插件的使用方法。
