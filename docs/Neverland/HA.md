# 安装和配置 Home Assistant

!!!Neverland 与 Home Assistant
    社区版 Neverland 使用 [Home Assistant](https://www.home-assistant.io/){target=_blank} 驱动家居/联网设备，用户可以使用 CodeLab Scratch、Python，或者 CodeLab Adapter 支持的[其他 34 门编程语言](https://adapter.codelab.club/dev_guide/system_command/)，与家居/联网设备交互。

## Home Assistant 简介
Home Assistant 是一个开源家庭自动化软件，将隐私放在首位，由全球各地的志愿者构建。目前支持 1,500+ 智能家居设备。

Home Assistant 采用 Python 构建，可以运行在任何主流操作系统，以及[树莓派](https://www.raspberrypi.org/){target=_blank}中。

## 安装在哪里？
[Home Assistant](https://www.home-assistant.io/) 有[多种安装方法](https://www.home-assistant.io/docs/installation/){target=_blank}。如果你打算长期使用它，将其用于家庭自动化，推荐[在树莓派上安装](https://www.home-assistant.io/getting-started/)。 如果你安装它是为了临时使用 Scratch 来对家庭设备进行编程，则直接在你编程的电脑上安装即可。

## 环境依赖
[Python](https://www.python.org/downloads/){target=_blank} >= `3.6`


## 开始安装
*  `pip3 install homeassistant`
    *  国内用户可通过更换 pypi 源加速安装过程: `pip3 install homeassistant  -i https://mirrors.aliyun.com/pypi/simple`

## 启动 Home Assistant
`hass --open-ui`

第一次启动时，会安装部分依赖项，根据网络情况不同，耗时不等。

一切准备就绪，将自动打开浏览器，进入都 Home Assistant 主页。访问地址是：`http://127.0.0.1:8123`

![](https://www.home-assistant.io/images/getting-started/username.png)

第一次使用需要填写基本用户信息，放心，数据都保存在本地。

## 添加智能设备
这里展示如何接入 Yeelight 彩光灯（[购买链接](https://www.yeelight.com/zh_CN/product/lemon-color){target=_blank}）和米家智能家庭套装（[购买链接](https://item.mi.com/product/5708.html){target=_blank}）。

如果你有其他智能设备需要接入，可参考[官方文档](https://www.home-assistant.io/){target=_blank}。或者 Google 搜索`home assistant + 你想接入的设备`。

### 接入 Yeelight 彩光灯
#### 步骤 1：配网
下载 **Yeelight** 手机客户端 ，按照 App 引导，为彩光灯配网。

配网完成后，你应该能使用 App 控制它。

#### 步骤 2：局域网访问
进入设备页，点击右下角按钮。

<img src="/img/yeelight1.jpeg" width=300 />

允许局域网访问。

#### 步骤 3：获取设备 IP
进入设备页，点击左上角控制器，获取设备 IP。

<img src="/img/yeelight2.jpeg" width=300 />

#### 步骤 4：添加配置信息
将 Yeelight 彩光灯配置信息，添加到 [Home Assistant 配置文件（configuration.yaml）](https://www.home-assistant.io/docs/configuration/){target=_blank}里。

配置文件所在路径:

```
macOS	~/.homeassistant
Linux	~/.homeassistant
Windows	%APPDATA%/.homeassistant
```


添加配置信息:

```yaml
yeelight:
  devices:
    192.168.21.102:
      name: Living Room
```

#### 步骤 5：重启 Home Assistant
重启之后，你应该可以使用 Home Assistant 控制 Yeelight 彩光灯了！

![](/img/ha_yeelight.jpeg)

### 米家智能家庭套装
#### 步骤 1：配网
下载 **米家** 手机客户端 ，按照APP引导，首先为 **智能网关** 配网，之后把其他设备接入进来。

配网完成后，你应该能使用 App 控制它们。

#### 步骤 2：局域网访问
进入 **智能网关** 页，点击右上角，点击 `关于`。

<img src="/img/mijia.jpeg" width=300 />

进入关于页，猛戳空白处多下（操作听硬核的 :P）， 将出现 **局域网通信协议**，
<img src="/img/mijia2.jpeg" width=300 />

点击进入，打开它，并记下密码：

<img src="/img/mijia3.jpeg" width=300 />

#### 步骤 3：添加配置信息
将 Yeelight 彩光灯配置信息，添加到 [Home Assistant配置文件（configuration.yaml）](https://www.home-assistant.io/docs/configuration/){target=_blank}里。

配置文件所在路径：

```
macOS	~/.homeassistant
Linux	~/.homeassistant
Windows	%APPDATA%/.homeassistant
```


添加配置信息：

```yaml
xiaomi_aqara:
  discovery_retry: 5
  gateways:
    - key: 60n163sp2rduqx4ri
```

#### 步骤 4：重启 Home Assistant
重启之后，你应该可以使用 Home Assistant 控制 **米家智能家庭套装** 里的设备了！

![](/img/ha_mijia.jpeg)

## 使用 CodeLab Scratch 连接 Home Assistant
为了方便用户使用 Scratch 驱动家居设备，我们需要获取 Home Assistant 的访问 token，将其粘贴到 CodeLab Scratch 里的 Home Assistant 拓展积木里。如此一来我们就可以使用 CodeLab Scratch 来为家庭/教室里的设备编程。打个响指，把灯关掉！

#### 获取 Home Assistant 访问 token
如图依次按顺序（1、2、3）操作：

![](/img/ha_token.png)

由于 token 只出现一次，所以你最好先复制粘贴到记事本里。

## 使用 CodeLab Scratch 为家庭设备编程！


你既可以使用 CodeLab Scratch [在线版](http://scratch3v2.codelab.club/){target=_blank}，也可以使用[离线版](https://www.codelab.club/blog/codelab-download/){target=_blank}来进行编程。

![](/img/13b988916cd857177044a077d4fde798.png)

!!! 在线版与离线版打开方式
    如果你是要在线版，直接[点击项目链接](https://scratch.codelab.club/projects/23/editor/)即可。
    如果你使用离线版，则下载[源码文件](/sb3/neverland_helloworld.sb3)，使用 Scratch 加载它即可。
    

加载后填入你之前记下的 token。

!!! 提醒
    如果你的 Home Assistant 访问地址不是`http://127.0.0.1:8123` (诸如运行在树莓派上)，你就无法在 **在线版** 中连接它( 浏览器安全策略 )。有两种解决方案:  
    1. 使用离线版  
    2. 将 Home Assistant 的访问地址`http://127.0.0.1:8123`映射到 https 上，可以采用以下任何一种方案:  
        *    [ngrok](https://ngrok.com/)：下载并运行`ngrok http 8123`，你将 Home Assistant 的访问地址暴露到了 https 公网, 形如:`https://ff4b68f8.ngrok.io`.  
        *    [其他办法](https://www.home-assistant.io/docs/configuration/remote/)

<!--
### 在线版 CodeLab Scratch
由于 CodeLab Scratch 的在线版使用`https`，所以你需要先将 Home Assistant 的访问地址`http://127.0.0.1:8123`映射到 https 上。


有很多种策略实现它：

*  [ngrok](https://ngrok.com/)：下载并运行`ngrok http 8123`，你将 Home Assistant 的访问地址暴露到了 https 公网, 形如:`https://ff4b68f8.ngrok.io`.
*  [mkcert](https://github.com/FiloSottile/mkcert)
*  [其他办法](https://www.home-assistant.io/docs/configuration/remote/)

总之你应该能够以 https 方式访问它。
-->



## 拓展
除了可以使用 CodeLab Scratch 连接 Home Assistant，我们还可以使用 CodeLab Adapter 连接 Home Assistant，这对我们在创客/IoT 实验室里展开教学，以及进行多语言教学（34+ 编程语言）都很有用。

这部分的文档我们将在未来同步过来。

# 参考
*  [Installation in Python virtual environment](https://www.home-assistant.io/docs/installation/virtualenv/)
*  [Install Home Assistant](https://www.home-assistant.io/getting-started/)
