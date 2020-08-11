# Tutorial

NetworkZero 的目标是让局域网通信变得简单。

基于[networkzero](https://github.com/tjguk/networkzero/)包装，保留与其一致的接口

!!! 注意
    如果你无法在两台局域网电脑之间通信，可能需要关闭电脑的系统防火墙

# demo

收信人:  **地址** (地址名)，并 **接收** 来自这个地址的消息。
![](/img/16f959a43d2d3a24f60867f4ec55e8e9.png)


寄信人: 往 **目标地址** 发送 **信息**

![](/img/94e1e931cdd968e13f77169592956eb2.png)

允许任何人公布通信地址，所以可以轻松构建网状结构。

# 典型应用场景
*  局域网联机游戏
*  局域网聊天
*  多人联机控制机器人
*  与Python程序(诸如树莓派机器人)互动
    *  可与 基于[networkzero](https://github.com/tjguk/networkzero/)的程序互操作。