# 收工，吃饭
**Scratch**、**Home Assistant**、**智能家居（smart home）**、**声音检测（Sound）**

## 步骤 1：构建

### 是什么?
<video width="80%" src="/video/turnofflight_byfinger.mp4" controls="controls"></video>

打一个响指，关掉整个办公室的灯，下班回家吃饭！

### 它是如何工作的?
*  [运行 Home Assistant](/Neverland/HA){target=_blank}，接管空间的所有智能设备。
*  使用 CodeLab Scratch（[在线版](http://scratch-beta.codelab.club/){target=_blank}、[离线版](https://www.codelab.club/blog/2020/08/20/tools/){target=_blank}皆可）的 Home Assistant 扩展，控制智能设备。
*  使用 Scratch 中的 **声音响度积木** 监测环境中的声音，当声音响度超过某个值，关灯！

### 你需要准备些什么
*  [安装和配置 Home Assistant](/Neverland/HA){target=_blank}
*  CodeLab Scratch
*  智能家居设备（以下是 CodeLab 的推荐清单，任选一项即可）
    *  米家智能家庭套装（[购买链接](https://item.mi.com/product/5708.html){target=_blank}）
    *  Yeelight 彩光灯（[购买链接](https://www.yeelight.com/zh_CN/product/lemon-color){target=_blank}）
    *  如果你是 Home Assistant 用户，则可以任意使用[任何社区接入的套件](https://www.home-assistant.io/integrations/){target=_blank}

## 步骤 2：编程

![](/img/13b988916cd857177044a077d4fde798.png)

!!! 在线版与离线版打开方式
    如果你是要在线版，直接[点击项目链接](https://scratch.codelab.club/projects/23/editor/)即可。<!--https://scratch-beta.codelab.club/?sb3url=https://adapter.codelab.club/sb3/neverland_helloworld.sb3-->  
    如果你使用离线版，则下载[源码文件](/sb3/neverland_helloworld.sb3)，使用 Scratch 加载它即可.   
    加载后填入你之前记下的 token。

## 步骤 3：发挥想象
现在你可以使用 CodeLab Scratch 的 Home Assistant 插件自由的编程啦，试着与 Scratch 里其他有趣的积木互动吧。

如果你想让程序只对响指声作出反应，甚至只对你的响指声作出反应都是可能的，使用 AI 来做到这点！ [CodeLab Adapter 已经将 Teachable Machine 接入进来了](https://www.codelab.club/blog/adapter-teachable-machine/)，你可以使用声音、肢体、各种物体与你的房间进行互动！
