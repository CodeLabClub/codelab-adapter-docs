# Python

## 介绍
![](https://create.codelab.club/static/assets/1179a47022f9371566a78bd7868b68c8.jpg)

此扩展可以将 Python 代码交给 Adapter 执行（eval），并获取结果。

## hello world

打开 Scratch Python 插件

![](/img/1cd2e68f21c8a9d46f3a77f246b2cb41.png)

在 Scratch Python 插件里使用 **插件启停积木** 启动 CodeLab Adapter Python 插件。

![](/img/0d02673f6b41e5682510700191d28888.png)

执行 Python 代码:

![](/img/be7dd34fa27a46d1d1a4bd0dd2d6f71e.png)

## 积木说明
暂无

## 项目链接

### 自定义积木

你可以在插件中添加新的类，来自定义新功能, 我们做了一个范例: [PyHelper 源码](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_python.py#L18)。你可以使用 `PyHelper.open_url("https://www.codelab.club")`来为 Scratch 引入打开网页的功能。

你甚至可以更进一步，在 Scratch 中自定义积木！不需要编程 JavaScript，通过 Python 来扩展 Scratch！让我们构建一个打开网页的积木（Scratch本身没有打开网页的功能）:

点击制作新的积木:

![](/img/96e4ef0e81593944dbce7071bc81b828.png)

制作自定义积木，`添加输入项目`: url 参数.

![](/img/006c9f1b71307986b95d19ffea8c83e9.png)

接下来我们开始定义这个积木的功能，完成之后我们就可以使用它了

![](/img/3934f415f497c5080c7102cd6df3cb89.png)

以上例子的功能是按下空格，打开 CodeLab 主页。

你可以在插件里添加更多的类似`PyHelper`的自定义类，来为 Scratch 引入更多新的能力，使用 Python 就行！

### 文件储存案例

再来做一个例子，[@HansonXie](http://www.concentric-circle.com/author/admin/) 给我写了封邮件，说想写一个extension或者node来进行文件存储，希望用Python来做，而不是Javascript。在此我写个简单例子

我们可以使用 [Jupyterlab](/extension_guide/jupyterlab/) 编辑[extension_python.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_python.py). 在其中增加一个新的助手类，来负责存储文件

```python
class StorageHelp:
    def save_text_to_file(text, filename):
        with open(filename, "w"):
            filename.write(text)

```

之后,将其添加到eval中（使其可用)。

```python
eval(code, {"__builtins__": None}, {
                "PyHelper": self.PyHelper,
                "StorageHelp": StorageHelp()
            })
```

![](/img/262902f683ac487805e57536b8514dcb.png)

完成后，重新勾选extension_python.py（stop and start，不需要重启 Adapter）。

此次，自定义的积木，包括两个参数：存储的文本(text) 和 文件名(filename)

![](/img/53b39ca6689c28684215713de1410341.png)

!!!提醒
    注意文件名和内容都是字符串，有引号`"xxxxx"`

点击运行新的积木, 在jupyterlab中，可以看到新创建的文件已经在 extensions 目录里

![](/img/0a58a769497bdd4cacb5e93acca88014.png)

## FAQ
### 如何工作

!!! 提醒
    exec 可能带来各种安全风险，此外，eval也更符合我们采用的`对象/消息`隐喻。  
    如果你确实需要exec，可以自行构建插件， 参考[python_exec.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/python_exec.py)

内置在 Adapter 里的 Python 插件以 [eval](https://docs.python.org/zh-cn/3.7/library/functions.html#eval) 执行 Python 代码(只能执行表达式)，如果你希望以功能更轻大的 [exec](https://docs.python.org/zh-cn/3.7/library/functions.html#exec) (可执行任何 Python 语句)执行 Python 代码，可以在[插件市场](/extension_guide/extension_market/)里下载 [extension_python_exec 插件](/extension_guide/python_exec/)。

关于 eval 和 exec 的区别，参考:

-   [深度辨析 Python 的 eval() 与 exec()](https://juejin.im/post/5c97885b6fb9a070c11f929e)
-   [What's the difference between eval, exec, and compile?](https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile)

我们之没有将 extension_python_exec 内置在 Adapter 中，而是希望用户在需要时自行下载，因为它的功能过于强大，可能会带来一下风险，所以选择权交由使用者。强大的能力通常会伴随风险，当然我们不会做太多限制，由你决定：）


## 参考

-   [将 codelab-adapter 用作 Python 解释器](https://wwj718.github.io/scratch3-adapter-as-python-interpreter.html)

<!--
-   [使用 Scratch 3.0 制作幻灯片](https://wwj718.github.io/scratch3-adapter-presentation.html)。

-->
