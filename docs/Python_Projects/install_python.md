# 安装 Python3 ( Install Python3 )

!!! 提醒开发者
    本地即便没有安装 Python3，CodeLab Adapter 也能正常运行( extension )，如果你想使用 Adapter Node (诸如 node_vector ) ，则需要在本地有 Python3 环境。  
    安装了 Python3 之后， Adapter 将自动与其关联， 第三方公司/开发者能够使用 Python 生态中的所有资源，为用户去构建新的扩展( extension / node )，这样第三方公司能够将各类 AI /硬件/服务 接入进来 。这为 Adapter 带来了几乎无限的可扩展性。值得注意的事，这种方式的时间成本极低，你只需要构建插件业务逻辑，其他的一切都是免费得到的，从跨平台到强大的连接能力，参考 [jupyterlab](/extension_guide/jupyterlab/)

在 CodeLab Adapter 中，通过点击查看环境，你可以看到本地Python环境是否存在。

![](/img/bdc2f794bd15ed3faab14165b72badc2.png)

你将看到:

![](/img/5d00c1e6ee237fe95671d791a54805e5.png)

如果你看到的信息和上图类似，则说明你本地已经安装了 Python3，请确保 Python3 版本 **>= 3.6**。 

如果你没有安装过Python3， 本文将引导你安装它。

## Windows用户
如果之前没有安装过Python3， 推荐下载安装 [Python3.7](http://scratch3-files.just4fun.site/python-3.7.4.exe)。下载完成后，点击安装即可。

如果你之前安装过Python3，但版本低于 **3.6** , 建议卸载后，再安装。


## MacOS用户
MacOS自带了 Python3，如果你看到系统自带的 Python3 版本低于**3.6**， 推荐下载安装 [Python3.7](http://scratch3-files.just4fun.site/python-3.7.5-macosx10.9.pkg)， 下载完成后，点击安装即可。

!!! 提醒
    如果你是开发者，你的本地环境里可能有很多个版本的 Python3 环境，建议使用 [pyenv](https://github.com/pyenv/pyenv) 来管理它。你可以在配置文件里，[指定 Adapter 使用的 Python 版本](https://adapter.codelab.club/user_guide/settings/#python3_path)。

## Linux用户
Linux 自带了 Python3，如果你看到系统自带的 Python3 版本低于**3.6**， 推荐使用 [pyenv](https://github.com/pyenv/pyenv) 安装新的 Python3 版本。

你可以在配置文件里，[指定 Adapter 使用的 Python3 版本](https://adapter.codelab.club/user_guide/settings/#python3_path)。

---


安装完成之后, 点击 刷新环境

![](/img/da31f790ff1fb874842d861ca8e5f943.png)


再次点击 查看环境，你应该可以看到本地Python环境信息。