# Tutorial

simple NLU 是一个简单的语义处理器，基于简单的规则匹配，可以做一些有趣的事情。

主要受到 Cozmo 社区[Cozmo-Voice-Commands](https://github.com/rizal72/Cozmo-Voice-Commands)项目的启发。

## Demo

以下是一些 demo:

### Robomaster

<video width=80% src="/video/1593410656522462.mp4" controls="controls"></video>

### Cozmo 学猫叫

<video width=80% src="/video/1593428681227193.mp4" controls="controls"></video>

## 插件说明

-   使用方式: 到[插件市场](/extension_guide/extension_market/)下载插件, 搜索 **NLU**
-   插件类型: [Adapter Extension](https://adapter.codelab.club/dev_guide/helloworld/)
-   插件源码: [extension_simple_NLU.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_simple_NLU.py)

## 依赖

{!utils/dependence.md!}

## 开始使用

我们以前头的 Cozmo 学猫叫项目为例，解释插件的使用。

NLU 是一个语义解析器，语言文本的输入，是任意的。你可以使用 Scratch 内置的语音输入；也可以使用 Siri。

如果你和视频 demo 一样，准备使用 Siri，需要先将 Siri 接入到 Adapter 中，参考[文档](https://adapter.codelab.club/extension_guide/siri/)。

## 步骤 1：打开 Codelab Adapter

{!utils/open_adapter.md!}

## 步骤 2：打开 Codelab Scratch

{!utils/open_scratch.md!}

![](/img/3a2539ceababd25a668c6c7de55c6f63.png)


加载[Scratch-simple-nlu-cozmo](https://scratch3v3.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-nlu-cozmo.sb3){target=\_blank}

!!! 提醒
    如果你加载遇到问题，可能需要先刷新浏览器缓存

点击绿旗，将运行相应的adapter插件。按下空格将运行示例输入: `cozmo 前进50毫米，然后吓跑他，接着右转90度，之后表演一下学猫叫`

如果一切正常，可以拿起你的Siri，控制Cozmo啦！

!!! 使用Scratch内置语音输入
    如果你不想使用Siri，也可以使用CodeLab Scratch内置的语音输入， 以下是案例：[Scratch-nlu-cozmo-with-Scratch-input](https://scratch3v3.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-nlu-cozmo-with-Scratch-input.sb3){target=\_blank}。按下 `a`按键,开始语音输入(默认5秒，你可以自己调节输入时长)

# 进阶

如果你想构建更强大的语义引擎，可以使用[wit.ai](https://wit.ai/)、[api.ai](http://api.ai/)

当然你也可以使用等开源项目[rasa](https://rasa.com/)自行构建，中文用户推荐[Rasa_NLU_Chi](https://github.com/crownpku/Rasa_NLU_Chi)
