# MQTT Adapter Node
提醒: 需要使用[CodeLab Adapter最新版本](/user_guide/install/)

通过继承[AdapterMQTTNode](https://github.com/CodeLabClub/codelab_adapter_mqtt_client/blob/master/codelab_adapter_mqtt_client/codelab_adapter_mqtt_client.py#L12), 我们可以利用MQTT通道构建Adapter Node，一旦你理解MQTT message的消息细节，就可以在任何平台任何设备上构建Adapter Node，从超级计算机到单片机。

如果你对Adapter Node概念不熟悉，可以参考[这里](/dev_guide/Adapter-Node/)

## 依赖
`pip install codelab_adapter_mqtt_client`

## demo
依然以反转字符串为例.

参考[helloworld_mqtt_node.py](https://github.com/CodeLabClub/codelab_adapter_mqtt_client/blob/master/examples/helloworld_mqtt_node.py)

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
        self.EXTENSION_ID = "eim"

    def external_message_processor(self, topic, payload):
        self.logger.debug(payload)
        content = payload["zmq_payload"]["content"]
        extension_id = payload["zmq_payload"]["extension_id"]
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
打开CodeLab Adapter，运行`extension_mqtt_gateway`插件， 该插件在zeromq与mqtt直接进行转换。

运行helloworld_mqtt_node: `python helloworld_mqtt_node.py`

让我们在[CodeLab Scratch3](https://scratch3v2.codelab.club/)中尝试一下反转字符串:

<img width="800px" src="../../img/v2/helloworld_extension.png"/>

成功！

[AdapterMQTTNode](https://github.com/CodeLabClub/codelab_adapter_mqtt_client/blob/master/codelab_adapter_mqtt_client/codelab_adapter_mqtt_client.py#L12)已经开源在Github上，如果你对任何细节感到好奇，就把盒子拆开来看吧。

## debug
新开一个窗口，运行`codelab-mqtt-monitor`(随codelab_adapter_mqtt_client一起安装)，你将能够看到往来的MQTT message的内部细节。

## 想象空间

当你通过`codelab-mqtt-monitor`了解了MQTT message的内部细节，你就可以使用任何语言的MQTT client来构建Adapter Node！你甚至可以在一个单片机中构建Adapter Node！

## 更多 MQTT tools
参考[codelab_adapter_mqtt_client#tools for debugging](https://github.com/CodeLabClub/codelab_adapter_mqtt_client#toolsfor-debugging)