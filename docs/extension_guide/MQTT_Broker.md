# Tutorial
!!! 提醒
    3.2中可用(近期发布)

# 插件说明

-   使用方式: 到[插件市场](/extension_guide/extension_market/)下载插件, 搜索 **mqtt**
-   插件类型: [Adapter Extension](https://adapter.codelab.club/dev_guide/helloworld/)
-   插件源码: [extension_mqtt_broker.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_mqtt_broker.py)

# 使用场景

extension_mqtt_broker.py 插件允许你轻松在本地启动一个轻量级 MQTT Broker。

一个典型的使用场景是将各类支持 mqtt client 的硬件，接入 Adapter（当然你需要写一个 extension, 我们已经构建了一个:[MQTT_adapter](/extension_guide/MQTT_adapter/) ），这样方便你将 esp32、esp8266、掌控板等设备接入 Adapter 。

# Demo
```bash
hbmqtt_pub --url mqtt://127.0.0.1 -t /test -m some_data
hbmqtt_sub --url mqtt://127.0.0.1 -t /test
```

当然你可以使用任何mqtt client

# 高性能

基于高性能的[hbmqtt](https://hbmqtt.readthedocs.io/en/latest/index.html)。 基于协程的并发能力，足以让你在树莓派上支撑起整个学校的物联网。

# 进阶

你可以修改 broker 配置项，为其增加 auth 之类的功能, 详情参考[hbmqtt](https://hbmqtt.readthedocs.io/en/latest/index.html)文档。

# 参考

-   [hbmqtt](https://hbmqtt.readthedocs.io/en/latest/index.html)
