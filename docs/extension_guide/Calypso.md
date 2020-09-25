# Tutorial

![](/img/5e2d27904616c6f685c439d933fa2ced.png)

[Calypso](https://calypso.software/) 是 CMU 大学七年来对儿童如何学习基于规则的机器人编程的研究成果。由[David S. Touretzky](https://en.wikipedia.org/wiki/David_S._Touretzky)博士构建，他是 CMU 计算机科学和神经认知基础中心的研究教授。此外，Touretzky 一直活跃在互联网，主张言论自由。

[Calypso](https://calypso.software/)目前用于为 Cozmo 编程。被广泛用于 AI 教育项目.

<!--
# 插件说明

-   使用方式: 到[插件市场](/extension_guide/extension_market/)下载插件, 搜索 **mqtt**
-   插件类型: [Adapter Extension](https://adapter.codelab.club/dev_guide/helloworld/)
-   插件源码: [extension_calypso.py](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extensions_v3/extension_calypso.py)
-->

# Demo

<video src="/video/1588994952631075.mp4" controls="controls"></video>

当 Cozmo 看到我表情悲伤时，将帮我升起窗帘: "Give you some sunshine"

相关代码:

在 [Calypso](https://calypso.software/) 中:

![](/img/7f624134740a9c3db0aa2b42bcc8af2b.png)

源文件: [give-you-sunshine.calypso](/sb3/give-you-sunshine.calypso), 关键部分是 当 cozmo 说`message sad` 时, sad 消息将被发送到 Scratch EIM 插件里。

实际上只要 Cozmo 说的话形如 `message xxx`, xxx 消息都将被发送到 Scratch EIM 插件里。

想法最初来自 @jinlei 提到的圣经里关于 `powerful word` 的段落。

--

在 Scratch 中:

![](/img/09f4119ebb7e35375af5075a0138ef82.png)

源文件: [Scratch-calypso](https://scratch3v3.codelab.club?sb3url=https://adapter.codelab.club/sb3/Scratch-calypso_new.sb3)

# 参考

-   [calypso.software](https://calypso.software/)
-   [使用 Calypso 的世界 AI 青年比赛（WAICY）](https://calypso.software/blogs/news/world-ai-competition-for-youth-waicy-using-calypso)
    -   [Reading, Writing, 'Rithmetic ... and Now, Robotics](https://www.cmu.edu/news/stories/archives/2018/august/youth-ai-competition.html)
-   [AI4All 学生使用 Calypso 进行 AI 入门](https://calypso.software/blogs/news/ai4all-students-get-hands-on-intro-to-ai-using-calypso) 介绍了人工智能主题（计算机视觉，路径规划，文本到语音等）
-   [ReadyAI 现在提供 Calypso 的机构许可证](https://calypso.software/blogs/news/readyai-is-now-facilitating-institutional-licensing-of-calypso): 在学校，外展计划和计算机营中使用 Calypso
-   [Activity: Cozmo's Shack](https://www.cs.cmu.edu/~dst/Calypso/Curriculum/NewBrighton/Shack/)
