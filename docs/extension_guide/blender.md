# Tutorial

### 安装依赖
我的环境是: `MacOS blender2.8`

```bash
cd /Applications/blender.app/Contents/Resources/2.80/python/bin
wget https://bootstrap.pypa.io/get-pip.py
./python3.7m ./get-pip.py --prefix /Applications/blender.app/Contents/Resources/2.80/python
./python3.7m pip3 install pyzmq
```

### 在blender中运行[blender_server](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/servers/blender_server.py)

在blender中运行[blender_server.py](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/servers/blender_server.py)

在blender2.79b中， 打开`Text Editor`，运行[blender_server.py](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/servers/blender_server.py)
 
![](http://wwj-fig-bed.just4fun.site/codelab-blender_7d110f45.png)

在blender2.8中,我喜欢打开`Scripting`标签页(使用Text Editor也可以), 运行[blender_server.py](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/servers/blender_server.py):
![](http://wwj-fig-bed.just4fun.site/codelab-blender_d397ea81.png)

### 在codelab-adapter运行[extension_blender.py](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/extension_blender.py)插件

<img src="http://wwj-fig-bed.just4fun.site/codelab-blender_984f1dc6.png" width=400 />

下载`https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/extension_blender.py`插件。

下载完成后，重启codelab-adapter.

### 开始使用
打开[scratch3.codelab.club](https://scratch3.codelab.club/)， 开始使用。

<video width=600px src="http://wwj-tmp-video.just4fun.site/blender.mp4" controls="controls"></video>

如果你在网页里没看到blender插件，请刷新浏览器缓存。

# todo
将[blender_server](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/servers/blender_server.py)写成blender插件。