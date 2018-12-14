# FAQ for Developer

## 插件启停
目前，插件启动为线程。Python线程需要[手动管理](https://python3-cookbook.readthedocs.io/zh_CN/latest/c12/p01_start_stop_thread.html)，这部分的代码目前还比较粗糙。为了允许用户在UI中通过勾选来启停插件。建议插件作者使用`while self._running:`,参考[extension_demo](https://github.com/Scratch3Lab/scratch3_adapter_extensions/blob/master/extension_demo.py)


在1.0版本发布之前，插件部分我们将迁往协程，如此一来我们就能轻易管理插件的启停。目前Python社区很多库还不支持协程，所以我们不打算立刻迁移。

## 引入第三方Python库
Python社区有海量的第三方库，开发者可以将其引入插件中。

方法是使用`sys.path.append`,如果希望在插件中使用本机Python3已安装的库，则将其添加到插件头部:`import sys;sys.path.append("/usr/local/lib/python3.6/site-packages")`,完整的示例参考[extension_third_party_library](https://github.com/Scratch3Lab/scratch3_adapter_extensions/blob/master/extension_third_party_library.py)

`/usr/local/lib/python3.6/site-packages`可通过`pip3 show pip`看到。你也可以使用virtualenv创建的虚拟目录。

## Python与Scratch的双向通信
参考[Python与Scratch的双向通信](https://blog.just4fun.site/python-scratch-with-adapter.html)

大多数情况下，你只需要发送和接受字符串就够了，这种风格与Scratch内置的广播极为相近。是典型的事件驱动风格。

这篇教程主要针对那些希望去拓展Scratch的人。当你需要将一些复杂的程序接入Scratch（例如接入AI或者接入微信，如我们制作的例子），它会对你有帮助。