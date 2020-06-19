# hello world

## 依赖

DynamicTable 依赖于 Adapter 的内置的 `node_physical_blocks` 插件:

![](/img/008977d2d35d02c87bfc64cda9455e1e.png)

为了运行`node_physical_blocks` 插件，你的[本地需要具备 Python 环境](https://adapter.codelab.club/Python_Projects/install_python/)。

第一次运行`node_physical_blocks` 插件，会自动安装依赖: `opencv-contrib-python`, 依赖比较大(`> 60MB`), 耐心等待 1 分钟左右，安装完成会会弹出通知。

!!! 提醒
    如果自动安装没有成功，你可以在命令行里手动安装: `pip install opencv-contrib-python --user`

`node_physical_blocks`正常运行之后，就可以到 Scratch 中编程。

## Scratch

打开这两个插件:

-   ImageData
-   Physical Blocks

![](/img/253ce5ec1a3a1c828cb8e994be28310e.png)

ImageData 负责与 Scratch 舞台区数据交互，诸如获取舞台区的截图或者视频数据等。

我们可以将这些数据传递到 Adapter 处理: `node_physical_blocks`便是一个能够处理 ImageData 数据的插件，你也可以自定义插件。

### 获取视频中的 marker 信息

首先我们要开启摄像头(**镜像开启**)

#### 获取 marker id 列表

使用该积木可以获得摄像头里所有的 marker 的 id 列表

![](/img/9e58f774c4ba5608c6071049441b056e.png)

可以看到视频里，一共有 4 个 marker，从左到右 id 分别为 **28， 27，26，25**

利用这个积木，可以构建 [单词拼写程序](https://scratch3v3.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-spell-demo.sb3){target=\_blank}

<video width=80% src="https://adapter.codelab.club/video/1590154622682774.mp4" controls="controls"></video>

#### 获取 marker 旋转角
使用该积木可以获得摄像头里某个 marker 的旋转角

![](/img/9c1c6546a1eb7a16d840d627bb213f6a.png)


[Scratch-marker-angle-demo.sb3](https://scratch3v3.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-marker-angle-demo.sb3){target=\_blank}

利用旋转角可以构建纸糊方向盘:

<video width=80% src="https://adapter.codelab.club/video/1591187790289712.mp4" controls="controls"></video>

#### 获取 marker 位置
使用该积木可以获得摄像头里某个 marker 的位置信息

![](/img/b43faf03d72bf90c938794f864963e7a.png)

