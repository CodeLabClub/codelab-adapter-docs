# 读书与思考

**AI**、**Scratch**、**Home Assistant**、**智能家居（smart home）**、**Teachable Machine**

## 步骤 1：构建

### 是什么?

<video width="80%" src="/video/1583984194594670.mp4" controls="controls"></video>

训练一个 AI 助手，当你在阅读时，自动帮你打开书房的灯；当你合上书开始思考，自动关闭书房的灯，让你沉浸在黑暗里。

### 它是如何工作的?

-   [运行 Home Assistant](/Neverland/HA){target=\_blank}，接管空间的所有智能设备。
-   使用 CodeLab Scratch（[在线版](http://scratch3v3.codelab.club/){target=\_blank}、[离线版](https://www.codelab.club/blog/codelab-download/){target=\_blank}皆可）的 Home Assistant 扩展，控制智能设备。
-   使用 Scratch 中的 **图片分类积木** ，训练 AI 来识别看书与合上书的不同状态。

### 你需要准备些什么

-   [安装和配置 Home Assistant](/Neverland/HA){target=\_blank}
-   CodeLab Scratch
-   智能家居设备（以下是 CodeLab 的推荐清单，任选一项即可）
    -   米家智能家庭套装（[购买链接](https://item.mi.com/product/5708.html){target=\_blank}）
    -   Yeelight 彩光灯（[购买链接](https://www.yeelight.com/zh_CN/product/lemon-color){target=\_blank}）
    -   如果你是 Home Assistant 用户，则可以任意使用[任何社区接入的套件](https://www.home-assistant.io/integrations/){target=\_blank}

## 步骤 2：编程

![](/img/bfad7206e13a0eaca82005bb7125f4f5.png)

!!! 在线版与离线版打开方式
    如果你是要在线版，直接[点击项目链接](https://scratch.codelab.club/projects/24/editor/)即可。未来我们会直接发布到社区里。<!--https://scratch3v3.codelab.club/?sb3url=https://adapter.codelab.club/sb3/reading-thinking.sb3-->  
    如果你使用离线版，则下载[源码文件](/sb3/reading-thinking.sb3)，使用 Scratch 加载它即可.  
    加载后填入你之前记下的 token。

1. 在 **home button** 角色里设置你的 Home Assistant 访问 token；
2. 点击绿旗开始运行程序；
3. 按下 **r** 按键，添加 **看书** 样本。舞台区，你应该看到正在看书的摄像头画面；
4. 按下 **t** 按键，添加 **思考** 样本。舞台区，你应该看到正在思考（合上书）的摄像头画面；
5. 按下 **n** 按键，添加 **无** 样本，此时你既没在看书，也没在思考，桌子上空空如也；
6. 按下 **空格** ，开始识别你的桌面状态；
7. 按下 **q** 案件，暂时结束识别。

!!! 提醒
    如果关灯后你的房间完全处于黑暗，那么当你再次翻开书，摄像头将看不到你的这个行为！一般来说只有一些光线，它就能看到。如果你的房间遮光效果真的很好，可以考虑使用红外夜视摄像头。  
    如果它识别地并不准确，观察是否是光线造成的。重复训练，知道你对这个 AI 感到满意。  
    当然你也可以使用 Teachable Machine 来制作这个项目，它更加直观！ [CodeLab Adapter 已经将 Teachable Machine 接入进来了](https://www.codelab.club/blog/adapter-teachable-machine/)！  


## 步骤 3：发挥想象
这儿的核心想法是，使用摄像头捕获到外部世界的状态（翻开书/合上书），接着使用这些数据训练一个 AI 助手，让它对外部世界状态变化作出反馈！在这个想法下，能做的事情可太多啦。

如果你跟我一样是个懒人，则可以训练一个 AI 助手放在厨房，当摄像头识别到我早上第一次穿着睡衣出现在厨房里时，则自动启动整个早餐程序，由于 Home Assistant 已经把你的整个家庭设备加入进来，所以你可以做的事情非常丰富，把你的生活习惯交给自己训练的 AI 来打理，随着你的训练，它会越来越聪明，只有你最清楚自己的习惯，你或许不想由别人的云大脑来监视和服务你，毕竟你可能正光着膀子。

如果你家里有小孩，则可以将摄像头厨房里，让某些危险设备不对孩子的操作做反应，诸如当小孩按下烧水壶时，AI 助手可以告诉 Home Assistant 切断电源。
