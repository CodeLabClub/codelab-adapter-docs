# 乐器演奏 ( Teachable Machine)

**AI**、**Teachable Machine**、**CodeLab Adapter**、**Scratch**

## 步骤 1：构建

### 是什么?

<video width="80%" src="/video/tm_scratch_dy.mp4" controls="controls"></video>

!!! tips
    国内用户可能需要科学上网，才能访问[Teachable Machine](https://teachablemachine.withgoogle.com/) :)  
    记得避免全局翻墙，否则浏览器可能无法连接到CodeLab Adapter  
    (我们所面临的困难许多时候是人为的)

使用 [Teachable Machine](https://teachablemachine.withgoogle.com/) 训练一个 AI 助手，教会它认识不同的乐器卡片(可任选)，当看到吉他 (guitar) 卡片时，在桌子上播放吉他动画，并使用吉他演奏一段音乐；当看到萨克斯 (sax)卡片时，在桌子上播放萨克斯动画，并使用萨克斯演奏一段音乐，

利用投影让虚拟形象和实物在一张桌子上互动！

### 它是如何工作的?

-   使用 [Teachable Machine](https://teachablemachine.withgoogle.com/) 中的 [Image Project](https://teachablemachine.withgoogle.com/train/image) ，训练 AI 来识别看书与合上书的不同状态。
-   使用 [CodeLab Adapter](/) 将 Teachable Machine 的识别结果接入到 CodeLab Scratch 中
-   使用 CodeLab Scratch（[在线版](http://scratch3v2.codelab.club/){target=\_blank}、[离线版](https://www.codelab.club/blog/codelab-download/){target=\_blank}皆可）进行编程，让卡通形象、音乐与实物互动。

### 你需要准备些什么

-   CodeLab Scratch
-   [CodeLab Adapter](/)
-   安装 Chrome 浏览器插件: [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)
    -  点击安装 Tampermonkey 脚本 [Teachablemachine_Result.user.js](https://gist.github.com/wwj718/78402d0de9efb8d33742c8770056489c/raw/1269fef28877f4c7625a4dd21990271fdf04cfe8/Teachablemachine_Result_fixed.user.js), 使用它来获取 [Teachable Machine](https://teachablemachine.withgoogle.com/) 的识别结果
-   投影仪(我使用的是 [LG PH450UG-GL 超短焦投影仪](https://item.jd.com/4245251.html))
    -  投影仪是可选的，你也可以让动画显示在电脑屏幕上，而不是投影到桌面。记得在屏幕上将舞台最大化，效果比较好。

## 步骤 2：编程

### 准备工作
安装完 [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo) Chrome浏览器插件和 [Teachablemachine_Result.user.js](https://gist.github.com/wwj718/78402d0de9efb8d33742c8770056489c/raw/1269fef28877f4c7625a4dd21990271fdf04cfe8/Teachablemachine_Result_fixed.user.js) 脚本后，运行下载到本地的 [CodeLab Adapter](/)。

打开[Image Project](https://teachablemachine.withgoogle.com/train/image)，页面应该会弹出提示: **connected!** , 表示已经将 Teachable Machine 接入 CodeLab Adapter。

接下来，可以开始你的 Teachable Machine 之旅途。 我们来展示一个例子。

### 训练模型
在 Teachable Machine 训练你的AI助手，你需要教会它识别不同卡片，如果你对 Teachable Machine 不了解，参考我们的介绍文章[CodeLab Adapter 接入 Teachable Machine](https://www.codelab.club/blog/adapter-teachable-machine/)。

建立3个分类，分别是 **guitar**、**sax**、**none** (空桌面)

开始添加你的训练样本，完成训练后在页面右边测试它。

如果不满意，可以添加调整样本数据，重新训练，并再次测试它，直到满意为止。

![](/img/tm_demo.png)

### 开始在CodeLab Scratch中编程

![](/img/669e65e3fa62e4f184a5af8568476bad.png)

!!! 在线版与离线版打开方式
    如果你是要在线版，直接[点击项目链接](https://scratch3v2.codelab.club/?sb3url=https://adapter.codelab.club/sb3/tm乐器演奏.sb3)即可。未来我们会直接发布到社区里。  
    如果你使用离线版，则下载[源码文件](/sb3/tm乐器演奏.sb3)，使用 CodeLab Scratch 加载它即可.  

点击绿旗开始运行程序，将 Scratch 舞台区最大化。

如果你使用投影仪，在黑暗中效果比较好。

黑暗中如何看得见乐器卡片呢？将乐器卡片放在舞台去右上角，参考演示视频里的做法。

## 步骤 3：发挥想象
这儿的核心想法是，使用摄像头捕获到舞台卡片/物体，接着使用 Teachable Machine 训练好的模型来识别它，最后通过编程让 Scratch 中的虚拟角色与识别出的物体互动！在这个想法下，可以玩的东西非常多。


你可以训练你的 AI 助手识别任何你喜欢的玩具，然后与之互动。

诸如拿出一只老虎玩偶放在舞台中，它的朋友会作何反应呢？它的敌人会如何反应呢？舞台里的一只虚拟小猫可能叫了一声，一下子就蹿远了。

构建你自己的故事吧，让真实世界和虚拟世界互动起来。

你也可以通过接入 [Home Assistant](/Neverland/HA){target=\_blank}， 将整个家庭纳入到故事创作中，老虎出现时，随着一声虎啸，房间里的灯突然熄灭，预知后续如何？我们等待你的家庭剧本！

## 参考

-   [CodeLab Adapter 接入 Teachable Machine](https://www.codelab.club/blog/adapter-teachable-machine/)
-   [插件(extensions)文档 - Teachable Machine](http://localhost:8000/extension_guide/teachable_machine/)
