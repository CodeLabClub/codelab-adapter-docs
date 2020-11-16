# Etoys

## 介绍

![](/img/etoys-doThings.gif)

[Etoys](http://www.squeakland.org/) 是:

-   一种教育工具，向孩子们传授强大的思想(powerful ideas)
-   丰富的媒体创作环境和可视化编程系统
-   开放系统，几乎适用于所有个人电脑

Etoys 的开发始于迪斯尼，由艾伦·凯（Alan Kay）主导，受 Seymour Papert 的 Logo 语言影响，支持建构主义学习。

开发团队包括：Scott Wallace、Ted Kaehler、John Maloney 和 Dan Ingalls。

极大影响了 Scratch（John Maloney 是 Scratch 的首席架构师）

## 截图

![](/img/f5f4e17f5bf372c1ca4dd9852572320d.png)

![](/img/cd173ca2506612af447252da4d0ecb93.png)

## 接入 Adapter

Etoys 的最后一次更新是 2012 年（5.0 版本）。

我们试图通过将其接入 Adatper，使其得到 Adapter 连接的整个生态：物联网、AI、开源硬件... 使 Etoys 强大的表达能力与新的技术融合。

### 思路
接入的思路是"hack"。

Etoys与外部通信的方式并不多，在  **百宝箱** 里，仅发现了Scratch客户端，可以与外部通信。

![](/img/61a5c3971e42c1b893896a3819a7eb7b.png)

于是我们通过将 Adapter 伪装成 Scratch 1.3，来与Etoys通信，消息流向是(`Etoys->Adatper->Scratch3.0`)

由于百宝箱里的 Scratch客户端是socket client，所以更复杂的通信也是可能的，但`Etoys->Adatper->Scratch3.0`是我自己的典型使用场景。 更多细节参考: [Etoys 学习笔记: 与 Scratch 互操作](https://blog.just4fun.site/post/%E5%B0%91%E5%84%BF%E7%BC%96%E7%A8%8B/etoys-learning-note/). 

也欢迎你自己进行hack ：）

### 使用
使用方式很简单，在Adapter 中开启 `extension_socket_server` 插件（如果不存在该插件，到[插件市场](https://adapter.codelab.club/extension_guide/extension_market/)下载即可），源码在[extension_socket_server.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_socket_server.py)

开启插件后，加载demo程序，并点击绿旗运行它。

[Scratch-Etoys](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-etoys.sb3)

之后在 Etoys 里使用 broadcask 积木 即可：

![](/img/3f30f15d9232524bfea6b571f3ccf993.png)

!!! 提醒
    在使用具体积木时，需要先建立连接，点击 Etoys里Scratch客户端即可，如果连接顺利，猫的眼睛会睁开。

以下是一个简单的例子：

![](/img/253ca954118ccc71d8a15a801eb23efa.png)

使用Etoys里的按钮打开本地目录和CodeLab主页，背后利用到了 Adapter Python Extension的能力:

<video width=80% src="/video/1605187287307932.mp4#t=0.001" controls="controls"></video>

一切都是消息！

## Etoys 与 Scratch 对比
Scratch适合入门，它通过给定清晰的结构，提供更多确定性，让入门变得容易（不必担心搞乱环境）。

随着项目变得更复杂，Etoys是更理想的选择，因其拥有继承自Smalltalk的强大环境和表达能力，惊人的一致性，彻底的面向对象，随着项目逐渐生长，复杂度总是在可控的范围内(因为消息-对象隐喻）。

随着项目变得复杂，Scratch用户需要掌握越来越多的“技巧”，编程成为一件搜罗和记忆许多技巧（特例）的乏味工作（就像传统计算机教育），环境无法提供更多的支持。

Etoys/Squeak 为“Scratch下一步是什么？”提供了理想的答案: `Scratch -> Etoys -> Squeak(Smalltalk)`

## 教育者
Alan Kay 和 Etoys社区围绕Etoys写了许多精彩的文章，推荐阅读。也许是有史以来关于向孩子传授 powerful ideas 最精彩的文章之一。

诸如:

*  [Squeak Etoys Authoring & Media](http://www.squeakland.org/content/articles/attach/etoys_n_authoring.pdf)
*  [Kedama: A GUI-based Interactive Massively Parallel Particle Programming System](http://www.vpri.org/pdf/tr2005001_ohshima_kedama.pdf)

更多文章可以从[Etoy resources](http://www.squeakland.org/resources/articles/) 和 [Viewpoints Research Institute](http://www.vpri.org/)里找


## 进阶
你可以参考[Etoys 学习笔记: 与 Scratch 互操作](https://blog.just4fun.site/post/%E5%B0%91%E5%84%BF%E7%BC%96%E7%A8%8B/etoys-learning-note/)自行构建功能更丰富的Server，使用 [Adapter Node](https://adapter.codelab.club/dev_guide/Adapter-Node/) 将其接入Adapter生态。

## 参考

-   [Etoys 学习笔记: 与 Scratch 互操作](https://blog.just4fun.site/post/%E5%B0%91%E5%84%BF%E7%BC%96%E7%A8%8B/etoys-learning-note/)
