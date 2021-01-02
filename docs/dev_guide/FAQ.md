# FAQ for Developer

## 编辑文档
欢迎大家来协同编辑文档：[codelab-adapter-docs](https://github.com/CodeLabClub/codelab-adapter-docs)。

## 讨论组
陆续有开发者建议我构建论坛（discourse）和微信群方便大家讨论技术问题。

微信群无法沉淀有价值的内容，搜索功能太烂了，对富文本/markdown 的支持几近于无，微信不是好的办公工具。

与 CodeLab Adapter 相关技术问题，大家可以在 [issue](https://github.com/CodeLabClub/codelab_adapter_extensions/issues) 里讨论。

也可以在 [CodeLab Adapter 讨论组](https://forums.codelab.club/c/codelab-adapter)里讨论。

## 插件启停
目前，插件启动为线程。Python 线程需要[手动管理](https://python3-cookbook.readthedocs.io/zh_CN/latest/c12/p01_start_stop_thread.html)，这部分的代码目前还比较粗糙。为了允许用户在 UI 中通过勾选来启停插件。建议插件作者使用`while self._running:`，参考 [extension_eim](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_eim.py)。


在 1.0 版本发布之前，插件部分我们将迁往协程，如此一来我们就能轻易管理插件的启停。目前 Python 社区很多库还不支持协程，所以我们不打算立刻迁移。

## 引入第三方 Python 库

内置的第三方库参考：[wiki](https://github.com/CodeLabClub/codelab_adapter_extensions/wiki)。

如果你需要引入新的第三方库（如OpenCV），需要在本地安装有 Python3，可以参考：[servers_v2](https://github.com/CodeLabClub/codelab_adapter_extensions/tree/master/servers_v2)。

关于这个话题，我们日后会给出教程。

<!--
Python 社区有海量的第三方库，开发者可以将其引入插件中。

方法是使用`sys.path.append`，如果希望在插件中使用本机 Python3 已安装的库（推荐`pip3 install xxx --user`），则将其添加到插件头部：`import sys;sys.path.append("/Users/wuwenjie/Library/Python/3.6/lib/python/site-packages")`，完整的示例参考： [extension_third_party_library](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_third_party_library.py)。

`/Users/wuwenjie/Library/Python/3.6/lib/python/site-packages`可通过`python3 -m site --user-site`看到。你也可以使用 virtualenv 创建的虚拟目录。

有些库引入的时候可能会有问题，一些复杂库，建议使用 subprocess 跑为子进程。
-->


## Python 与 Scratch 的双向通信
参考

*  [json message](/dev_guide/json-message/)
*  [Python 与 Scratch 的双向通信](https://blog.just4fun.site/python-scratch-with-adapter.html)


大多数情况下，你只需要发送和接受字符串就够了，这种风格与 Scratch 内置的广播极为相近。是典型的事件驱动风格。

这篇教程主要针对那些希望去拓展 Scratch 的人。当你需要将一些复杂的程序接入 Scratch（例如接入 AI 或者接入微信，如我们制作的例子），它会对你有帮助。

## 如何接入 Arduino
陆续有开发者问到，如何使用 CodeLab Adapter 将 Arduino 接入到 Scratch 3.0 中。

有许多种方法，但我比较偏好在 Arduino 中烧入 Firmata 固件。之后以固件交互，我在[两种硬件编程风格的比较](https://blog.just4fun.site/Hardware-Programming-style.html)论述了这样做的好处。

之后使用 Firmata python client 与 Arduino 交互。

细节可以参考 [Arduino 与 Scratch 3.0](https://blog.just4fun.site/Scratch3-adapter-Arduino-scratch.html)。

## 支持哪些平台
首先区分 CodeLab Adapter 和 CodeLab Adapter Node。

CodeLab Adapter 既是消息中心，又是UI程序，CodeLab Adapter 可以运行在：

*  Windows（win7/win8/win10）
*  Mac
*  linux
    *  Ubuntu
    *  Raspbian
    *  Android

CodeLab Adapter Node 可以运行在任何平台上，包括单片机。

## 覆盖配置文件
为了方便开发者将 CodeLab Adapter 整合到其他软件中，作为服务使用，诸如整合到 [Scratch Desktop](https://github.com/LLK/scratch-desktop)，或者整合到 docker 容器内，作为局域网消息服务……

CodeLab Adapter 允许以[命令行方式启动（没有GUI）](/user_guide/FAQ/#_4)。

为了方便软件的二次分发和自定义，CodeLab Adapter 允许开发者覆盖用户配置文件([user_settings.py](/user_guide/settings/))，进而对 CodeLab Adapter 做初始化配置。

只需要将自定义的 [user_settings.py](/user_guide/settings/) 放在 CodeLab Adapter 同级目录中即可。

## 如何集成到 Electron

只需要集成[scratch3_eim](https://github.com/CodeLabClub/scratch3_eim)即可。

如果你想使用 socketio client 连接与 Adapter 沟通，参考[此处源码](https://github.com/CodeLabClub/scratch3_eim/blob/v3/codelab_adapter_base.js#L61)。

## Scratch里的小绿点是怎么实现的？

Scratch里的小绿点用于反应网页与Adapter的连通性, 小绿点的状态由[AdapterBaseClient connected 属性](https://github.com/CodeLabClub/scratch3_eim/blob/v3/codelab_adapter_base.js)决定。它属于 scratch-gui，而不属于scratch extension，这部分你需要自己实现。