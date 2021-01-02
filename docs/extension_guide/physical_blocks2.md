# Tutorial

## 介绍
physical blocks 2.0，新的更新我们都将在这个版本是进行，[physical blocks 1.0](/extension_guide/physical_blocks/)在未来将弃用。

使用 physical blocks，可以在一张桌子上对实物进行编程。

Windows 和 Mac 用户开箱可用。 Linux需要安装依赖（参考文末）

!!! 提醒
    CodeLab Adapter版本 `>= 3.7.3`

参考:

-   [CodeLab DynamicTable: A Seeing World](https://www-old.codelab.club/blog/codelab-dynamictable-a-seeing-world/)
-   [CodeLab DynamicTable: 一个可实施的技术方案](https://www-old.codelab.club/blog/codelab-dynamictable-an-instance/)

## 积木介绍

![](/img/121f181ffb02f95cddf1501c47decd12.png)

可以从 [arucogen](https://chev.me/arucogen/) 查询 ArUco marker id

## Demo

<video width=80% src="/video/1589459621915320.mp4" controls="controls"></video>

<video width=80% src="/video/1589459630916864.mp4" controls="controls"></video>

<video width=80% src="/video/1590154622682774.mp4" controls="controls"></video>

## 入门案例

分享两个入门案例:

-   [physical-blocks2-angle-demo](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/physical-blocks2-angle-demo.sb3){target=\_blank} : 获取 marker 旋转角
-   [physical-blocks2-spell-demo](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/physical-blocks2-spell-demo.sb3){target=\_blank} : 获取 marker id 列表(从左到右，从上到下)

## 更多案例
*  [第一期的直播演示项目](https://www-old.codelab.club/blog/the-first-live-showcase-projects-code/)
*  [智能家居展厅](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-spelling-iot-show.sb3)

# FAQ

### 刷新率/FPS
在 MacOS（2.3 GHz Intel Core i5）下，大约达到10帧的刷新率

目前尚未发布的 Pro 版本大约是 20 帧的刷新率

可使用以下技巧观察刷新率:

![](/img/a438c5b97d7072c233101e1f06082caa.png)

### 与1.0版本的区别？
标记列表默认是字符串(序列化之后)，可以随意与scrath积木组合(诸如`xx包含xx`积木)，避免因为操作list引起的崩溃（诸如将list保存为变量）。

在2.0中，直到主动使用JSON parse积木解析后，它才称为列表。相关操作参考:[json积木](/extension_guide/json/)，也可参考前边的例子: [physical-blocks2-spell-demo](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/physical-blocks2-spell-demo.sb3){target=\_blank}

此外2.0 只使用一个积木更新数据，提高标签存在的稳定性（也提高速度），其中一种典型的编程模式是: 在一次更新数据之后的积木都对应更新瞬间的视野状态。而不像1.0，每个积木都有各自瞬间的视野。

### 如何打印 Marker
我们提供了一份30张的版本:

![](/img/e6cc193e54fdda12ae3ada44c2299dfd.png)

你可以从 [arucogen](https://chev.me/arucogen/) 里打印（建议从编号1开始）

更多细节参考[CodeLab DynamicTable: 一个可实施的技术方案](https://www-old.codelab.club/blog/codelab-dynamictable-an-instance/)

### 默认的Marker支持250种不同类型（marker id）
默认是`4X4_250`(最多250种)的marker， 你可以选择：

*  `4x4_50`(最多50种)
*  `4x4_250`(最多250种)
*  `4x4_100`(最多100种)
*  `4x4_1000`(最多1000种)

选择之后请修改(推荐使用[JupyterLab](/extension_guide/jupyterlab/))插件里对应的代码(104行):

```python
# aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_250)
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_1000)
```

关于不同的marker数量决定了字典的大小，越小的数字，鲁棒性越好。 

### Linux 用户

Linux 用户需要手动安装 `opencv-contrib-python`（有系统依赖）。

#### 树莓派用户

安装依赖系统

```bash
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt install libatlas-base-dev
sudo apt-get install qt4-dev-tools
sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103
```

之后安装`opencv-contrib-python`

-   `pip3 install opencv-contrib-python==3.4.6.27`
