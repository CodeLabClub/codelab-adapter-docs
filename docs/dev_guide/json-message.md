# json message

在 [hello world](/dev_guide/helloworld/) 案例中，我们构建了这样一个程序：接收一个来自 Scratch3 的字符串（`hello world`），将其反转后（`dlrow olleh`）返回。

有时候字符串是不够用的，如果我们从 Scratch3 往 CodeLab Adapter extension 传递更复杂的数据结构怎么办呢？

有两种办法：

1. 自定义 Scratch3 extension，拓展 payload 结构：[payload](https://github.com/CodeLabClub/scratch3_eim/blob/9716545108fca06f08fcfbf26456a97f3092dd20/index.js#L292)
2. 使用 Scratch3 EIM extension，传递 json 消息。

第二种方式非常简单，不必去碰 Scratch 的东西，只要使用 Python 写 extension 就行，我们在此讨论这种方式。

## 传递 x、y 坐标
设想这样一种应用场景：我们希望使用 Scratch 控制机器人（如 Cozmo）移动到特定的坐标位置`(x,y)`。

我们可以通过以下两个步骤完成：

1.  在 Scratch3 中自定义新的积木
    *  使用 Scratch3 json extension 构建 json 数据
    *  使用 Scratch3 EIM extension 传递消息到 CodeLab Adapter
2.  构建 CodeLab Adapter 插件：`extension_robot_xy.py`，在插件中处理传递过来的`(x,y)`

## 在 Scratch3 中自定义新的积木
<img width="800px" src="/img/v2/robotxy_scratch3.png"/>


## 构建 CodeLab Adapter 插件
```python
import time
from codelab_adapter.core_extension import Extension


class RobotXYExtension(Extension):
    NODE_ID = "eim/robot"
    s
    def __init__(self):
        super().__init__()

    def extension_message_handle(self, topic, payload):
        self.logger.debug(f'the message payload from scratch: {payload}')
        content = payload["content"]
        if type(content) == dict:
            x = content["x"]
            y = content["y"]
            self.logger.info(f'x:{x}; y:{y}')

    def run(self):
        while self._running:
            time.sleep(1)

export = RobotXYExtension
```

在此，值得注意的是`self.NODE_ID = "eim/robot"`，观察前头的截图，可以看出`"eim/robot"`与 Scratch3 eim 的积木块的对应关系。

## 开始测试
如果你对如何运行 CodeLab Adapter extension 不熟悉，请参考 [hello world](/dev_guide/helloworld/)。

<img width="800px" src="/img/v2/robot_xy.png"/>


## json message from CodeLab Adapter to Scratch3
前头我们学会了如何将 json 消息从 Scratch3 发往 CodeLab Adapter，接下来我们学习如何将 json 消息从 CodeLab Adapter 发往 Scratch3。

我们来设计这样一个 CodeLab Adapter extension：每秒钟将一个随机的 (x,y) 发往 Scratch3，使用 (x,y) 来控制小猫的位置。

我们来修改 `extension_robot_xy.py`


```python
import time
import random
from codelab_adapter.core_extension import Extension


class RobotXYExtension(Extension):
    NODE_ID = "eim/robot"

    def __init__(self):
        super().__init__()

    def extension_message_handle(self, topic, payload):
        self.logger.debug(f'the message payload from scratch: {payload}')
        content = payload["content"]
        if type(content) == dict:
            x = content["x"]
            y = content["y"]
            self.logger.info(f'x:{x}; y:{y}')

    def run(self):
        while self._running:
            message = self.message_template()
            random_x = random.randint(-240,240)
            random_y = random.randint(-180,180)
            message["payload"]["content"] = {"x":random_x, "y":random_y}
            self.publish(message)
            time.sleep(1)

export = RobotXYExtension
```

重新勾选`extension_robot_xy`插件，现在你可以在 Scratch 中收到 CodeLab Adapte 传过来的 json 数据了！


<img width="800px" src="/img/v2/randomxy_scratch.png"/>

在 Scratch 一侧，使用 json 拓展来解析传递过来的消息。

## 提醒
如果不是必要，尽量使用字符串消息。

Scratch 内部的消息就只支持字符串，这是一种很好的设计，因为它简单易理解。
