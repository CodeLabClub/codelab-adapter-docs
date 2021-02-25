# Python对象的连接器：EIM 插件

好事多磨，经过[对象和消息](object_illustrate.md)的介绍我们终于来到第一个项目案例： EIM。

## 教程目的

---
我们将使用 **EIM 插件** 去获得 **操作系统** 的信息。其中涉及 *Python* 代码编辑器：*Jupyterlab* 的操作。

你可能会感到头大，什么是 **EIM**，什么又是 **操作系统**？莫头疼，让我们一一细看。

我们非常鼓励 **打开浏览器去搜索你不懂的词汇** ，比如操作系统。

## 概念解释

---

### 操作系统

什么是操作系统呢？维基百科的定义如下

> 操作系统（英语：Operating System，缩写：OS）是一组主管并控制计算机操作、运用和运行硬件、软件资源和提供公共服务来组织用户交互的相互关联的系统软件程序，同时也是计算机系统的内核与基石。 ——维基百科

这个定义很复杂，牵扯到计算机硬件，软件，以及编程等话题。我们在这里不详细展开。

在直观的认识中，我们使用的 *Windows*， *macOS* 和 *Unix类系统* 等就是 **操作系统**，我们可以在 *Windows* 上运行浏览器进行 *Scratch* 编程，也可以在上面运行 *腾讯QQ* 等通讯软件和朋友聊天，少不了的是我们可以玩各种各样的电子游戏，可以做的事情还有很多。。。

<!--在这里，我们有上述直观的了解就可以往下尝试了，虽然我们希望在接下来的日子里，大家可以根据自己的兴趣，去学习这一部分的知识。-->
到此为止，我们有上述直观的了解就够了，而 Python 这门编程语言就可以扩展我们和操作系统交互的能力。做一些除了玩游戏以外的事情。比如做一款属于自己的游戏，搭建一个属于自己的网页。

### EIM 插件

在 Adapter 中， *EIM* 是 *Everything Is a Message* 缩写，即 **对象之间流动的一切皆消息**。

在Adapter所连接的 *对象* 之间，流动的就是 *消息*，而不同的 *对象* 可以各自根据 *消息* 做出不同的反应。

*EIM插件* 的作用是： **在Adapter中传递 *Scratch对象* 和 *Python对象* 之间的消息**。

你可能一下就反应过来了，这里的消息不就类似于小猫和小熊间的对话吗？只是 **小猫** 和 **小熊** 变成了 **Scratch对象** 和 **Python对象** 而已。Adatper 只不过是让这个“对话”在不同层面的对象之间得以发生，

> *就像声音的传播需要空气一样，Scratch 和 Python 之间的消息传递需要 Adapter插件：EIM*

（除了由衷对你聪明的赞许，我无话可说 :)）

![eim_mr](/img/eim_mrpg.png)
*^消息流动示意图^*

## 案例：获取操作系统信息

---

现在 **我们尝试使用 *Python* 获取计算机操作系统的信息，然后通过 *Adapter* 发送到 *Scratch* 中，让小猫说出来。** 以此为例扩展Scratch的能力，尝试触达计算机操作系统中的信息。

有的小伙伴又有疑问了：

> 我没有学过 *Python* 怎么办？

莫慌，这里涉及的代码非常简单，并且提供的是一个模板，容许你稍加修改就可以达到你想要的效果，在这个过程中，更需要的是你的想象力。

<!--需要在案例结束的时候提及消息的流动是单向的，并且鼓励读者尝试不同方向的消息流动，举个例子作为提示-->

### 第一步：编写 Python 代码

*Jupyterlab* 是一个写 *Python* 代码的环境，我们在上面修改和运行代码。

1. 打开 *Codelab Adapter* （不记得如何打开的同学请回看[安装Adapter](../get_start/gs_install.md)）。

2. 编写 Python 代码
    我们将以下代码复制到一个 *Python Notebook* 中并运行他们。请注意阅读代码中的注释，帮助我们了解代码在干什么。

    ```python
    # “#”井号后面是注释，不作为代码运行
    from codelab_adapter_client import run_monitor, send_message  # adapter >= 4.3.0 or codelab-adapter-client >= 4.1.3
    # from codelab_adapter_client.utils import run_monitor, send_simple_message
    import platform
    # 上面两句代码的意思是导入代码运行需要的依赖

    def monitor(msg): # 这里定义了一个函数，参数 msg 是 Scratch 中发送过来的消息，就是 Scratch 和 Python对象 说的话。
        print(msg)
        return "我的操作系统是：" + str(platform.platform()) # 定义了返回给Scratch的系统信息，就是 Python对象 要对Scratch 说的话。

    # send_simple_message("hello")
    run_monitor(monitor) # 发送消息给Scratch
    ```

    ![run_jupyter](/img/run_jupyter.gif)

    ps：Linux用户，在第一次打开 *Jupyter* 插件时，会帮你自动下载并打开，操作不如上图也没关系，请给点耐心。

### 第二步：在 Scratch 中编程

完成第一步操作后，我们在 *Scratch* 中，使用积木向 *Python对象* 发消息，和接收来自 *Python对象* 的消息。

所用到的积木块

- ![block_eim_broadcast](/img/block_eim_broadcast.png) 广播消息积木
- ![block_eim_recieve](/img/block_eim_recieve.png) 收消息积木

1. 在 *Scratch* 中启动EIM扩展

    ![eim](/img/run_eim.gif)

2. 发送和接收消息
    我们在广播消息积木中输入发送给 *Python对象* 的消息：“ **我的操作系统是什么** ？”

    随后让小猫说出获取的 *操作系统信息* 。演示用到的系统为 *Linux系统* 。
    ![msg](/img/run_msg.gif)

    现在回到 *Jupyterlab* 中，我们可以看到，从下方的红框显示了 *Scratch对象* 发送过来的消息。

    ![msg_from_Scratch](/img/jupyter_recieve.png)

如果我们修改了上述代码，需要重新运行Python程序，点击红框中的 *方块* ，再点击 *运行箭头*，就可以了。若实在不行，刷新一下页面，重新运行程序。

### 原理解释

运行 *Python* 程序后，我们启动了 *Python对象*，*Python对象* 会持续地接收来自 *Scratch对象* 发送过来的消息。通过 `run_monitor(monitor)` 函数，我们将处理后的消息返回到 *Scratch对象* 中。我们可以看到，在这里 **Python对象** 其实就是一个 **Python程序**

## 启发与想象力

在上述的教程中，我们观察到了， *Scratch对象* 是如何与 *Python对象* 进行沟通的.

![msg_flow](/img/eim_msg_flow.png)

这样一来， **我们就可以利用Python语言的能力，去处理来自 *Scratch* 的消息，并返回到Scratch中。**

那么，我们还可以用到 *Python语言* 的哪些能力去处理 *Scratch* 的消息呢？比如：

- 在 *Python对象* 中使用AI自然语言处理，去理解小猫说的话，制作一个自动回复的机器人。[聊天机器人项目](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-tuling-chatbot.sb3)
- 在 *Python对象* 中使用图像识别，让小猫去理解摄像头的事物是什么？[图像识别项目](../extension_guide/EasyOCR.md)
- 比如。。。
