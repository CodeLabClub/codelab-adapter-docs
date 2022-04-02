# JupyterLab
![](https://jupyterlab.readthedocs.io/en/stable/_images/jupyterlab.png)

## 介绍
[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) 是 jupyter notebook 的下一代产品。  

Jupyter Notebook（前身是IPython Notebook）是一个基于Web的交互式计算环境。

如果你正在学习 Python/数据科学/人工智能，它是你绝佳的编程环境。

CodeLab Adapter 将其集成到插件，如果想编辑代码，诸如

*  [编辑 CodeLab Adapter的配置文件](/user_guide/settings/)
*  [使用 Python 扩展 Scratch的能力](/extension_guide/eim_monitor/)
*  [构建新插件](/dev_guide/helloworld/)

它都是我们推荐的工具。

或者任何时候你想学习 Python ，JupyterLab 都是你理想的伙伴。

## hello world
在 webUI 里运行 **extention_jupyterlab** 插件。

![](/img/1e0f0b09f47ceddcb57ae90141db2b66.png)

---

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

## 积木说明
暂无

## 项目链接
暂无

## FAQ

### 启用 Jupyterlab 插件，没有自动打开 Jupyterlab
可能是因为你的系统用户名（windows系统）是中文，目前 Jupyterlab 存在这个 bug, 官方正在修复中。

我们目前给出了一个手动打开方案:

1. 启动 Jupyterlab 插件
2. 稍等 3-5秒， 之后在浏览器里打开`localhost:8888` (如果打不开，则试试`localhost:8889`)
3. 复制 `Adapter token` 到 Jupyterlab 登陆框里

![](/img/0dfae2da010f3a18f600fb490a95583b.png)



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


###  精简版(linux/RPI)如何安装 jupyterlab
完整版已经内置了一切依赖。

如果你是有精简版，确保你已经[安装了 Python3](/Python_Projects/install_python/)。  

你不必手动安装 **jupyterlab** ，运行插件，CodeLab Adapter 会为你其余的一切。  

当然你也可以在命令行里手动安装它。

### 如何启动实时协作模式
[实时协作模式](https://jupyterlab.readthedocs.io/en/stable/user/rtc.html)对于结对编程、远程教学以及课堂教学可能都有帮助。

启动实施模式的方法是，使用 jupyterlab 打开 extensions 目录里的 `extension_jupyterlab.py` 插件，将 `self.allow_collaborative`改为True。 之后重启 Jupyterlab 插件。

此时，同一个局域网里的任何电脑都可以进入同一个 Jupyterlab 里，进行实时协作。 

具体方法是:

1. 在其他电脑上的浏览器里(可以是移动设备！)，打开启用实时协作的Jupyterlab的地址入口(形如`192.168.31.100:8888`)， 之后输入token，token与Adapter token一样。
2. 结对编程者打开同一个notebook文件（或者 `.py` 文件）。

### 运行 Python 脚本

在 Jupyterlab 中打开 **终端**.

MacOS:

`./Support/bin/python3 ./adapter_home/notebooks/hello.py`

Windows:

`.\src\python\python .\src\adapter_home\notebooks\hello.py`

### 为何 MacOS 下无法在jupyterlab使用摄像头(如在opencv中)

最近几个版本的 MacOS 对权限管理非常严格，需要从命令行启动 Adapter（允许访问摄像头）


### 更新Adapter后，Jupyterlab页面显示白色

是因为jupyterlab版本升级造成的。

删除 `C:\Users\<CurrentUserName>\.jupyter` 目录，重启 Adapter