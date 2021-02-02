# Sugar

![](/img/sugar_bar.jpeg)

构建 Sugar 插件的动机最初来自 @Lounsen 的想法: 接布尔量的 hat 积木。

Sugar 插件是个实验室，试图为 Scratch 提供 **甜** 的语法糖。

新的想法/需求，欢迎在[这个帖子](https://discuss.codelab.club/t/topic/169)下讨论

# 积木介绍

## 接布尔量的 hat 积木
当情况**发生变化**，并且满足添加，才触发。类似 **当角色被点击** 积木。

-   [Demo](https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/Scratch-when-true.sb3)

<!--除非情况发生变化，否则只触发 **一次** .-->

上述例子，表达的是: 如果 **我的变量** 一直 **<** 50，只向前移动一次.

使用hat积木我们可以构造出与 Scratch 原生事件积木类似的东西:

![](/img/be0f690d69bb72e95916eb2fdc722839.png)

### 与linda积木配合使用
![](/img/hat-linda.png)

hat 积木中只应包含 Scratch 原生积木，最好不要放入扩展积木。

可能引起异常的原因还在进一步调查中。

## Color积木
参考 [Computer Colors](https://en.scratch-wiki.info/wiki/Computer_Colors)