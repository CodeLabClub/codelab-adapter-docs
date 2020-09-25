# Adapter插件——让小猫来打开网站

<!--
所引用图片均以getstart开头
-->

在前一小节，我们介绍了Adapter的整体界面，现在我们开始使用Adapter去扩展创作平台的能力。

Adapter插件可以让创作平台拥有更多的能力，我们可以用创作平台让小猫自由的旋转，让小猫去追捕小鱼，那有没有想过 **让小猫去帮我们打开CodeLab的网站呢？** 接下来，我们来尝试点击小猫，让小猫为我们打开CodeLab网站。

让我们开始吧！

---

## 第一步：启用Python插件

首先，我们打开Adapter，并打开创作平台，然后在创作平台中，我们可以看到右上方的小球是绿色的，如果没有，请重启Adapter，再次打开Python插件。

接下来我们将Python扩展添加到创作平台中，点击左下角的添加扩展。

![getstart_pyproject3](/img/getstart_pyproject3.png)

在添加扩展页面找到并点击Python扩展

![getstart_pyproject4](/img/getstart_pyproject4.png)

到这里，第一步：添加Python扩展就完成了。

---

## 第二步：开始编程

<!-- 在介绍广播积木时，需要加个介绍广播积木的链接？ 帮助不理解该概念的使用者，去了解这一概念。-->

在这里我们将启用Python扩展，并且 **利用扩展将Codelab的主页和小猫连接起来。**

首先，让我们编程， **点击绿旗的时候，就启动Python扩展**。

![pyproject_start_extension1](/img/pyproject_start_extension1.gif)

随后我们将创造一个属于自己的积木，在创造一个积木时，我们先给积木取个名字，然后将我们想要赋予积木的功能拖到自定义积木的下方。

![pyproject_start_extension2](/img/pyproject_start_extension2.gif)

要赋予自定义积木打开网站的能力，只需要将 `PyHelper.open_url("https://codelab.club")` 复制并粘贴到python积木块中, 这样一来我们就赋予了自定义积木块打开Codelab网站的能力了。

![pyproject_pyblock](/img/pyproject_pyblock.png)

到这里好像可以结束了，可是我们的目标是让小猫来打开网站。接下来我们将积木的能力赋予给小猫。

![pyproject_start_extension3](/img/pyproject_start_extension3.gif)

---

## 第三步：让小猫来打开网站

到这里，我们已经将所有的工作做完了，现在我们将点击绿旗，再点击小猫。看看会发生什么？

![pyproject_start_extension4](/img/pyproject_start_extension4.gif)

如果在操作过程遇到困难，可以直接参考[项目源码](https://scratch3v3.codelab.club/?sb3url=https://adapter.codelab.club/sb3/pyproject1.sb3)

---

## 最后

到这里我们已经成功的让小猫帮我们打开网站了，有的小伙伴会说我能打开自己喜欢的网站吗？

当然可以，我们可以尝试将Python积木块中的网址替换一下？也许打开的就是你喜欢的网站了。

在这个项目中，我们做了非常简单的三件事情

1. 启动Adapter的Python插件(extension_python)
2. 创造了一个拥有打开网站能力的积木
3. 将打开网站的能力赋予给了小猫

接下来我们将继续扩展创作平台的能力，连接Microbit。
