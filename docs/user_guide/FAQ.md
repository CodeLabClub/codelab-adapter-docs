# FAQ

### 与官方的[Scratch Link](https://scratch.mit.edu/microbit)有什么差异？
兼容性方面：

[Scratch Link](https://scratch.mit.edu/microbit)目前有以下依赖:

*  Windows 10 version 1709+
*  macOS 10.13+
*  Bluetooth 4.0

codelab-adapter对平台和操作系统没有这么高的要求，我们支持:

*  window7、window8、window10（32位/64位都支持）
*  macOS大多数版本
*  Ubuntu
*  树莓派
*  其他linux发行版

[Scratch Link](https://scratch.mit.edu/microbit)

在连接能力上，[Scratch Link](https://scratch.mit.edu/microbit)目前只支持BLE，codelab-adapter支持任何的连接:

*  USB
*  WIFI
*  Bluetooth2.0/Bluetooth4.0
*  大多数的协议(mqtt/ZeroMQ/socket...)
*  ...

codelab-adapter killer特性之一是允许普通用户(scratcher)[使用Python拓展Scratch的能力](https://blog.just4fun.site/scratch-adapter-eim-script.html)

codelab-adapter killer特性之二是允许开发者和公司使用Python构建自定义的插件，轻松将任何硬件/AI/IOT设备接入到Scratch3.0中。


Scratch官方计划开源[Scratch Link](https://scratch.mit.edu/microbit)，一旦它们开源，我们将在codelab-adapter通过插件实现Scratch Link的所有功能。

如果你目前要使用以下三种硬件，我们推荐你先使用Scratch Link。未来我们会和官方的功能完全一样。

*  [wedo2.0](https://scratch.mit.edu/wedo)
*  [microbit](https://scratch.mit.edu/microbit)
*  [ev3](https://scratch.mit.edu/ev3)

Scratch Link和codelab-adapter可以协同工作.

codelab-adapter致力于提供更好的跨平台支持和开放的[插件系统](https://github.com/Scratch3Lab/codelab_adapter_extensions)，codelab-adapter的目标是连接万物，不只是连接教育硬件。

### codelab-adapter与[Scratch3 Lab](https://scratch3.codelab.club/)是否连接成功？
codelab-adapter启动之后，可以看到[Scratch3 Lab](https://scratch3.codelab.club/)指示灯显示绿色，代表连接成功

<img alt="" src="../../../img/scratch3-home-connect.png">

### 启动codelab-adapter后，与scratch3无法通信怎么办？
检查下是不是打开了科学上网的软件。

### codelab-adapter可以支持其他平台吗？
codelab-adapter可以支持其他编程平台吗？而不只是在codelab的的平台上使用。

可以的！

codelab-adapter几乎支持任何平台，无论是scratch3.0构建的还是blockly构建的(如Tynker和code.org)的，或者你用其他什么黑魔法构建的，都没问题！

这是目前的接入文档:[codelab-adapter支持第三方平台](https://blog.just4fun.site/scratch3-adapter-open-plan.html)

相关的合作条款我们正在构建中。

期待接入codelab-adapter的公司或组织，欢迎联系我们: `wuwenjie718@gmail.com`

来信请注明公司/组织的一些基本信息，以及你们正在做的事情 ：）

### Python版本
我们在不同操作系统选择的Python版本不同。

*  Ubuntu/Raspbian: 3.5.3
*  Windows/MacOS: 3.6.5

### 如何使用Python拓展Scratch的能力？
参考[使用Python拓展Scratch的能力](https://blog.just4fun.site/scratch-adapter-eim-script.html#_4)

