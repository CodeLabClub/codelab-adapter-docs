# Tutorial

![](/img/44fe13429c50c93fcef527360c1ae6ac.png)

# 插件说明

-   使用方式: 到[插件市场](/extension_guide/extension_market/)下载插件, 搜索 **sonicPi**
-   插件类型: [Adapter Node](https://adapter.codelab.club/dev_guide/Adapter-Node/)
-   插件源码: [node_sonicPi.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_sonicPi.py)
-   依赖库(python):  `python -m pip install codelab_adapter_client python-sonic`

# 外部环境依赖

需要下载[Sonic Pi](https://sonic-pi.net/)。

# 开始使用

运行 Sonic Pi。

启动 CodeLab Adapter，运行 node_sonicPi 插件。

打开 Scratch 编程界面，我们已经制作了一个 demo:[Scratch-SonicPi](https://scratch-beta.codelab.club?sb3url=https://adapter.codelab.club/sb3/Scratch-SonicPi.sb3)。

<video src="/video/1588741044537372.mp4" controls="controls"></video>


# 进阶

更多可用的指令，参考[python-sonic](https://github.com/gkvoelkl/python-sonic)。

如果你想深入了解[Sonic Pi](https://sonic-pi.net/)，可以跟着 Sonic Pi 软件内置的文档学习。

## 发送消息
`>= 3.7.2` 的 Adapter 支持使用Scratch积木发送OSC消息，消息的参数(args)是一个 list(采用json语法，字符串使用 **双引号** )

## Receiving OSC
[Sonic Pi Receiving OSC](https://sonic-pi.net/tutorial.html#section-12-1)

参考这个文档，你也可以基于[python-sonic](https://python-osc.readthedocs.io/en/latest/client.html#example)构建一个[自定义插件](https://adapter.codelab.club/project_tutorial/eim_pt/#python)直接与Sonic Pi沟通。

# 参考

-   [Sonic Pi](https://sonic-pi.net/)
-   [python-sonic](https://github.com/gkvoelkl/python-sonic)
