# EIM Monitor

## 插件介绍

通过 **extension_eim_monitor** 插件，[Scratcher](https://en.scratch-wiki.info/wiki/Scratcher) 可以轻松使用 Python 拓展 Scratch 的能力。

当 **extension_eim_monitor** 启用时， 来自 Scratch EIM 插件的消息将被 [~/codelab_adapter/extensions/eim_monitor.py](/user_guide/FAQ/#_1) 脚本处理， 处理结果返回给 Scratch。 我们将这种对 Scratch 消息的响应机制称为 **monitor** 。

默认的脚本，会在Scratch的消息结尾加上`from monitor`并返回。[脚本源码](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v2/eim_monitor.py)（简单的 Python 代码）为：

```python
def monitor(content,logger):
    return content + ' from monitor'
```

你可以随意修改 **monitor** 脚本代码，改变处理规则。

## 依赖

{!utils/dependence.md!}

## 步骤 1：打开 Codelab Adapter

{!utils/open_adapter.md!}

## 步骤 2：打开 Codelab Scratch3

{!utils/open_scratch.md!}

## 步骤 3：加载 extension_eim_monitor 插件

在 Web UI 中点击加载 **extension_eim_monitor** 插件

## 步骤 4：hello world

选择对应的 Scratch3 插件：EIM

<img width="600px" src="/img/v2/scratch3_extensions_eim.png"/>

往 CodeLab Adapter 发送消息，观看 Python 对其的处理结果：

<img width="600px" src="/img/v2/scratch_monitor_run.png"/>

## 步骤 5：自定义 eim_monitor 逻辑
修改 **eim_monitor.py** 代码后，需要重启勾选 **extension_eim_monitor** 插件。

运行 **extension_eim_monitor** 插件后， **monitor** 函数会被重复调用，通过修改 **monitor** 函数的返回值，可以让 Scratch 中发送任意数据。

!!! help
    如何找到 **eim_monitor.py** 文件? [~/codelab_adapter/extensions/eim_monitor.py](/user_guide/FAQ/#_1)

## 其他用例
```python
import webbrowser
def monitor(content,logger):
    '''
    打开网页
    '''
    webbrowser.open(content)
    return "ok"
```

在 Scratch EIM 中传递消息`https://www.codelab.club`试试。

## 参考

- [使用 Python 拓展 Scratch 的能力](https://blog.just4fun.site/scratch-adapter-eim-script.html)
