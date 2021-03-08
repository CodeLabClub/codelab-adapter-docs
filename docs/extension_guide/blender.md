# Tutorial
系统依赖参考 [EIM 教程](/extension_guide/eim/)。

### 安装依赖

我的环境是：`MacOS blender 2.92`

<!--
```bash
cd /Applications/blender.app/Contents/Resources/2.80/python/bin
wget https://bootstrap.pypa.io/get-pip.py
./python3.7m ./get-pip.py --prefix /Applications/blender.app/Contents/Resources/2.80/python
./python3.7m pip3 install codelab_adapter_client --upgrade
```
-->

```bash
/Applications/Blender.app/Contents/Resources/2.92/python/bin/python3.7m -m pip install codelab_adapter_client --upgrade
```

### 在 blender 中运行 [node_blender](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_blender.py)

<!--
在 blender 中运行 [node_blender.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_blender.py)，我们在 blender 2.79 和 2.80 两个版本中都做了测试。

在 blender 2.79b 中， 打开`Text Editor`，运行 [node_blender.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_blender.py)：

![](/img/codelab-blender_7d110f45.png)
-->

打开 `Scripting` 标签页，运行 [node_blender.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_blender.py)：

!!!提醒
    如果你希望看到调试信息(log)  
    在命令行里启动blender， `/Applications/blender.app/Contents/MacOS/blender` （MacOS）


![](/img/codelab-blender_d397ea81.png)

<!--
###  运行  CodeLab Adapter (作为消息中心)

<img width="300px" src="../../img/v2/adapter_scratch_style_ui.png"/>
-->

### 开始使用

打开 [CodeLab Scratch3](https://scratch-beta.codelab.club/)，开始使用。

<video width=600px src="/video/blender.mp4" controls="controls"></video>

如果遇到问题，请尝试刷新浏览器缓存。

#### Demo
[Scratch blender](https://scratch-beta.codelab.club?sb3url=https://adapter.codelab.club/sb3/Scratch-blender.sb3)


# todo

将 [node_blender](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_blender.py) (v2)写成  blender 插件。

# FAQ
### bpy hello world
```py
# 切入blender scripting 面板
bpy.data.objects["Cube"].location.x += 0.5
```

<!--
### 与pharo结合
```bash
# /Applications/Blender.app/Contents/Resources/2.92/python/bin/python3.7m
```
-->

### 基于 OSC 的通信

你也可以使用 Scratch OSC 插件(需要开启Adapter) 与 Blender 通信(需要安装[AddRoutes](http://www.jpfep.net/pages/addroutes/)(在blender 2.92中可用))。


![](/img/be016baa10d3ef1239067f5f8ebff915.png)
