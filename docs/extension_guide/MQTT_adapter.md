# Tutorial

# 插件说明

-   使用方式: 到[插件市场](/extension_guide/extension_market/)下载插件, 搜索 **mqtt**
-   插件类型: [Adapter Extension](https://adapter.codelab.club/dev_guide/helloworld/)
-   插件源码: [extension_mqtt_adapter.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_mqtt_adapter.py)

# 使用场景

extension_mqtt_adapter.py 插件桥接 mqtt 与 Scratch。

原理很简单，它将来自mqtt的消息(mqtt topic:`to_scratch`)，转发到 eim 中，将eim中的消息转发到mqtt(mqtt topic:`from_scratch`). （下文有例子）

## mqtt -> Scratch
!!! 提醒
    你需要首先选择一个mqtt broker，[extension_mqtt_adapter.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_mqtt_adapter.py#L24)假设你在本地运行了一个mqtt broker(mqtt 127.0.0.1 1883)。你可以使用任何mqtt broker。在 Adapter 3.2 中，将自带一个轻量级高性能的 mqtt broker: [MQTT Broker](https://adapter.codelab.club/extension_guide/MQTT_Broker/)

将消息从mqtt client 发往Scratch:

`hbmqtt_pub --url mqtt://127.0.0.1 -t to_scratch -m "mqtt message"`

当然你可以使用任何 mqtt client代替 [hbmqtt_pub](https://hbmqtt.readthedocs.io/en/latest/references/hbmqtt_pub.html)

![](/img/3d038a2722e91bebf7af544b40fe71f1.png)


## Scratch -> mqtt
将消息从Scratch 发往 mqtt client

先启动 mqtt client 的消息订阅。当然你可以使用任何 mqtt client代替 [hbmqtt_sub](https://hbmqtt.readthedocs.io/en/latest/references/hbmqtt_sub.html)


```bash
hbmqtt_sub --url mqtt://127.0.0.1 -t from_scratch
```

![](/img/0f3729283a13ed781801789995b8e4a8.png)

# Scratch 相关源码
[Scratch-mqtt-adapter](https://scratch3v3.codelab.club?sb3url=https://adapter.codelab.club/sb3/Scratch-mqtt-adapter.sb3)
