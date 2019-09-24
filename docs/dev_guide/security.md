# 安全性

2.5.x 版本主要围绕安全性在做一些工作。

### [REST API](/dev_guide/REST-API/)

2.5.0 之后， [REST API](/dev_guide/REST-API/) 默认禁用,你需要通过[用户配置文件](/user_guide/settings/)启用它。

### WEBSOCKET API

如果你只是将 CodeLab Adapter 当作 message hub(空间编程)，你也通过设置`OPEN_WEBSOCKET_API = False`，WEBSOCKET API 将被禁用，那样 Web UI 将无法起作用。

### ZeroMQ

默认只接受本地(127.0.0.1)创建的[Adapter Node](/dev_guide/Adapter-Node/)的 ZeroMQ 消息， 如果你希望构建分布式应用，请设置`OPEN_MESSAGE_HUB=True`，那样 CodeLab Adapter 将接受来自其他机器的 ZeroMQ 连接请求。

当 MESSAGE_HUB 处于 open 状态时，如何保证安全呢？答案是: 使用 token.

### MQTT

如果你要使用 MQTT gateway，出于安全性考虑，请替换为自己的 mqtt uri，默认的插件使用开放的账号。

### Python Kernel

考虑到运行真实 Python 代码的风险，2.5.0 之后，我们[使用`eval`替代`exec`](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/extensions_v2/extension_python_kernel.py#L52),并且对其做了限制，尽管如此，黑客社区依然有针对 eval 的精妙攻击方式。

所以我们使用[verify_token](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/extensions_v2/extension_python_kernel.py#L39)验证请求的消息是否携带 token，考虑到兼容性，目前来自 WEBSOCKET API 的消息，默认被加上 token，所以我们在未来版本中将考虑对请求域名做检验。

如果你构建了安全攸关的应用，请考虑使用[verify_token](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/extensions_v2/extension_python_kernel.py#L39)校验 token。

!!! tip
    如果你希望像原先那样，真实地运行完整的 Python 代码，原先的插件在[这儿](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/extensions_v2/extension_python_kernel_exec.py)。

!!! tip
    如果你只是希望在浏览器中教学Python语法，在浏览器中运行的[Brython](https://brython.info/)可能是更好的的选择。