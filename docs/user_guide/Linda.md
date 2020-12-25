# Linda

!!! 提醒
    在 **Adapter >= 4.0** 中可用。  
    Adapter 4.0 预计本月底发布，CodeLab 成员可预先使用Alpha版 `http://nc.codelab.club:8888/s/ytJDb6kkBRM7z5k` (仅在 Neverland 内网可访问)

![](https://blog.just4fun.site/post/img/011233bf058d45eb2deb2b05e288f2bd.png)

# 介绍

CodeLab Adapter 4.0 内置了 Linda server（Tuple Space），目前我们提供了以下客户端（持续增加中...）与 Linda Tuple Space 交互:

-   [Python Client](#python-client)
-   [Scratch Client](#scratch-client)
-   [REST API](#rest-api)
-   [cli (命令行客户端)](#cli)
-   [JavaScript Client(开发者)](#javascript-client)
-   [mush-lang](#mush-lang)

Linda 最有趣的一个地方是，所有 Tuple Space 参与者（跨语言、跨系统、跨网络）都能够互操作，语义由参与者自己"协调", 所以 Alan Kay 将 Linda 称为"协调语言"。

# 基本操作(operate)

### 核心操作
*  out: 生成一个元组(tuple) 到 元组空间（tuple space）
*  in: 在tuple space中匹配元组，如果匹配到则消耗它, 如果未匹配则一直等待
    *  inp: in的非阻塞版本。 如果匹配到则消耗它, 如果未匹配则返回空元组
*  rd: read only,  在tuple space中匹配元组，如果匹配到则返回它(不移除), 如果未匹配则一直等待
    *  rdp: 非阻塞版本的 rd
*  eval: 暂不考虑实现

### 辅助操作
不在 linda 的原始论文中，是我自己的扩展

*  dump: 获取元组空间所有元组
*  status: 获取元组空间状态
*  reboot: 重置元组空间


# Python Client
安装依赖: `pip install https://github.com/CodeLabClub/codelab_adapter_client_python/archive/master.zip`


提供同步和异步两种基类:

-   AdapterNode
-   AdapterNodeAio

## AdapterNode

```python
from codelab_adapter_client import AdapterNode

class MyNode(AdapterNode):
    NODE_ID = "linda/test"

    def __init__(self):
        super().__init__()

node = MyNode()
node.receive_loop_as_thread()
time.sleep(0.1)

res = node.linda_reboot() # reboot linda server, clean tuple space
assert res == []

res = node.linda_out([1, 2, 3]) # out
assert res == [1, 2, 3]

res = node.linda_out([1, 2, 4]) # out
res = node.linda_dump()
assert res == [[1, 2, 3], [1, 2, 4]]

res = node.linda_rd([1, 2, 3]) # read and blocking
assert res == [1, 2, 3]

res = node.linda_rdp([1, 2, "*"]) # read but non-blocking
assert res == [1, 2, 3] # 先入先出

res = node.linda_in([1,2,3]) #  read then remove (blocking)
assert res == [1, 2, 3]
```

## AdapterNodeAio(异步)

同步和异步 API 保持一致

```python
import asyncio
from codelab_adapter_client import AdapterNodeAio

class MyNode(AdapterNodeAio):
    NODE_ID = "linda/test"

    def __init__(self):
        super().__init__()

# 以下代码在 jupyter 中运行，如果你想在python脚本中使用，请考虑异步代码的生命周期，参考:  https://github.com/CodeLabClub/codelab_adapter_client_python/blob/master/tests/test_linda_client.py#L26
task = asyncio.create_task(node.receive_loop())
await asyncio.sleep(0.1) # !! 等待zmq通信管道建立完成

_tuple = ["test_linda"]

# reboot
res = await node.linda_reboot()
assert res == []

# out
_tuple = ["hello", "world"]
await node.linda_out(_tuple)

# rdp
res = await node.linda_rdp(_tuple)
assert res == _tuple

# inp
res = await node.linda_inp(_tuple)
assert res == _tuple

res = await node.linda_dump()
assert res == []
```

更多用法参考测试文件: [test_linda_client.py](https://github.com/CodeLabClub/codelab_adapter_client_python/blob/master/tests/test_linda_client.py)

# Scratch Client

![](/img/535830f43871561e905b39e3133d4aa7.png)

![](/img/6f86e7818670c680547b9bfd70601504.png)

# REST API 

使用 [httpie](https://httpie.io/docs#non-string-json-fields) 作为客户端。`:=` 表示后边跟的是 json 数据

## out

`http post https://codelab-adapter.codelab.club:12358/api/linda operate=out tuple:='["hello", "linda"]'`

## in

`http post https://codelab-adapter.codelab.club:12358/api/linda operate=in tuple:='["hello", "linda"]'`

## dump

`http post https://codelab-adapter.codelab.club:12358/api/linda operate=dump tuple:='["dump"]'`

其他原语类似

## cli (命令行客户端)

```bash
pip install https://github.com/CodeLabClub/codelab_adapter_client_python/archive/master.zip
# pip install codelab_adapter_client --upgrade # 暂未更新到 pypi
codelab-linda --help

codelab-linda out --help

# reboot
codelab-linda reboot

# dump
codelab-linda dump

# out
codelab-linda out --data '[1, "hello"]'

# rd
codelab-linda rd --data '[1, "hello"]'
codelab-linda rd --data '[1, "*"]'

# rdp
codelab-linda rd --data '[1, 2, 3]' # []

# in
codelab-linda rd --data '[1, "*"]'
```

# JavaScript Client
方便开发者，将 Linda 引入自己的web项目。

CodeLab 目前使用 JavaScript Client，将 Linda 带入 CodeLab Scratch、CodeLab Adapter WebUI 和 Lively。

```js
import AdapterBaseClient from "./codelab_adapter_base.js"; // https://github.com/CodeLabClub/scratch3_eim/blob/v3/codelab_adapter_base.js
let NODE_ID = "linda/js/client";
let HELP_URL = "https://adapter.codelab.club/user_guide/Linda/";
let runtime = null;
let adapter_client = new AdapterBaseClient(NODE_ID, HELP_URL, runtime);

await adapter_client.linda_out([1,2,3]).then((data)=>{console.log("linda",data); return data}) 

tuple = await adapter_client.linda_in(["hi", "lively", "*"]).then((data)=>{console.log("linda",data); return data})

tuple = await adapter_client.linda_in(["hi", "python", "from Lively"]).then((data)=>{console.log("linda",data); return data})

tuple = await adapter_client.linda_in(["hello", "lively", "*"]).then((data)=>{console.log("linda",data); return data})

await adapter_client.linda_in([1,2,5], 1000).then((data)=>{console.log("linda",data); return data}) //超时
```



# mush-lang
>  LISP 是一种构建材料 -- Alan Kay

为了更好地探索 Linda 的可能性，我们围绕 Linda 的基本原语，构建了一门简单的语言 -- **mush-lang**。

mush-lang 采用 LISP 风格的语法，可以视为 LISP 的一门玩具方言。 LISP 因其同构性(内外表示一致)，可能是所有语言中最简单的。

mush-lang 目前在 Python 中实现。

![](/img/WechatIMG1765.png)

# Demo


## 多个 Scratch 角色 的 实时同步

<video width=80% src="/video/1608041327753652.mp4" controls="controls"></video>

在 Python 的例子中，我们甚至在Scratch里构建了 Server！


两个Scratch角色同步的代码如下

*  [linda-demo1](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/linda-demo1.sb3)
*  [linda-demo2](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/linda-demo2.sb3)


python 与 Scratch 同步的代码如下:

*  [linda-demo1](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/linda-demo1.sb3)

Python核心部分代码为:

```python
node.linda_out(["request", "loudness", "xxx"])
node.linda_in(["response", "loudness", "*"])
```


## Jupyter 与 Scratch 的互操作
<video width=80% src="/video/1608095793244042.mp4" controls="controls"></video>

跨语言对象之间的互操作

用到了 Jupyter notebook 里的 ipywidgets.

```python
# 请使用 jupyter notebook，而不是jupyterlab
from ipywidgets import interact, interactive, fixed, interact_manual
from codelab_adapter_client import AdapterNode
import time

class MyNode(AdapterNode):
    NODE_ID = "linda/jupyter"

    def __init__(self):
        super().__init__()

node = MyNode()
node.receive_loop_as_thread()

@interact(show=True, x=100, size=100)
def f(show,x,size):
    node.linda_out(["%%x", x], wait=False) # f函数是非阻塞的回调函数，使用wait=False参数，使node.linda_out使非阻塞的，此时相当于流，记得使用 message tuple（见下文）
    node.linda_out(["%%show", show], wait=False)
    node.linda_out(["%%size", size], wait=False)
    return show,x,size
```


# 进阶
## 消息风格
linda 的基本观点是数据不停生灭（由用户显式操控）。

如果我们想在 Linda 中实现 "消息/流" 的模式，可能会遇到tuple堆积（生产者太快）的问题（这是很严重的问题，似乎也不是正确使用linda的方式）

为了尽可能少地破坏概念完整性，我们引入了一种特殊的tuple来支持"消息/流"模式。

我们定义了一种叫做 message tuple 的 tuple，它像消息一样，每次只能流的瞬时截面: **一个数据**。

以下是几个message tuple的例子:

*  ("%%x", 1)
*  ("%%y", 50)
*  ("%%z", "hello", "world")

在语法层面，message tuple只是普通的tuple，唯一区别是第一个元素需要是如下风格字符串， "%%x", x可以是任意值，可以把它看作message tuple的id，不同id的message tuple被视为不同tuple，支持tuple的所有操作符。

以下是一个例子:


*  [message_tuple demo](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/linda-message_tuple.sb3)


!!!视角
    站在变量的视角，你可以将其看作全局变量


# FAQ

## 如何提到 Linda 操作的速度
[ZMQ_LOOP_TIME](https://adapter.codelab.club/user_guide/settings/#zmq_loop_time)

以下是一个在scratch里进行速率测试的demo

[linda-rate](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/linda-rate.sb3)


## Linda 与 EIM
Linda 与 EIM 将长期共存，一个 Adapter Node，即是Linda client，也是EIM client，它们各有所擅。长期来看，我们更偏好 Linda。



---



# 参考

-   [在 CodeLab Adapter 中实现 Linda 并发模型](https://blog.just4fun.site/post/%E7%BC%96%E7%A8%8B/adapter-linda/)
-   [Linda: 比 Actor 更好的并发模型](https://blog.just4fun.site/post/%E7%BC%96%E7%A8%8B/linda-intro/)
-   [[译]Alan Kay 看待'对象'的几次观点转变](https://blog.just4fun.site/post/%E7%BC%96%E7%A8%8B/alan-key-between-oo-fp/)
-   [建立在异步消息之上的同步指令: 分别在 JavaScript、Python、Squeak 上实现](https://blog.just4fun.site/post/%E7%BC%96%E7%A8%8B/async-msg-sync-cmd/)
-   [[译]Smalltalk 背后的设计原则](https://blog.just4fun.site/post/%E7%BC%96%E7%A8%8B/design-principles-behind-smalltalk/)
