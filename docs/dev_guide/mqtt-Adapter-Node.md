# MQTT Adapter Node

!!! 提醒
    还未迁移到 Adapter 3.0, 推荐先使用 [MQTT_adapter](/extension_guide/MQTT_adapter/)

提醒：需要使用 [CodeLab Adapter 最新版本](/user_guide/install/)。

通过继承 [AdapterMQTTNode](https://github.com/CodeLabClub/codelab_adapter_mqtt_client/blob/master/codelab_adapter_mqtt_client/codelab_adapter_mqtt_client.py#L12)，我们可以利用 MQTT 通道构建 Adapter Node，一旦你理解 MQTT message 的消息细节，就可以在任何平台任何设备上构建 Adapter Node，从超级计算机到单片机。

如果你对 Adapter Node 概念不熟悉，可以参考[这里](/dev_guide/Adapter-Node/)。

## 依赖
`pip install codelab_adapter_mqtt_client`

## Demo
依然以反转字符串为例：

参考 [helloworld_mqtt_node.py](https://github.com/CodeLabClub/codelab_adapter_mqtt_client/blob/master/examples/helloworld_mqtt_node.py)

```python
import json
import time
from codelab_adapter_mqtt_client import AdapterMQTTNode
from codelab_adapter_mqtt_client.topic import *
from loguru import logger


class HelloWorldMQTTNode(AdapterMQTTNode):
    def __init__(self, *args, **kwargs):
        kwargs["logger"] = logger
        kwargs["external_message_processor"] = self.external_message_processor
        super().__init__(*args, **kwargs)
        self.NODE_ID = "eim"

    def external_message_processor(self, topic, payload):
        self.logger.debug(payload)
        content = payload["zmq_payload"]["content"]
        NODE_ID = payload["zmq_payload"]["NODE_ID"]
        if type(content) == str:
            content_send_to_scratch = content[::-1] # 反转
            payload["zmq_payload"]["content"] = content_send_to_scratch
            self.publish(payload)

if __name__ == "__main__":
    node = HelloWorldMQTTNode()
    try:
        node.client.on_message = node.mqtt_on_message
        node.run()
    except KeyboardInterrupt:
        print('Control-C detected. See you soon.')
        node.clean_up()
```

## 运行
打开 CodeLab Adapter，运行`extension_mqtt_gateway`插件，该插件在 zeromq 与 mqtt 直接进行转换。

运行 helloworld_mqtt_node：`python helloworld_mqtt_node.py`

让我们在 [CodeLab Scratch3](https://scratch-beta.codelab.club/) 中尝试一下反转字符串：

<img width="800px" src="../../img/v2/helloworld_extension.png"/>

成功！

[AdapterMQTTNode](https://github.com/CodeLabClub/codelab_adapter_mqtt_client/blob/master/codelab_adapter_mqtt_client/codelab_adapter_mqtt_client.py#L12) 已经开源在 GitHub 上，如果你对任何细节感到好奇，就把盒子拆开来看吧。

## Debug
新开一个窗口，运行`codelab-mqtt-monitor`（随 codelab_adapter_mqtt_client 一起安装），你将能够看到往来的 MQTT message 的内部细节。

## 想象空间

当你通过`codelab-mqtt-monitor`了解了 MQTT message 的内部细节，你就可以使用任何语言的 MQTT client 来构建 Adapter Node！你甚至可以在一个单片机中构建 Adapter Node！

## 更多 MQTT tools
参考 [codelab_adapter_mqtt_client#tools for debugging](https://github.com/CodeLabClub/codelab_adapter_mqtt_client#toolsfor-debugging)。
