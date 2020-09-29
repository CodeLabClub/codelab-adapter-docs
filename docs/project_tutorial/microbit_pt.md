# Micro:bit Radio 与 Adapter

在[*入门案例2*](../get_start/gs_microbit.md)中，我们通过 *Micro:bit 插件* ， 在 *Scratch* 中对 *Micro:bit* 编程，但如果要充分使用 **Micro:bit生态** 的能力， 一块 *Micro:bit* 无法满足我们表达想法的需求。比如在 [Fire!:投石器](https://codelab-adapter-docs.codelab.club/video/wand_catapult_demo.mp4) 项目中我们用到了 **三块Micro:bit**。

而 **Micro:bit Radio 插件** 可以连接多块 *Micro:bit* ，并将 **Scratch** 和 **Python语言** 的能力结合到 **Micro:bit** 中。

## 教程目的

---

在本篇教程中，我们将使用 *Adapter* 的 **Micro:bit Radio 插件** 连接两块 *Micro:bit*，其中一个为 **消息中转板** ，另一个为 **功能板** 。通过实现 无线控制小猫的案例，展示 **Micro:bit 生态** 与 **Scratch** 的连接。

## 原理解释

---

在案例开始前，我们先介绍一些基本知识，以便了解 **Micro:bit生态** 能做什么，以及 **Micro:bit Radio** 插件的工作方式。

### Micro:bit 生态能做什么

在[入门案例2](../get_start/gs_microbit.md)中， 我们简单介绍了 *Micro:bit* 是什么？

[那 Micro:bit 生态 能做什么呢？](https://www.microbitgo.com/info/id/183/time/1552289945)，链接中的视频，向我们展示了 *Micro:bit* 能为我们按下快门，为小花浇水等一大堆有趣的事情。

不熟悉 *Micro:bit* 的小伙伴，我们推荐[micro:bit 官方社区](https://microbit.org/get-started/user-guide/overview/)和[中文社区](https://www.microbitgo.com/index)，社区里有丰富的教程与案例，供大家参考。

### Micro:bit Radio 插件

*Micro:bit Radio* 使用了 *Micro:bit* 内置的无线通信模块，使得多块 *Micro:bit* 可以互相通信。

这需要 **一块 *Micro:bit* 作为 *消息中转站*** ， *Micro:bit 消息中转站* (简称 *中转站* ）需要用USB线与计算机相连， 而其他 *Micro:bit* 作为 **功能板** 就通过 **中转站** 与计算机进行连接。

再建立以上连接之后，我们就可以通过 *Scratch* 对 **功能板 Micro:bit** (简称 *功能板* ）进行编程，比如用 **功能板** 控制小猫的移动。

小伙伴可能会问：
> “我一块 *Micro:bit* 也能控制小猫的移动呀，为什么要用两块呢？”

在这里，只是想用一个简单的案例，说明多个 *Micro:bit* 连接的方式，为连接多个 *Micro:bit* 提供一个案例，以便我们利用多个 *Micro:bit* 表达我们的想法。

## 案例：无线控制小猫移动

---

### 第一步：为 Micro:bit功能板 编程

用USB线，将 *功能板* 连入计算机中

首先我们先在 *makecode* 中为 *Micro:bit功能板*

- 定义向 *Micro:bit中转站* 发送消息的按键
    映射 按钮 “A” 和 “B” 分别发送字符串“a” 和 “b” 到中转站。
- 定义收到 *Micro:bit中转站* 消息的行为
    即当 *功能板* 收到字符 “c” 时，显示爱心

    ![mb_funboard](/img/microbit_funboard_code.png)

我们将这 [*功能板 makecode代码*](https://makecode.microbit.org/11509-28026-09943-34050) （文件后缀名为.hex)下载到计算机本地文件中，并拖入到 Micro:bit 文件夹中，完成代码的导入。

### 第二步：为 Micro:bit中转站 编程

在 *makecode* 为 *中转站* 编程

- 定义向 *Adapter* 收发消息的功能
- 定义向 *Micro:bit功能板* 收发消息的功能 <!-- 代码需要加上功能注释-->

    ![mb_mid_board](/img/microbit_midboard_code.png)

和第一步一样，下载 [*消息中转站 makecode代码*](https://makecode.microbit.org/_Fx5Aif6Fv17d)，并烧入中转站。

以上的代码，看不懂是没关系的，只要我们知道相应的模块是做什么的就好了。

眼尖的小伙伴发现，上述步骤的关键，在于将 *中转站* 和 *功能板* 置于同一个 **无线设置组** 。使得它们彼此之间可以相互通信交流。

### 第三步：Scratch 环境初始化

完成上述两步后，我们保持 *中转站* 与 *计算机* 的连接。并为 *功能板* 持续供电。

比如像这样的

![microbit_battery](/img/microbit_battery.png)

1. 打开 *Adapter*
2. 在 *Scratch* 中启用 *Micro:bit插件*

ps：对这部分不熟悉的同学，请回看[入门案例：microbit](../get_start/gs_microbit.md)

### 第四步：在 Scratch 中为功能板编程

经过前三步，我们已经为两块 *Micro:bit* 和 *Scratch* 建立起连接。

现在， **我们要在 *Scratch* 中为 *功能板* 定义行为，用 *A* 和 *B* 按键来控制小猫的移动。**

*Scratch* 代码如图所示：

![microbit_Scratch_code](/img/microbit_scratch_code.png)

[Micro:bit Radio项目](https://scratch3v3.codelab.club/?sb3url=https://adapter.codelab.club/sb3/microbit_radio_code.sb3)

点击绿旗，再按下 *功能板* 的按键，小猫是不是如你所愿地前进和后退了呢？

在 **Scratch中** 点击发送字符 “c” 的积木块，我们就可以在 *功能板* 上看到一个爱心了。

### 消息流动的过程

在这个案例中，一共涉及了 **三个对象** 在沟通和交流。**Scratch，Micro:bit中转站 和 Micro:bit功能板** 。

对象之间的消息传递如下图所示：

![对象消息图](/img/microbit_radio_messageflow.png)

## 启发与想象力

---

通过这个案例，我们可以看到， **Adapter 可以将不同的对象连接起来，让不同对象可以彼此交互， 不仅仅是单一 *Micro:bit* 可以与 *Scratch* 进行交互，而且是整个 *Micro:bit* 生态** 。

通过修改 *功能板* 的 *makecode代码*，以及 *Scratch中的代码*

- 我们可以使用 *Micro:bit* 更多的传感器来触发 **我们想要发送的消息** 。

    比如人和人之间表示友好，不仅可以通过言语问候，也可以通过握手。

- 我们可以定义 *Micro:bit* 接收到特定的消息时，所作出的反应。

    如果配合 *Micro:bit* 各种功能各异的扩展板，也许我们就可以构建出一个属于自己的计算机实体乐园了。

以上可能还不能满足一些好奇小伙伴的野心：
> 我能用其他对象（比如Python对象）去和 *Micro:bit 生态* 进行交互吗？这样我就可以让 Micro:bit 获得更多可自定义的行为了。

当然可以啦！接下来我们将用 *Scratch PPT* 的例子，展示 **Python对象，Scratch对象 和 Micro:bit** 的交流协作，去制作一个属于自己的独特 *Power Point* 工具。
