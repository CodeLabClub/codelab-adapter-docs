# I am reading!

<video width=80% src="/video/python_neverland.mp4" controls="controls"></video>

## 依赖

{!utils/neverland_require.md!}

## 项目介绍

你在房间里看《权力的游戏》，当房门突然被打开时，屏幕自动切换到阅读界面。

## 思路

在 Neverland 中使用 HANode 基类与空间中的智能家居交互: 当 **门窗传感器** 感应到门被推开时，将信号报告给电脑，将界面切换到读书 App。

## 涉及的知识

- 继承
- 面向对象（OOP）
- subprocess：从 Python 中调用系统命令
- 函数调用
- CodeLab Adapter Longan 插件

## 想象空间

- 使用 Python 为整个空间编程！

## 示例

### 项目源码

- [neverland_i_am_reading.py](https://github.com/CodeLabClub/codelab_adapter_client_python/blob/master/examples/neverland_i_am_reading.py)

### 使用说明

#### 步骤 1：安装 Python

{!utils/install_python.md!}

#### 步骤 2：安装依赖

`pip install codelab_adapter_client --upgrade`

#### 步骤 3：下载源码

将[项目源码](https://github.com/CodeLabClub/codelab_adapter_client_python/blob/master/examples/neverland_i_am_reading.py)复制或下载到本地。

#### 步骤 4：运行

`python neverland_i_am_reading.py`

### 你的创作

一些建议：

- 关上门之后你想触发什么行为？
- 看看其他的例子：[examples](https://github.com/CodeLabClub/codelab_adapter_client_python/tree/master/examples)
- 试试 Neverland 里的其他智能设备
