# Squeak/Smalltalk

## 介绍

![](/img/balloon-squeak.svg)

[Squeak](http://squeak.org/) 是 Smalltalk 的现代实现.

有几位 Smalltalk-80 的实现者(他们之前在施乐实验室创造了 Smalltalk)都参与到了 Squeak 中，包括 Alan Kay 和 Daniel Ingall，这个项目依然在持续演进，他们抱有跟今天计算机整个领域不同的愿景。

MIT媒体实验室推动的OLPC计划，采用Squeak作为开发环境。

Etoys、Croquet、第一代的Scratch都是用 Squeak 实现的。

关于 Squeak 入门，可参考[Smalltalk 入门导览](https://wwj718.github.io/post/%E7%BC%96%E7%A8%8B/smalltalk-guide/)

## 接入 Adapter
有很多种方式将 Squeak 和 Adapter连在一起，诸如HTTP、Websocket、ZeroMQ，系统调用(Adapter python client提供系统命令)，你也可以自己写一个Adapter插件来连接两者。

目前我最喜欢的一种方式是使用 [OSC](/extension_guide/osc/), 由于最新的Adapter内置了 OSC server，所以我们可以轻松将Squeak用作 osc cleint， 消息流向是 `Squeak->Adapter`。

## demo

在Squeak中, 下载 OSC : [OSC-SimonHolland](http://www.squeaksource.com/OSCClient/OSC-SimonHolland.14.mcz), 之后拖到 Squeak 桌面，加载使用即可。

```smalltalk
(OSCMessage for: {'/eim/osc' . 1}) sendTo: #[127 0 0 1] port: 12361.  "turn right"

(OSCMessage for: {'/eim/osc' . 0}) sendTo: #[127 0 0 1] port: 12361. "forward"

(OSCMessage for: {'/eim/osc' . -1}) sendTo: #[127 0 0 1] port: 12361.  "turn right"
```

以上的代码将控制Scratch里的飞行器:

[squeak-scratch-demo](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/squeak-scratch-demo.sb3)

<video width=80% src="/video/smalltalk-scratch.mp4#t=0.001" controls="controls"></video>


## 进阶
你也可以在Squeak中运行 OSC server，此时消息流向是 `Adapter -> Squeak`

以上代码也可以运行在其他smalltalk方言中，诸如 Pharo。

# 参考
*  [squeak osc](http://wiki.squeak.org/squeak/5836)