# Tutorial

该文档由 [@Hanson 同学](http://www.concentric-circle.com/author/admin/) 创建。

## 介绍

Box2D 是一个被广泛使用的 2D C++物理引擎，Codelab Scratch 中的 Box2D 插件基于 Javascript 构建。

不依赖于 CodeLab Adapter。

# 步骤 1 在 Codelab Scratch 中导入 Box2D 插件

![](/img/scratch-box2d-extension.png)

# 步骤 2 创建一个 Box2D 世界

创建一个世界之后才能模拟物理。

![](/img/box2d-step2.png)

使用 setup stage 模块在舞台上创建一个世界。它有 3 种样式：

1.  Boxed stage：有地板、墙和天花板的世界。墙和地板分别是舞台的下、左右边框，而天花板在舞台的 y=940 的高度。
2.  Open(with floor)：只有地板的世界。
3.  Open(no floor)：啥也没有的世界，但它还是一个世界。

之后可以选择设置重力中心（set gravity to），可以想象那里有一个质量无限大的物体吸引着其他物体。也可以不设置，默认在舞台下方。

# 步骤 3 使角色加入到物理世界

只有被加入到物理世界他才会被物理法则所影响。

![](/img/box2d-step3.png)

模块：Enable for**_mode_**

参数 1 影响的对象：

1.  This costume 这个角色
2.  This circle 角色的外接圆
3.  This polygon 并不知道是什么意思，因为不会使用
4.  All sprites 所有角色

参数 2 模式：

1.  Normal 普通
2.  Precision 精确

# 步骤 4 重复模拟

使用一个循环，其中有模块 step simulate 来重复模拟。

完成！

至此，最基础的架构世界已经完成了。你现在可以使用运动模块等来让角色动起来。这些模块很好理解，只需要在架构好的世界里尝试一次就知道了。

注意：你的角色的质量会因大小而改变。你可以设置密度来影响它。

其它模块解释:

-   Push with force**_in direction_** 向某个方向施加一定大小的力。有惯性的影响。
    注意：你的角色的质量会因大小而改变。你可以设置密度来影响它。

-   Spin with force \_\_\_ 顺时针旋转角色。参数为力量大小，有方向。同样受到惯性的影响。

-   Set density**_ roughness_** 设置密度和光滑程度。不知为何这里采用的是形容词来确定五种程度。

-   Set fixed\_\_\_ 设置固定。

-   Touching any/feet 碰撞判断，参数为整个身体/脚。

-   Scroll 指的是舞台的滚动，舞台、重力中心和所有角色都会滚动。

# 异常

当你的程序中出现了问题时，它并不会崩溃。现象就是你无法点击小绿旗来启动这个程序。此时你需要做的是检查程序，或是试着移除部分程序以确定哪里出现了问题。

# 已知问题

当使角色加入物理世界时模块 Enable for**_mode_**参数为 this polygon 时会出现未知问题

# demo
*  [box2d 练习](https://create.codelab.club/projects/9961/)
*  [重量称量(多物体交互demo)](https://create.codelab.club/projects/9968/)