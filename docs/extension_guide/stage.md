# Tutorial

Stage 指 Scratch 的舞台区。

![](/img/307a089f4fc36348702fe4d98958ce30.png)

Adapter Stage 插件允许将舞台区的图像（舞台或者摄像头图像）以 base64 的格式发往 Adapter，你可以使用 Adapter node/extension 自定构建图像处理程序，诸如使用 神经网络 或 OpenCV，将识别的结果返回给 Scratch。

当然，你也可以构建一个自动保存舞台状态的插件，或者自拍/美颜插件：）

需要配合 Scratch `图像识别`插件中的积木使用。

![](/img/999e46633d51f05d58c863c698fcb109.png)

!!! 提醒
在 Adapter 3.2 之前，你需要自行从[插件市场](/extension_guide/extension_market/s)里下载 Stage 插件。 [源码地址](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_stage.py)

运行 Stage 插件（当前插件的功能是把图像保存到 [Adapter Home 目录](https://adapter.codelab.club/user_guide/FAQ/#adapter)）,你可以通过修改插件做其他事情。

如果你想使用 OpenCV 或 Tensorflow 处理图像，需要自定义[Adapter Node](/dev_guide/Adapter-Node/)

## Demo
[stage image](https://scratch3v3.codelab.club/player.html?sb3url=https://adapter.codelab.club/sb3/stage_image.sb3)
