# Tutorial
![](https://raw.githubusercontent.com/JaidedAI/EasyOCR/master/examples/example2.png)

支持70多种语言的开箱可用OCR，包括中文，日文，韩文和泰文...

[EasyOCR](https://github.com/JaidedAI/EasyOCR)的一层薄薄包装，将 EasyOCR 的能力引入 Scratch


# 使用
运行 CodeLab Adapter。

![](/img/ddd063082e3ef5ebb89d868217e327a8.png)

在 Adapter [Jupyterlab 安装第三方库](https://adapter.codelab.club/extension_guide/jupyterlab/#_4) easyocr: `import pip; pip.main(['install', 'easyocr'])`


运行以下程序:

```python
from codelab_adapter_client.utils import run_monitor, save_base64_to_image
import easyocr

reader = easyocr.Reader(['ch_sim','en'], gpu = True) # need to run only once to load model into memory

def monitor(msg):
    filename = save_base64_to_image(msg, "tmp_img")
    result = reader.readtext(filename, detail = 0)
    if result:
        return str(result)

run_monitor(monitor)
```

对以上机制不熟悉的朋友可以参考 [Python对象的连接器：EIM 插件](/project_tutorial/eim_pt/)

打开 [测试项目](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-EasyOCR.sb3)

由于 easyocr 的计算发生在本地，且基于神经网络，所以处理时间比较久， 处理后的结果将返回到`收到的消息`

# 总结
这个例子展示了，使用 CodeLab Adapter 可以轻松将 AI 能力接入Scratch