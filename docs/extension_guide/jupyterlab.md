# [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/)

JupyterLab 是 jupyter notebook 的下一代产品。  

Jupyter Notebook（前身是IPython Notebook）是一个基于Web的交互式计算环境。

如果你正在学习 Python/数据科学/人工智能，它是你绝佳的编程环境。

CodeLab Adapter 将其集成到插件，如果想编辑代码，诸如

*  [编辑 CodeLab Adapter的配置文件](/user_guide/settings/)
*  [使用 Python 扩展 Scratch的能力](/extension_guide/eim_monitor/)
*  [构建新插件](/dev_guide/helloworld/)

它都是我们推荐的工具。

或者任何时候你想学习 Python ，JupyterLab 都是你理想的伙伴。

# Tutorial
## 依赖

{!utils/dependence.md!}

## 步骤 1：打开 Codelab Adapter

{!utils/open_adapter.md!}

运行 **extention_jupyterlab** 插件。

!!! 提醒
    完整版已经内置了一切依赖。  
    如果你是有精简版，确保你已经[安装了 Python3](/Python_Projects/install_python/)。  
    你不必手动安装 **jupyterlab** ，运行插件，CodeLab Adapter 会为你其余的一切。  
    当然你也可以在命令行里手动安装它。

## 步骤 2：使用 jupyterlab
jupyterlab 默认将打开 [Adapter主目录](/user_guide/FAQ/#adapter)。

![](/img/ef69bd04ec22e90d3cf449e24c5e83e8.png)

[Adapter主目录](/user_guide/FAQ/#adapter)存放有:

1. [用户配置文件](/user_guide/settings/)
2. extensions 目录（可以在此修改 extension 的行为（如[eim_monitor](/extension_guide/eim_monitor/) ,修改完后，重新勾选插件即可，不必重启 Adapter）
3. nodes 目录（可以在此修改 [Adapter Node](/dev_guide/Adapter-Node/) 的行为，修改完后，重新勾选插件即可，不必重启 Adapter）
4. jupyter notebooks (用于存放Python代码，你可以从这里开始你的Python之旅)
5. 资源文件(诸如 webui 的 html 文件，你可以自由修改！)
6. Adapter 运行日志，当你需要[调试](/dev_guide/debug/) extension 时，查看日志将很有帮助。

你可以使用 jupyterlab 随意修改它们。别担心改坏了。如果发现修改后 Adapter无法正常运行。则将整个[ Adapter 主目录](/user_guide/FAQ/#adapter)删除即可，重启 Adapter，你将得到一个崭新的 Adapter 主目录。它是为你学习而构建的环境，别担心玩坏它，尽情探索吧。

# FAQ

### 启用 Jupyterlab 插件，没有自动打开 Jupyterlab
可能是因为你的系统用户名（windows系统）是中文，目前 Jupyterlab 存在这个 bug

### 安装第三方库
```py
import pip
# 举个例子: 安装 furl
pip.main(["install", "furl"])
# 你也可以使用国内的源: 
# pip.main(['install', 'furl', '-i', 'https://mirrors.aliyun.com/pypi/simple'])
# 针对ssl证书有问题的用户  pip.main(['install', 'furl', '-i', 'http://mirrors.aliyun.com/pypi/simple', "--trusted-host", "mirrors.aliyun.com"])
```

安装完之后，需要在 jupyterlab 重启kernel，也可以重启 jupyterlab。

### 列出所有库
```py
import pip 
pip.main(["freeze"])
```

### 汉化
`Adapter >= 3.3.1`，jupyterlab 版本升级到 3.0，支持切换语言:

![](/img/11fb41502c94b84002f80a965be907fa.png)