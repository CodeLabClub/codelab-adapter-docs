# Python exec kernel

## 依赖

{!utils/dependence.md!}

## 步骤 1：打开 Codelab Adapter

{!utils/open_adapter.md!}

Python exec 插件不是内置插件，需要自行在[插件市场](/extension_guide/extension_market/)下载。

[exec](https://docs.python.org/zh-cn/3.7/library/functions.html#exec) 比 [eval](https://docs.python.org/zh-cn/3.7/library/functions.html#eval) 更为强大（关于二者的区别参考[这儿](http://localhost:8000/extension_guide/extension_python_kernel/#_2)） ，可以执行任何 Python 代码，你甚至可以在 Scratch 里构建木马病毒。

![](/img/41eedbf599b54b6ae55270367a084d15.png)

## 步骤 2：打开 Codelab Scratch3

{!utils/open_scratch.md!}

## 步骤 3：hello world

选择对应的 Scratch3 插件：EIM.

![](/img/87c21a33377d036bc77b508f660c81f7.png)

在 Scratch 里使用 **插件启停积木** 启动 CodeLab Adapter Python exec 插件。

![](/img/ffff77596571818eec1ebb90451b2517.png)

现在你可以运行任何Python代码了!

我们还是以打开浏览器为例, 可以直接运行:`import webbrowser; webbrowser.open("https://www.codelab.club")`， `import`也是没问题的！

![](/img/6fd59d416f93334e7749f2a94bd5e060.png)

!!!提醒
    广播的主题是`eim/extension_python_exec`, extension_python_exec 正是插件的名字

## 延伸
python里能做的许多事情，现在你都可以在这个积木里做。让我们来做一些更复杂的事情。

让我们使用 Python 在Scratch里获取 CodeLab Adapter的最新版本，并让小猫🐱读出来

```python
import requests
latest_version_url = "http://adapter.codelab.club/about/latest_version.json"
response = requests.get(latest_version_url).json()
print(response["version"])
```

我们首先需要把这些代码变成单行代码， 可以使用[python single line convert](http://jagt.github.io/python-single-line-convert/){target=_blank}来做:

![](/img/aa507ed37b2b835fc5316abb42f4e681.png)

点击convert，开始转化，转化之后得到: `exec("""\nimport requests\nlatest_version_url = "http://adapter.codelab.club/about/latest_version.json"\nresponse = requests.get(latest_version_url).json()\nprint(response["version"])\n""")`

运行它！

![](/img/4c3dbbb99d7df8d3c2eec4048b3dbc2f.png)

完美！

!!!提醒
    我们使用了一些奇技淫巧在Scratch里写大段 Python 代码， 仅仅是出于好玩和 **because we can** 的 geek 精神，通常更好的做法是将一些功能代码放在adapter 扩展文件里，而不是在Scratch 里写大段代码，那将是难以阅读和理解的。