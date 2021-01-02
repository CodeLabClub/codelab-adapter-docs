# Tutorial

## 介绍

<!--
physical blocks 是物理积木，基于 [ScratchJR blocks](https://www.scratchjr.org/learn/blocks) 改造而来。

使用 physical blocks，可以在一张桌子上对实物进行编程，而无需借助屏幕。

physical blocks 在软件层面是一个 CodeLab Adapter插件，由于 CodeLab Adapter 可以连接一切事物，所以physical blocks也可以对一切事物进行编程！ （参见文末 Demo）

它是 CodeLab DynamicTable 的一部分。

## 使用方式
*  打印 CodeLab physical blocks
*  运行 Adapter physical blocks 插件
*  使用 physical blocks 在桌子上进行编程
*  运行程序！
-->

!!! 提醒
    建议使用2.0版本: [physical blocks 2.0](/extension_guide/physical_blocks2/)。 不久将弃用1.0版本。

使用 physical blocks，可以在一张桌子上对实物进行编程。

Windows 和 Mac 用户开箱可用。 Linux需要安装依赖（参考文末）

建议以[入门案例](#_3)为模版。

参考:

-   [CodeLab DynamicTable: A Seeing World](https://www-old.codelab.club/blog/codelab-dynamictable-a-seeing-world/)
-   [CodeLab DynamicTable: 一个可实施的技术方案](https://www-old.codelab.club/blog/codelab-dynamictable-an-instance/)

## 积木介绍
![](/img/bb2b302ff9e4fc9cc00bc5883eb013bc.png)

可以从 [arucogen](https://chev.me/arucogen/) 查询 ArUco marker id

## Demo

<video width=80% src="/video/1589459621915320.mp4" controls="controls"></video>

<video width=80% src="/video/1589459630916864.mp4" controls="controls"></video>

<video width=80% src="/video/1590154622682774.mp4" controls="controls"></video>

## 入门案例

分享两个入门案例:

-   [Scratch-marker-angle-demo.sb3](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-marker-angle-demo.sb3){target=\_blank} : 获取 marker 旋转角
-   [Scratch-spell-demo.sb3](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-spell-demo.sb3){target=\_blank} : 获取 marker id 列表(从左到右，从上到下)

## 更多案例
*  [第一期的直播演示项目](https://www-old.codelab.club/blog/the-first-live-showcase-projects-code/)
*  [智能家居展厅](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-spelling-iot-show.sb3)

# FAQ

### 如何打印 Marker
我们提供了一份30张的版本:

![](/img/e6cc193e54fdda12ae3ada44c2299dfd.png)

你可以从 [arucogen](https://chev.me/arucogen/) 里打印（建议从编号1开始）

更多细节参考[CodeLab DynamicTable: 一个可实施的技术方案](https://www-old.codelab.club/blog/codelab-dynamictable-an-instance/)

### 默认的Marker只有50种, 想要更多怎么办
默认是`4X4_50`(最多50种)的marker， 你可以选择`4x4_100`(最多100种)，或者`4x4_1000`(最多1000种)

选择之后请修改(推荐使用[JupyterLab](/extension_guide/jupyterlab/))插件里对应的代码(104行):

```python
# aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_100)
```

关于不同的marker数量决定了字典的大小，越小的数字，鲁棒性越好。 考虑到大多数用户的场景，50个是够用的，所以我们默认采用50.

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
