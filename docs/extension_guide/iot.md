# MQTT 插件
MQTT broker 需要支持 wss(websockets) 协议, 才能在Scratch里连接它

CodeLab 提供一个broker: 

*  url: iot.codelab.club
*  默认用户名/密码: guest/test
*  tcp port: 1883
*  websockets port: 8084
*  websocket port: 8083

# Demo
## scratch client
[scratch demo](https://create.codelab.club/projects/9792/)

## python client
```py
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/scratch3_sub")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('guest', 'test')

client.connect("iot.codelab.club", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
```