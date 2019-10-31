# eim trigger

## 插件介绍

通过 **extension_eim_trigger** 插件，[Scratcher](https://en.scratch-wiki.info/wiki/Scratcher) 可以轻松使用 Python 拓展 Scratch 的能力。

**extension_eim_trigger** 通过调用 [~/codelab_adapter/extensions/eim_trigger.py](/user_guide/FAQ/#_1) 脚本， 往 Scratch 发送消息。 我们将其称为消息的触发机制( **trigger** )。

默认的脚本，每隔 1s，往 Scratch 中发送一次时间戳，[脚本源码](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/extensions_v2/eim_trigger.py)(简单的 Python 代码)为:

```python
import time

def trigger():
    timestamp = time.time()
    time.sleep(1)
    return timestamp
```

你可以随意修改 **trigger** 脚本代码，往 Scratch 中发送任意数据。

## 依赖

{!utils/dependence.md!}

## 步骤 1: 打开 Codelab Adapter

{!utils/open_adapter.md!}

## 步骤 2: 打开 Codelab Scratch3

{!utils/open_scratch.md!}

## 步骤 3: 加载 extension_eim_trigger 插件

在 Web UI 中点击加载 **extension_eim_trigger** 插件:

<img width="300px" src="/img/v2/open_adapter_trigger_extension.png"/>

开启 **extension_eim_trigger** 插件后,

## 步骤 4: hello world

选择对应的 Scratch3 插件: EIM

<img width="600px" src="/img/v2/scratch3_extensions_eim.png"/>

让 Scratch3 的角色读出每秒更新一次的时间戳:

<img width="600px" src="/img/v2/scratch_trigger_run.png"/>

## 步骤 5: 自定义 eim_trigger 逻辑

默认的逻辑是 **每秒更新一次时间戳**, 相应代码为:

```python
import time

def trigger():
    timestamp = time.time()
    time.sleep(1)
    return timestamp
```

运行 **extension_eim_trigger** 插件后， **trigger** 函数会被重复调用，通过修改 **trigger** 函数的返回值，可以让 Scratch 中发送任意数据。

!!! help
    如何找到 **eim_trigger.py** 文件? [~/codelab_adapter/extensions/eim_trigger.py](/user_guide/FAQ/#_1)

## 其他用例
```python
import time
i = 0
def trigger():
    global i
    i += 1
    time.sleep(1)
    return i
```

## 参考

- [使用 Python 拓展 Scratch 的能力](https://blog.just4fun.site/scratch-adapter-eim-script.html)
