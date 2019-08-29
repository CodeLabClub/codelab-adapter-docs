# 配置文件
CodeLab Adapter允许用户的自定义配置。只需要在`~/codelab_adapter`目录下创建`user_settings.py`文件即可。 以下是一些常见配置项:

### OPEN_MESSAGE_HUB
是否允许本地(localhost)之外的Adapter Node与CodeLab Adapter通信， 默认是`OPEN_MESSAGE_HUB=False`。

将OPEN_MESSAGE_HUB设为True的一个典型用例是将树莓派作为消息中心，把硬件能力提供给移动端(iPad/mobile)使用。

### USE_SSL
是否以https运行Adapter Node的http/websocketss服务。

默认是`USE_SSL=True`。

将USE_SSL设为False的一个典型用例是CodeLab Adapter作为服务集成到Electron中。将USE_SSL设为False之后就不会存在证书过期问题（无需https证书）。


### AUTO_OPEN_WEBUI
是否自动打开Web UI

默认是`AUTO_OPEN_WEBUI = True`。

如果你希望将CodeLab Adapter用作内部服务，可以将AUTO_OPEN_WEBUI设为False

### PYTHON3_PATH
系统的Python3路径，当使用[CodeLab Adapter server](https://github.com/Scratch3Lab/codelab_adapter_extensions/tree/master/servers_v2)时，实际上是调用了使用了系统的Python3.

PYTHON3_PATH默认为：

```python
    if (platform.system() == "Darwin"):
        path = "/usr/local/bin/python3"
    if platform.system() == "Windows":
        path = "python"
    if platform.system() == "Linux":
        path = "/usr/bin/python3"
```

你可以自行指定。

### DEFAULT_ADAPTER_HOST
默认是`DEFAULT_ADAPTER_HOST = "codelab-adapter.codelab.club"`

如果你使用自己的https证书，可以替换为自己的域名。
