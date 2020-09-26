# Tutorial

系统依赖参考 [EIM 教程](/extension_guide/eim/)。

操作树莓派 GPIO 的工具里，[gpiozero](https://gpiozero.readthedocs.io/en/stable/index.html)尤为出色，因其具有很好的可理解性， 图形化未必意味着更好的可理解性。

为了充分利用 gpiozero，决定只对它做一层薄薄的包装(REPL), 使其在 Scratch 中可用。

尤其适合于那些试图以 Python 去增强 Scratch 的人。

!!! 提醒
    如果你在用 树莓派 4B， 建议更新一下wiringPi: [wiringPi updated to 2.52 for the Raspberry Pi 4B](http://wiringpi.com/wiringpi-updated-to-2-52-for-the-raspberry-pi-4b/)  

# 安装和配置
参考 [Installing GPIO Zero](https://gpiozero.readthedocs.io/en/stable/installing.html#installing-gpio-zero)

Raspbian 默认已经预装 gpiozero 。

你需要启动它: `sudo systemctl start pigpiod`

如果你计划在 PC 或 Mac上对树莓派 GPIO 进行编程， 需要[配置使其可被远程访问](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html)。

同时你需要在本地安装: `python -m pip install codelab_adapter_client gpiozero pigpio --user`

我们推荐远程访问模式，这意味着，树莓派可以运行在局域网里的任何地方，而你可以在自己的电脑上使用 CodeLab Adapter 对它进行编程，如此一来，你可以把 Scratch 和 Adapter 的所有能力带给它。

当然你也可以在树莓派上运行 Adapter 和 Scratch。

# 开始使用
!!! 提醒
    在 Adapter 3.2 之前，你需要自行从[插件市场](/extension_guide/extension_market/)里下载 raspberrypi 插件。 [源码地址](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/nodes_v3/node_raspberrypi.py)  
    树莓派默认地址为:`raspberrypi.local`, 如果你ping不通它，可以手动在插件里填写树莓派ip。

运行树莓派插件，打开 [Scratch-rpi-gpiozero](https://scratch-beta.codelab.club?sb3url=https://adapter.codelab.club/sb3/Scratch-gpiozero.sb3)。

    
!!! 提醒
    如果你手头没有LED， 你可以[使用命令行工具 gpio](https://blog.just4fun.site/post/iot/raspberrypi-install-and-config/#%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7) ，观察引脚输出变化。  
    gpio用的mode是wPi，而gpiozero用的是BCM，所以pin17对应wpi的pin0  
    ![](/img/fa6b43a839c1e55d8e761529ac996970.png) 

# 最后
我们并不打算构建完备的积木组操控树莓派，树莓派高度灵活，难以完全积木化它的所有特性，那样不会提高可理解性。 我们希望用户灵活使用 Python 去增强 Scratch ，更好的扩展模式可以参考[Python eval kernel](https://adapter.codelab.club/extension_guide/extension_python_kernel/)。

当然一些功能是可以积木化的，期待你来提交 PR。

!!! 提醒
    [Raspbian Scratch 3 Desktop](https://www.raspberrypi.org/blog/scratch-3-desktop-for-raspbian-on-raspberry-pi/)也是个很好的选择，有丰富的积木。  
    CodeLab Adapter的目标是**连接**。 

# 参考
- [gpio 测试工具](https://blog.just4fun.site/post/iot/raspberrypi-install-and-config/#%E6%B5%8B%E8%AF%95%E5%B7%A5%E5%85%B7)
- [wiringPi updated to 2.52 for the Raspberry Pi 4B](http://wiringpi.com/wiringpi-updated-to-2-52-for-the-raspberry-pi-4b/)