# 制作一个多功能 Scratch PPT

经过前两个教程，我们已经将 Scratch 创作表达的环境延伸到了 **计算机系统** 以及 **Micro:bit 生态**。

可别忘了， **Adapter 可以 *连接多个对象* ，并让 对象们 彼此沟通，由此构成一个 *可理解* 和 *可扩展* 的编程环境** 。

**我们作为创作主体，在这个编程环境中，自由地表达我们的想法，让想象成为可能。**

现在，我们开始进入由多个对象构成的创作环境中编程。

## 案例思考

---

我们知道， *Scratch* 可以制作 *PPT（幻灯片）* 。美中不足的是，这个 *PPT* 缺乏一些可扩展的功能比如：

- 打开计算机本地的视频
- *PPT* 换页只能依靠点击鼠标
- 。。。

而在之前的案例中，我们尝试

- 使用 *Ptyhon对象* 获得了 *计算机操作系统* 的信息
- 使用 *无线Micro:bit* 去控制 *Scratch小猫* 移动。

**咦！这不恰好可以用之前尝试过的案例用于改进 Scratch PPT 了吗？**

## 案例：改进一个 Scratch PPT

---

在这里我们尝试在已有的 [*Codelab演讲PPT*](https://scratch3v3.codelab.club/?sb3url=https://adapter.codelab.club/sb3/codelab_ppt_base.sb3)(点击链接，打开项目) 上进行改进，为其添加以下功能

- *无线Micro:bit* 作为翻页笔
- 可以打开任意网站视频（以 Codelab官网 为例）

### PPT 源码

![help_tool_code](/img/sppt_htool.png)

在 *help_tool角色* 中代码定义了 **翻页功能** ，以及 **打开本地文件** 和 **打开网页链接** 的自定义积木。（见图注）

值得一提的是：

> 这里引入 *Python对象* 能力的方式与 [*Eim插件教程*](./eim_pt.md) 不一样，用到的是 *Python插件* 。在 [*入门教程1*](../get_start/gs_pyproject.md)中有示例如何使用。

这里简单解释一下插件工作的原理，在 [*Python插件*](https://adapter.codelab.club/extension_guide/extension_python_kernel/) 代码文件中，定义了 `PyHelper类` ，在该类中定义了用于打开连接的 `open_url 方法` 。Scratch积木块通过广播一条 *代码语句* ：`PyHelper.open_url(url)` 给 *Python对象* ，然后 *Python对象* 就会执行这段代码，打开相应的链接了。

!!! 提醒
    PyHelper类中还有一个方法很实用: `open`, 这个方法以系统默认的方式打开任何东西: 诸如文本、图片、视频、软件...只要传入想打开的东西的 **绝对系统路径** 即可。诸如打开Chrome浏览器: `PyHelper.open("C:\Program Files\Google\Chrome\Application\chrome.exe")`

![pyboardcast](/img/sppt_pyboardcast.png) *python广播积木*

ps： *python插件* 和 *eim插件* 的区别需要小伙伴先具备一些Python语言知识，我们将会在插件开发手册中详细解释两者的具体区别。

另外两个角色的代码定义了一个翻页动画，我们将会在动画结束后，利用自定义积木自动弹出 Codelab 的介绍视频。

### 无线 Microbit 作为翻页笔

---

#### 第一步：准备两块 *Micro:bit*

我们按照上一篇教程：[*Micro:bit Raio*](./microbit_pt.md)，在 *madecode* 中定义好 *功能板* 和 *中转板* 的行为。让我们可以在 Scratch中使用 *功能板* 的 *A键* （左上方按钮） 和 *B键* （右上方按钮）。

#### 第二步：绑定翻页功能

我们将 *功能板* 的 *A键* 绑定到 **向前翻页** ，*B键* 绑定到 **向后翻页** 。

![ab_button](/img/sppt_abbuttou.png)

现在尝试按下 *Micro:bit 功能板* 的 *A / B 键* ， PPT 开始翻页了！

### 翻页动画打开 Codelab官网

---

当翻页到 Codelab 标志时，会有一个动画介绍 Codelab 概况。

![codelab_animation](/img/sppt_anmiation.gif)

现在，我们在动画结束后，自动转到介绍 *Codelab视频* 中。

我们先来看看 *角色introduction* 的代码

![introduction](/img/sppt_introduction.png)

在这个角色收到 `show_codelab_introduction` 的消息时，开始出场动画，然后 *Codelab介绍信息* 就显示出来了。

那么要在动画结束打开一个网页，就非常简单了，我们只需要

1. 在 **introduction角色** 中自定义 `open_url` 积木
2. 使用 `open_url` 积木

代码如下：

![improvement](/img/sppt_openUrl.png)

现在尝试一下，是否能在翻页动画结束后，自动转到 *Codelab官网* 呢？

[完整项目代码](https://scratch3v3.codelab.club/?sb3url=https://adapter.codelab.club/sb3/codelab_ppt_improved.sb3)

## 启发与想象力

---

增强 *Scratch PPT* 的例子就此完结了，不知道大家有没有发现，在 *Adapter* 的帮助下， **我们很容易实现不同对象之间的交互**

- 在 *Micro:bit Radio项目* 的基础上，无需对Micro:Bit 做任何硬编码（即使用makecode去定义按键的具体功能）， 通过两个积木块，就可以赋予 Micro:Bit 翻页笔的功能
- 将 Python对象打开网址的能力， 即刻赋予给翻页动画

**根据消息的沟通随时绑定对象** ，正是 Adapter 的最核心特性。

前面提到的 **对象可以根据自己的需要去响应来自其他的对象的消息** 在这里得以体现，如果我不想用 *Micro:bit* 翻页，换成眼动仪，也就是拖动两个积木块的事情。这时候， *Micro:bit* 就可以去控制其他东西了，在 *Neverland* 中可以是 窗帘的升降 或是 灯光的亮灭 或是。。。现实已经不会成为你想象力的天花板了。

## 项目教程结语

---

到此为止，项目教程向大家展示了

- **Adapter 的核心概念：对象 和 消息**
- Adapter 的基本使用方法
- Adapter 的核心特性

核心特性包括

- 灵活地连接各种实体硬件生态（如 Micro:bit)
- 拓展 Scratch 使用 *计算机操作系统* 的能力
- 不同对象之间的可以灵活地绑定

**最重要的是，我们的想法可以在 Adapter 创建出的丰富可编程环境中任意表达了**

接下来就是发挥大家想象力的时候了，非常欢迎大家继续跟随 Adapter文档 去探索更多编程的可能性！
