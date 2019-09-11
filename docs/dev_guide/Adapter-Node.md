# Adapter Node
在上一节:[hello world](/dev_guide/helloworld/)中我们学会了如何自定义一个extension。

extension有如下的限制:

1.  必须放置在插件目录中（`~/codelab_adapter/extensions`）。
2.  只能使用CodeLab Adapter[已打包的第三方库](https://github.com/Scratch3Lab/codelab_adapter_extensions/wiki)

如果你想使用Python社区海量的第三方库: 诸如[pygame](https://github.com/pygame/pygame)、[numpy](https://github.com/numpy/numpy)、[opencv](https://github.com/opencv/opencv)、[tensorflow](https://github.com/tensorflow/tensorflow), extension就办不到了，但Adapter Node可以！

我们希望CodeLab Adapter专注于连接万物，所以构建了Adapter Node，允许你在任何地方创建CodeLab Adapter的扩展，允许你使用任何Python库，无论你准备构建游戏、构建网站、构建深度学习应用还是构建一个机器人！

## Adapter Node是什么
Adapter Node只是普通的Python程序，继承自[AdapterNode](https://github.com/Scratch3Lab/codelab_adapter_client_python/blob/master/codelab_adapter_client/base.py#L174)。别害怕，它很简单的。

## 第一个Adapter Node
我们开始写第一个Adapter Node。

你需要完成这些前置工作:

*  安装了Python3(`>=3.6`)
*  pip3 install codelab_adapter_client

接着可以随便在什么地方创建一个python文件,随便给它起个名字，诸如`my_first_adapter_node.py`:

我们让这个Node的功能与[hello world](/dev_guide/helloworld/)里我们自定义的插件功能相同：反转字符串

```python
import time
from loguru import logger
from codelab_adapter_client import AdapterNode


class EIMNode(AdapterNode):
    def __init__(self):
        super().__init__()
        self.EXTENSION_ID = "eim"

    def send_message_to_scratch(self, content):
        message = self.message_template()
        message["payload"]["content"] = content
        self.publish(message)

    def extension_message_handle(self, topic, payload):
        self.logger.info(f'the message payload from scratch: {payload}')
        content = payload["content"]
        if type(content) == str:
            content_send_to_scratch = content[::-1]  # 反转字符串
            self.send_message_to_scratch(content_send_to_scratch)

    def run(self):
        while self._running:
            time.sleep(1)


if __name__ == "__main__":
    try:
        node = EIMNode()
        node.receive_loop_as_thread()
        node.run()
    except KeyboardInterrupt:
        node.terminate()  # Clean up before exiting.
```

## 运行
打开CodeLab Adapter（不需要选择插件），将CodeLab Adapter作为消息中心。

运行my_first_adapter_node.py: `python3 my_first_adapter_node.py`

让我们在[CodeLab Scratch3](https://scratch3v2.codelab.club/)中尝试一下反转字符串:

<img width="800px" src="../../img/v2/helloworld_extension.png"/>

成功！

它只是普通的Python程序，使用你本地的Python环境，所以你现在可以使用[pygame](https://github.com/pygame/pygame)、[numpy](https://github.com/numpy/numpy)、[opencv](https://github.com/opencv/opencv)、[tensorflow](https://github.com/tensorflow/tensorflow)来增强Scratch3啦！


## 想象空间
如果你希望构建分布式的应用，诸如构建密室逃脱中的各种机关。只需要[做一下配置就行](https://adapterv2.codelab.club/user_guide/settings/#open_message_hub), 让CodeLab Adapter接受分布式的请求。

你可以将Adapter Node跑在任何地方，来增强CodeLab Adapter的能力，无论是本地、云端还是分布式节点。

我们也正在构建其他语言的client，你不会被限制在Python中，而是可以在任何编程语言任何平台上构建Adapter Node。 参考:[编程语言支持](/dev_guide/multi-language-support/)

## 更多例子
*  [blender](/extension_guide/blender/): 这是个实际的案例，演示如何使用AdapterNode基础类粘合不同软件，将其变为Adapter Node。
*  [examples](https://github.com/Scratch3Lab/codelab_adapter_client_python/tree/master/examples)
*  [servers_v2](https://github.com/Scratch3Lab/codelab_adapter_extensions/tree/master/servers_v2)