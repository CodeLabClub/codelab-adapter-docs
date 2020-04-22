# Extension Market

CodeLab Adapter 3.0 有一个统一的插件市场，可以方便下载到新的插件，就像我们在 vscode 或 sublime text 里的体验的那种插件系统，有个体面的 UI，而不是使用 curl 或者 wget 去 github 里手动下载。

![](/img/4c48b29253b1923ce61ba104e5ef21fa.png)

作为演示我们下载了插件市场里的一个番茄工作法插件，这个插件的功能很简单(源码也是公开的): 每 25 分钟提醒编程者起来看看窗外风景。

![](/img/06be05f915263f36d4663074d6147cb5.png)

下载完成之后，不需要重启软件，即可在 Scratch 和 Web UI 中看到新下载的插件，点击运行它：每 25 分钟，你就会收到一条信息提示你做个短途休息。

![](/img/b6d455988e421b05e1aa9eb593957c6a.png)

### 提交自定义插件到插件市场

只需要将你自定义的 [Adapter Extension](/dev_guide/helloworld/) 或者 [Adapter Node](/dev_guide/Adapter-Node/) 提交到[codelab_adapter_extensions](https://github.com/CodeLabClub/codelab_adapter_extensions), 提交合并之后，它将出现在插件市场中。

!!!提醒
    3.0.0 插件市场仅支持 Adapter Extension，3.1.0 版本增加了对 Adapter Node 的支持。Adapter Node 脚本可以托管在互联网的任何位置。

这是目前所有可用的插件都在：[codelab_adapter_extensions](https://github.com/CodeLabClub/codelab_adapter_extensions)。源码以 GPL 协议开放。研究与学习可以随意使用它。

codelab.club 内部在使用的一些插件近期也在整理源码，将陆续开放出来。欢迎大家一起改进它们。

你可以用这些插件将 Scratch 3.0/blockly:

-   接入 Python kernel
-   接入四轴飞行器
-   接入 Cozmo/Vector
-   接入任何用 Python 写的 AI 程序
-   接入眼动仪
-   接入 Minecraft
-   接入 blender
-   ……

<!--
以下是插件列表

*  [extension_android.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_android.py)
*  [extension_blender.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_blender.py)
*  [extension_chatterbot.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_chatterbot.py)
*  [extension_cozmo.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_cozmo.py)
*  [extension_demo.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_demo.py)
*  [extension_eim.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_eim.py)
*  [extension_eim_http.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_eim_http.py)
*  [extension_eim_monitor.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_eim_monitor.py)
*  [extension_eim_script.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_eim_script.py)
*  [extension_facial_landmarks.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_facial_landmarks.py)
*  [extension_fly.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_fly.py)
*  [extension_helloworld.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_helloworld.py)
*  [extension_home_assistant.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_home_assistant.py)
*  [extension_hungry_robot.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_hungry_robot.py)
*  [extension_microbit.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_microbit.py)
*  [extension_minecraft.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_minecraft.py)
*  [extension_mpython.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_mpython.py)
*  [extension_mxcar.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_mxcar.py)
*  [extension_opencv.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_opencv.py)
*  [extension_presentation.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_presentation.py)
*  [extension_python_kernel.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_python_kernel.py)
*  [extension_switch_joycon.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_switch_joycon.py)
*  [extension_tensorflow.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_tensorflow.py)
*  [extension_third_party_library.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_third_party_library.py)
*  [extension_tulingbot.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_tulingbot.py)
*  [extension_ubtrobot.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_ubtrobot.py)
*  [extension_vector.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_vector.py)
*  [extension_wechat.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_wechat.py)
-->
