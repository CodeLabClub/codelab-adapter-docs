# changelog
*  2018.5.26  v0.1.0
*  2018.5.28  v0.1.1
    *  fix extension_cozmo bug
*  2018.10.24 v0.2.0, [重构笔记](https://blog.just4fun.site/scratch3-adapter-refactoring-note.html)
*  2018.11.30 v0.2.3
*  2018.12.03 0.3.0 支持eim_script
*  2018.12.14 0.3.1 fix bug: 多个ws通道重复pub; 直接展示插件
*  2019.01.16 0.4.0
    *  支持第三方网站接入
    *  增加插件
    *  完善插件的管理，退出后自动清理子进程
    *  第三方库支持
        *  requests
        *  pyserial
        *  Pillow
*  2019.01.29 0.5.0
    *  修复read阻塞问题(导致需要额外的一条消息才能推出插件)
    *  支持前端启停插件
    *  将消息用作内部管理机制
    *  rename scratch3-adapter to codelab-adapter
    *  添加树莓派插件(gpiozero)
    *  支撑多个client并行作为UI(同步)
*  2019.01.30 0.5.1
    *  添加调试(Debug)页面
*  2019.02.14 0.6.0 
    *  添加rest api
    *  统一消息体命名规范: message.data/message.message -> message.payload
    *  添加`打开本地文件目录`功能
    *  内置微信插件(extension_wechat)
    *  添加typing库
    *  完善cli mode
*  2019.02.14 0.6.1
    *  提高微信插件(extension_wechat)的易用性（内置）
*  2019.02.15 0.6.2
    *  fix bug
*  2019.02.16 0.7.0
    *  允许跨域访问websocket/REST API, 方便开发者调试
    *  为webdebug添加REST API调试工具
*  2019.02.23 0.7.1
    *  让Cozmo/Vector插件支持同步模式(通过添加messageID),至于采用同步模式还是异步模式，由client决定
    *  添加[extension_mpfshell](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/extension_mpfshell.py)扩展(by [junhuanchen](https://github.com/junhuanchen))
*  2019.02.26 0.8.0
    *  允许用户添加自定义配置:`~/codelab_adapter/user_settings.py`
        *  典型的配置包括: `cli_load_extension_threads = ["extension_iot"]` 命令行模式(./codelab-adapter --mode cli)默认启动插件
    *  add [gpiozero](https://github.com/RPi-Distro/python-gpiozero) for raspberrypi platform
    *  内置mqtt client/broker: [hbmqtt](https://hbmqtt.readthedocs.io/en/latest/)
    *  内置[extension_iot](https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/extension_iot.py)
    *  更新extension_mpfshell
*  2019.03.16 0.8.1
    *  微信插件支持收发群消息
    *  添加web日志页面
    *  添加重构之后的blender插件
*  2019.08.28 2.3.1
*  2019.09.10 2.5.0
    *  安全性改进
*  2019.09.23 2.5.1
    *  使用scratch配色风格的Web UI
    *  版本号更新提醒(只提醒旧版本，不提醒测试版升级)
    *  报告adapter core信息(version)
*  2019.09.23 2.5.3
    *  将GUI menu迁移到web ui