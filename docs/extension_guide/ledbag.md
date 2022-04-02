# LedBag

## 介绍
![](/img/4a2c14f97a6a25c20a2e401305a0fb77.png)

可编程书包（也兼容可编程相框、音响...）

### demo
<video width=80% src="https://adapter.codelab.club/video/f4d76c09adbf9175727b943fc38a6b.MP4#t=0.001" controls="controls"></video>

<video width=80% src="https://adapter.codelab.club/video/04142c1c7f22ab2b4d0820eef22c93.MP4#t=0.001" controls="controls"></video>

<video width=80% src="https://adapter.codelab.club/video/9563d376e264a35d051f2d1ae6ca03.MP4#t=0.001" controls="controls"></video>


## hello world
```python
from codelab_adapter.led_bag import LedBag
bag = LedBag()
bag.connect()  #  默认连接 jupyterlab 模拟器，输入书包id可连接到书包: bag.connect(DEVICE_ID)
# 点亮第一个led
bag.set_pixel(0, 0, 'red') # bag.set_pixel(0, 0, (255,0,0))
```

### LedBag API
可以在 Adapter notebooks 里的 `hello_LedBag.ipynb` 做实验

#### 控制像素
```python
color = (255, 0, 0)
# 设置像素
bag.set_pixel(0, 0, color)
# 查询像素, renturn RGB tuple
bag.get_pixel(0, 0)
```

![](/img/07609aadfd5b5e04a8b3a78e2fd9c9b6.png)

#### 清理画布
```python
bag.clear()
```

#### show
```python
bag.show()
```


#### 全屏颜色
```python
color = (255, 0, 0) # red (RGB), 通过调整 RGB 的数值调整亮度
bag.set_color(color)
```

#### 显示字符
```python
# 显示 emoji 字符
bag.display_emoji('🐳')
# 英文字符
bag.display_text('hello world')
# 中文字符串
bag.display_text_zh('早上好', color=(255,0,0))
# 显示中文字符
bag.display_char_zh('早', color=(255,0,0))
```

#### 硬件特殊功能
```python
# 内置效果
bag.show_visualization(1)  # 参数: 特效 ID
# 记分板
bag.show_scoreboard(3, 2)
# 显示时钟
bag.show_clock()
# show design
bag.show_design()
```

#### 保存、加载图片
```python
# 保存当前图像
bag.save(name="test")

# 加载图像(自动转为16x16格式)
bag.load('test.png')
```

#### 断开蓝牙
```python
bag.close()
```

### 动画(Animation) API
```python
from codelab_adapter.led_bag import Animation
animation = Animation()

# bag set pixel ...  
animation.add_frame(bag) # 把 bag 当前状态(bag._img)作为 animation 的一帧
# bag set pixel ... 
animation.add_frame(bag)


# 在模拟器里展示动画
animation.show(duration=0.1)

# 将动画同步到书包
animation.show(to_bag=bag)

# 保存为gif
animation.save(name='hello')


# 加载 gif, 建议使用手机 APP 设计动图。 也可参看动图网站 https://giphy.com/，或者试试表情包
animation.load('./hello.gif')

# 查看、修改某一帧
animation.show_frame(FRAME_ID)
animation.remove_frame(FRAME_ID)

```

## 积木说明

需要先下载插件: [node_ledbag.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_ledbag.py)

[Scratch Demo](https://create.codelab.club/projects/16313/editor/)


## 进阶

### 游戏平台
与像素交互

```python
# import pynput
import time
from codelab_adapter.led_bag import LedBag
import ipywidgets as widgets
from IPython.display import display

bag = LedBag() # 
bag.connect()

block_location = (0, 0)

button_up = widgets.Button(description="上")
button_down = widgets.Button(description="下")
button_left = widgets.Button(description="左")
button_right = widgets.Button(description="右")

output = widgets.Output()
vbox = widgets.VBox([button_up, button_down])
hbox = widgets.HBox([button_left, vbox, button_right])
display(hbox, output)

def move(direction):
        global block_location
        bag.clear()
        if direction == "上":
            x, y = block_location
            block_location = (max(x-1, 0), y)
            bag.set_pixel(block_location[0], block_location[1], 'red')
        if direction == "下":
            x, y = block_location
            block_location = (min(x+1, 15), y)
            bag.set_pixel(block_location[0], block_location[1], 'red')
        if direction == "左":
            x, y = block_location
            block_location = (x, max(y-1, 0))
            bag.set_pixel(block_location[0], block_location[1], 'red')
        if direction == "右":
            x, y = block_location
            block_location = (x, min(y+1, 15))
            bag.set_pixel(block_location[0], block_location[1], 'red')

def on_button_clicked(b):
    global block_location
    with output:
        move(b.description)
    
button_up.on_click(on_button_clicked)
button_down.on_click(on_button_clicked)
button_left.on_click(on_button_clicked)
button_right.on_click(on_button_clicked)
```

连接游戏手柄: ...

<!--
# gamepad
x = widgets.Controller()  # 不成熟， 使用 pygame

latest_press = 0
def on_controller_event(change):
    global latest_press
    for button_index, button in enumerate(change['owner'].buttons):
        if button.value==1 and latest_press != button_index:
          with output:  
            # print(button_index, button)
            if button_index == 13:
                move('下')
                latest_press = button_index
            elif button_index == 12:
                move('上')
                latest_press = button_index
            elif button_index == 15:
                move('右')
                latest_press = button_index
            elif button_index == 14:
                move('左')
                latest_press = button_index
            else:
                pass
        
            
x.observe(on_controller_event)
display(x)
-->

<!--
# kayboard
from pynput.keyboard import Key, Listener

def on_press(key):
    print(f'{key} pressed')

# Collect events until released
with Listener(on_press=on_press,) as listener:
    listener.join()
-->

## FAQ
### 发现设备
```python
import nest_asyncio
nest_asyncio.apply() 
import bluetooth
result = bluetooth.discover_devices(lookup_names=True)
print(result)
```

### OverflowError 
!!!提醒
    4.9.6 以上版本没有这个问题

一张图片最多包含 62 种颜色。

如果你想让每个像素随机变化，可使用以下代码:

```python
import random
from codelab_adapter.led_bag import LedBag
bag = LedBag()
bag.connect('xxx')

bag.clear()
color_set = set()  # 颜色集合（不重复）

while len(color_set) <= 62:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    if color not in color_set:
        color_set.add(color)

for i in range(16):
    for j in range(16):
        bag.set_pixel(i,j, random.choice(list(color_set)))
```

### 如何工作

## 参考
