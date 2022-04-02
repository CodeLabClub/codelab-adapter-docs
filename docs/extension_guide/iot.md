# MQTT 插件
MQTT broker 需要支持 wss(websockets) 协议, 才能在Scratch里连接它

CodeLab合作伙伴[英荔教育](https://aimaker.space/about)为CodeLab社区用户提供一个免费 MQTT broker: 


*  url: mqtt.longan.link
*  默认用户名/密码: guest/test
*  tcp port: 1883
*  tls port 8883
*  websockets port: 8084

# Demo
## scratch client
[scratch demo](https://create.codelab.club/projects/22163/editor/)

## python client
基于 [paho-mqtt](https://github.com/eclipse/paho.mqtt.python)

```py
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        print('已连接')
    else:
        print('连接出错！')
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('guest', 'test')

client.connect("mqtt.longan.link", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever() # client.loop_start() 是非阻塞的
```

## MicroBlocks demo
[MicroBlocks demo](https://microblocks.codelab.club/#scripts=GP%20Scripts%0Adepends%20%27MQTT%27%20%27WiFi%27%0A%0Ascript%20429%20-138%20%7B%0AwhenStarted%0Acomment%20%271.%20connect%20wifi%27%0A%27wifi%20connect%20to%27%20%27Elite_1006%27%20%2720130530%27%203%0AwaitMillis%201000%0Acomment%20%272.%20connect%20MQTT%20broker%27%0A%27MQTT%20connect%20to%27%20%27mqtt.longan.link%27%20128%20%27MicroBlocks_client%27%20%27guest%27%20%27test%27%0Acomment%20%27subscribe%20topic%27%0A%27MQTT%20sub%27%20%27microblocks%27%0AsendBroadcast%20%27go%21%27%0A%7D%0A%0Ascript%20429%20155%20%7B%0AwhenBroadcastReceived%20%27go%21%27%0Acomment%20%27receive%20mqtt%20message%27%0Aforever%20%7B%0A%20%20if%20%28%27MQTT%20connected%27%29%20%7B%0A%20%20%20%20event%20%3D%20%28%27last%20MQTT%20event%27%29%0A%20%20%20%20if%20%28isType%20event%20%27list%27%29%20%7B%0A%20%20%20%20%20%20sayIt%20%27topic%27%20%28%27MQTT%20event%20topic%27%20event%29%20%27%2C%20payload%27%20%28%27MQTT%20event%20payload%27%20event%29%0A%20%20%20%20%7D%0A%20%20%7D%20else%20%7B%0A%20%20%20%20sayIt%20%27try%20to%20connect%20...%27%0A%20%20%20%20waitMillis%20500%0A%20%20%20%20%27MQTT%20connect%20to%27%20%27mqtt.longan.link%27%20128%20%27MicroBlocks_client%27%20%27guest%27%20%27test%27%0A%20%20%7D%0A%7D%0A%7D%0A%0Ascript%20581%20120%20%7B%0Acomment%20%27publish%20topic%20payload%27%0A%27MQTT%20pub%27%20%27scratch%27%20%27Hello%21%27%0A%7D%0A%0Ascript%20403%20-168%20%7B%0Acomment%20%27work%20with%20https%3A%2F%2Fcreate.codelab.club%2Fprojects%2F22163%2Feditor%2F%27%0A%7D%0A%0A)


# 参考
*  [MQTT.js](https://github.com/mqttjs/MQTT.js): 提供 cli 工具
*  [mosquitto](https://github.com/eclipse/mosquitto)
*  [paho-mqtt](https://github.com/eclipse/paho.mqtt.python)
*  [gmqtt](https://github.com/wialon/gmqtt)