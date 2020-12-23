# Tutorial

![](/img/6f6fc565cbcff4105784b448c628c307.png)

!!!提醒
    Aqara 是实验性插件，未来可能移除。如果你比较依赖于它，建议自行维护Adapter Node，直接与Aqara云通信，这是一个例子: [extension_Aqara_scene.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_Aqara_scene.py)。 我们准备长期支持的项目是 Longan hub 、 Home Assistant 和 WebThings

## 介绍

Aqara(绿米)智能家居用户可在 CodeLab 创作平台上对智能设备进行编程，让孩子将智能家庭改造为魔法世界吧！

# Demo

<video width=50% src="/video/wand.mp4" controls="controls"></video>

更多好玩的演示 参考: [CodeLab projects](https://www.codelab.club/projects/)

# 使用
!!! 提醒
    目前只支持 Aqara 网关，不支持小米网关。

### 获取 token

点击`打开绿米授权`积木，将打开登陆页面，使用 Aqara 账号登陆后，将获得一个token。

### 连接到云
之后将token复制到 **连接** 积木里, 运行它即可。

![](/img/d9aefea95691b05581de0c8382168af4.png)

### hello world
构建一个入门程序: 当小猫被点击时，将灯泡打开

![](/img/ca0019da61b7c540b340665bed5c0c5e.png)

# 扩展性
使用 `场景` 积木，可以调用 Aqara APP 里定义的任何场景！ 如果你发现某些设备没有被积木化，可以通过把它纳入场景中，之后通过场景积木调用它！
