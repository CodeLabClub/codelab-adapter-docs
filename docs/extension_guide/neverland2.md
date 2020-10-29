# Neverland 2.0


[demo3](https://scratch-beta.codelab.club?sb3url=https://adapter.codelab.club/sb3/neverland2-demo3.sb3)

<video src="/video/1601261973458887.mp4" controls="controls"></video>


# 原理
<!--拓扑图
![]()
-->

项目包含以下部分:

*  adapter master: 空间主节点，以`NEVERLAND_HUB`模式运行的Adapter,运行在树莓派上
*  adapter node(makey node): 空间功能节点，运行在树莓派上
*  user client: 运行在用户计算机上的 Adapter

## adapter master
`ADAPTER_MODE=3 ./codelab-adapter`

关于 [Adapter 的模式](https://adapter.codelab.club/user_guide/settings/#adapter_mode)

## adapter node
`python3 makey_node.py`

## user client
正常运行Adapter即可