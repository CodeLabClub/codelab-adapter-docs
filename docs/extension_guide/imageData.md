# Tutorial
用于获取和设置舞台区数据，具体而言:

*  获取当前舞台图像、当前视频图像
    *  这些数据的消费者包括:
        *  [extension_stage.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_stage.py)
        *  [node_physical_blocks2.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_physical_blocks2.py)
*  获取/设置当前角色的自定义造型

# demo
大多数的 physical blocks 项目都使用到了`获取当前视频图像`.

而以下项目使用到了`获取/设置当前角色的自定义造型`:

<video width=80% src="/video/1590665913541756.mp4" controls="controls"></video>

<video width=80% src="/video/1590665910081123.mp4" controls="controls"></video>

## 与 physical blocks 2.0 配合使用

![](/img/4d3435d3f92fb2d57d9dc301bd06fd40.png)

!!! 提醒
    如果你想切换分辨率，Adapter的版本需要`>=3.7.4`, 或者到插件市场下载最新的physical blocks 2.0插件。 此外值得注意的是，分辨率越高，刷新率越慢（很大原因是因为传输的数据大造成的）