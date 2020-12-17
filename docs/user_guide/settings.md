# 配置文件

CodeLab Adapter 允许用户的自定义配置。配置文件位于:`~/codelab_adapter/user_settings.py`。 

支持使用环境变量覆盖这些配置项，诸如`AUTO_OPEN_WEBUI=false codelab-adapter`

以下是一些常见配置项：

## ADAPTER_MODE
有三种模式：

1. NORMAL, 普通用户模式，CodeLab Adapter 作为客户端程序，增强 Scratch，支持自定义插件……关注易用性与安全性。
2. DEV（开发）模式，关注灵活性，同时也带来安全风险。
3. NEVERLAND_HUB 模式， 用于Neverland 2.0
4. LONGAN_HUB 模式, 关注健壮性

<!--
    NORMAL = 1  # Sun的value被设定为0
    DEV = 2
    NEVERLAND_HUB = 3
    LONGAN_HUB = 4
-->

## KEEP_LAST_CLIENT
是否强行保留最后一个web client（webUI 或 Scratch）

默认是 `False`

## ALWAYS_KEEP_ADAPTER_RUNNING
当所有web client退出时， Adapter 软件是否也退出

默认是 `False`


## OPEN_MESSAGE_HUB

是否允许本地（localhost）之外的 Adapter Node 与 CodeLab Adapter 通信，默认是`OPEN_MESSAGE_HUB=False`。

将 OPEN_MESSAGE_HUB 设为 True 的一个典型用例是将树莓派作为消息中心，把硬件能力提供给移动端（iPad/mobile）使用。

## USE_SSL

是否以 https 运行 Adapter Node 的 http/websocketss 服务。

默认`USE_SSL=True`。

将 USE_SSL 设为 False 的一个典型用例是 CodeLab Adapter 作为服务集成到 Electron 中。将 USE_SSL 设为 False 之后就不会存在证书过期问题（无需 https 证书）。

## AUTO_OPEN_WEBUI

是否自动打开 Web UI

默认`AUTO_OPEN_WEBUI = True`。

如果你希望将 CodeLab Adapter 用作内部服务，可以将 AUTO_OPEN_WEBUI 设为 False。

## PYTHON3_PATH

系统的 Python3 路径， 只在 lite 版本（linux）中可用，默认为 `"/usr/bin/python3"`, 你可以自行指定。

## DEFAULT_ADAPTER_HOST

默认`DEFAULT_ADAPTER_HOST = "codelab-adapter.codelab.club"`

如果你使用自己的 https 证书，可以替换为自己的域名。

## OPEN_WEBSOCKET_API

默认`OPEN_WEBSOCKET_API = True`

OPEN_REST_API 用于打开/关闭 WEBSOCKET API。

## OPEN_REST_API

默认`OPEN_REST_API = True`

OPEN_REST_API 用于打开/关闭 [REST API](/dev_guide/REST-API/)。

## TOKEN

默认为`None`，软件每次启动都将随机生成 TOKEN。

取消注释`# TOKEN = "<random string>"`，则永久固定 TOKEN。

`<random string>` 在软件初次运行的时候在本地随机生成。

## RC_EXTENSIONS
默认启动的 EXTENSIONS

默认为 `[]`

## RC_NODES
默认启动的 NODES

在mac下 RC_NODES 默认为: `["node_status_bar.py"]`, 它是一个 [menu bar](https://support.apple.com/zh-cn/guide/mac-help/mchlp1446/mac)

![](/img/00e8f34f01567100b4cdcc83b2941068.png)

在windows/linux 下 RC_NODES默认为`[]`


## USER_WHITELIST_HOSTNAME
白名单

只有加入白名单的域名才能与 Adapter 通信。

## ZMQ_LOOP_TIME
决定消息收发的速度，由于Adapter本质上是个消息系统，所以 ZMQ_LOOP_TIME 直接影响Adapter的运行速度。

ZMQ_LOOP_TIME 默认值 0.02 （秒），ZMQ_LOOP_TIME 越小，Adapter 消息速度(EIM、Linda)越快。

相应的代价是 Adapter 会占用更多CPU。

## OPEN_LINDA_REST_API
是否开启 [Linda REST API](https://adapter.codelab.club/user_guide/Linda/#rest-api)

默认是开启(True)

## 