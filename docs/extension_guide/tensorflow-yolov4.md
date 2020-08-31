# Tutorial
[tensorflow-yolov4](https://github.com/hhk7734/tensorflow-yolov4)， 请参考文档，安装响应依赖。


接入方法参考[使用4 行 Pyhon 代码扩展 Scratch](https://blog.just4fun.site/post/%E5%B0%91%E5%84%BF%E7%BC%96%E7%A8%8B/4-line-python-code-as-scratch-ext/)

使用前请将[coco.names](https://github.com/hhk7734/tensorflow-yolov4/tree/master/test/dataset) 和 [yolov4-tiny.weights](https://drive.google.com/file/d/1GJwGiR7rizY_19c_czuLN8p31BwkhWY5/view?usp=sharing) 下载到对应目录。

```python
from codelab_adapter_client.utils import run_monitor, save_base64_to_image
from yolov4.tf import YOLOv4
import cv2
import cv2
import numpy as np

yolo = YOLOv4(tiny=True)

yolo.classes = "/tmp/coco.names"

yolo.make_model()
yolo.load_weights("/tmp/yolov4-tiny.weights", weights_type="yolo")

def monitor(msg):
    filename = save_base64_to_image(msg, "/tmp/tmp_img")
    original_image = cv2.imread(filename)
    resized_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    resized_image = yolo.resize_image(resized_image)
    resized_image = resized_image / 255
    input_data = resized_image[np.newaxis, ...].astype(np.float32)
    candidates = yolo.model.predict(input_data)
    print(candidates)
    # yolo.inference(media_path=filename)

run_monitor(monitor)
```