# Tutorial

<!--思考文档结构-->
![](/img/WechatIMG1431.jpeg)

## 介绍
《我的世界》是一款开放世界游戏，玩家没有具体要完成的目标，并且在游戏内有极高的自由度。

## hello world
### 运行 minecraft

需要配合 [minecraft Pi edition](https://www.minecraft.net/en-us/edition/pi/) 或者 [raspberryjuice](https://dev.bukkit.org/projects/raspberryjuice) 使用。


运行 minecraft，使得 [mcpi](https://github.com/martinohanlon/mcpi) 能够接入minecraft，如果你不是使用树莓派，可能需要调整[插件源码](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_minecraft.py#L30)， 细节参考[mcpi](https://github.com/martinohanlon/mcpi)文档。

### 启动插件
启动 CodeLab Adapter，运行 node_minecraft 插件。

打开 Scratch 编程界面，我们已经制作了一个 demo:[我的世界 mcTurtle DEMO](https://create.codelab.club/projects/10963/editor/)(如果你打开出错，请清理浏览器缓存)， 你可以从这里起步，它是一个运行在Minecraft世界里的Turtle，它会出现在你周围 推荐你飞到空中(空格)去看它的运行轨迹。

<video src="/video/1588665494072465.mp4" controls="controls"></video>

如果你想做更多有趣的事，建议阅读[minecraft](https://www.stuffaboutcode.com/p/minecraft.html), 我们鼓励你去修改[插件源码](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_minecraft.py)，去支持更多的对象。欢迎把你的修改结果提交到 CodeLab 源码仓库，分享给社区里的其他人用


## 积木说明

![](/img/d4c3c008cbb93d6ec60a976d6284f828.png)

<!--todo 自动安装 https://stackoverflow.com/questions/12937533/use-pip-install-uninstall-inside-a-python-script -->


## FAQ
### Adapter 精简版用户(Linux/RPI)
Windows 和 Mac 用户开箱可用。Linux用户将自动安装依赖


##  参考

-   [Minecraft](https://www.stuffaboutcode.com/p/minecraft.html)
-   [Minecraft API](https://www.stuffaboutcode.com/p/minecraft-api-reference.html)
-   [Minecraft Graphics Turtle](https://www.stuffaboutcode.com/2014/05/minecraft-graphics-turtle.html)
-   [Coding shapes in Minecraft](https://www.stuffaboutcode.com/2013/11/coding-shapes-in-minecraft.html)
    -   [Minecraft - Stuff Library](https://minecraft-stuff.readthedocs.io/en/latest/)
-   [TeachCraft](https://github.com/TeachCraft)
-   [https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi](https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi)
-   [Python Coding for Minecraft](https://www.instructables.com/id/Python-coding-for-Minecraft/)
-   [mcpi](https://github.com/martinohanlon/mcpi)
-   [minecraft-python](https://github.com/Macuyiko/minecraft-python)
