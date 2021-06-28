# 物理引擎
## 介绍
物理引擎扩展是基于 [Box2D](https://box2d.org/) 开发的用于模拟物理规则的游戏引擎，使用它可以很方便地模拟重力、物体间的碰撞，制作游戏变得更加简单。先体验[吃货大冒险](https://create.codelab.club/projects/10726/)项目来看看物理引擎的效果吧。
![](/img/PE_Example.png)

## Hello World
接下来我们使用物理引擎扩展制作一个角色能够跳跃和移动的项目。

### 1. 加载物理引擎扩展

从扩展库中选择“物理引擎”扩展，也可以直接通过搜索框搜索扩展。
![](/img/PE_Extension.png)
### 2. 让角色跳起来

拼接下图中的积木，当按下上键，小猫竖直方向上的速度会变成 15，小猫向上移动，由于物理引擎会模拟重力效果，小猫最终会落回地面，这样就制作了跳跃的功能。在开始的时候需要设置角色的形状，如果想让物理引擎起作用，“逐步模拟”积木需要一直运行。
![](/img/PE_jump.png)
### 3. 让角色移动

现在，小猫可以跳跃了，添加以下积木就可以让小猫左右移动，同时按上键和右键，小猫会向前方跳跃。
![](/img/PE_move.png)
添加一个新角色 Paddle，设置它的形状并且让它固定住，现在它也拥有了物理属性，小猫可以跳到平板上。注意，小猫角色已经添加了“逐步模拟”积木，平板角色不需要重复添加。完整程序见[【物理引擎】跳跃和移动](https://create.codelab.club/projects/12707/editor/)项目。
![](/img/PE_paddle.png)

## 积木说明
物理引擎积木的介绍请参考项目[【物理引擎】积木介绍](https://create.codelab.club/projects/13039/editor/)，里面有逐个积木的介绍和相应的示例。
![](/img/PE_blocks.png)

## 拓展
### 更多项目
[CodeLab 社区](https://create.codelab.club/explore/projects/all?extension=griffpatch)有很多物理引擎相关的项目，这里列出部分项目：

- [【物理引擎】教程](https://create.codelab.club/studios/435)
- [鼠标的吸引力3](https://create.codelab.club/projects/11212/)
- [Floating Bubbles remix remix](https://create.codelab.club/projects/11058/)
- [弹射: 小猫吃西瓜 v0.9](https://create.codelab.club/projects/10032/)
- [桌球](https://create.codelab.club/projects/11429/)
- [合成大西瓜1.2](https://create.codelab.club/projects/9151/)
- [[Box2D] 风火轮](https://create.codelab.club/projects/9985/)

### FAQ
**1. 物理引擎不起作用**

可能是以下原因：

- “逐步模拟”积木没有一直运行
- 没有设置角色的形状
- 角色隐藏起来了

如果有更多物理引擎相关的问题或想法，欢迎在 [CodeLab 论坛](https://discuss.codelab.club/)交流讨论。