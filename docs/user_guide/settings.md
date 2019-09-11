# 配置文件

CodeLab Adapter 允许用户的自定义配置。只需要在`~/codelab_adapter`目录下创建`user_settings.py`文件即可。 以下是一些常见配置项:

## OPEN_MESSAGE_HUB

是否允许本地(localhost)之外的 Adapter Node 与 CodeLab Adapter 通信， 默认是`OPEN_MESSAGE_HUB=False`。

将 OPEN_MESSAGE_HUB 设为 True 的一个典型用例是将树莓派作为消息中心，把硬件能力提供给移动端(iPad/mobile)使用。

## USE_SSL

是否以 https 运行 Adapter Node 的 http/websocketss 服务。

默认`USE_SSL=True`。

将 USE_SSL 设为 False 的一个典型用例是 CodeLab Adapter 作为服务集成到 Electron 中。将 USE_SSL 设为 False 之后就不会存在证书过期问题（无需 https 证书）。

## AUTO_OPEN_WEBUI

是否自动打开 Web UI

默认`AUTO_OPEN_WEBUI = True`。

如果你希望将 CodeLab Adapter 用作内部服务，可以将 AUTO_OPEN_WEBUI 设为 False

## PYTHON3_PATH

系统的 Python3 路径，当使用[CodeLab Adapter server](https://github.com/Scratch3Lab/codelab_adapter_extensions/tree/master/servers_v2)时，实际上是调用了使用了系统的 Python3.

PYTHON3_PATH 默认为：

```python
    if (platform.system() == "Darwin"):
        path = "/usr/local/bin/python3"
    if platform.system() == "Windows":
        path = "python"
    if platform.system() == "Linux":
        path = "/usr/bin/python3"
```

你可以自行指定。

## DEFAULT_ADAPTER_HOST

默认`DEFAULT_ADAPTER_HOST = "codelab-adapter.codelab.club"`

如果你使用自己的 https 证书，可以替换为自己的域名。

## OPEN_WEBSOCKET_API

默认`OPEN_WEBSOCKET_API = True`

OPEN_REST_API用于打开/关闭WEBSOCKET API

## OPEN_REST_API

默认`OPEN_REST_API = True`

OPEN_REST_API用于打开/关闭[REST API](/dev_guide/REST-API/)

## TOKEN

默认`TOKEN = "<random string>"`

TOKEN 在软件初次运行的时候在本地随机生成，
