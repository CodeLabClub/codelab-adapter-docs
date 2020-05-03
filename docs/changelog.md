# changelog
*  2018.5.26  v0.1.0
*  2018.5.28  v0.1.1
    *  fix extension_cozmo bug
*  2018.10.24 v0.2.0，[重构笔记](https://blog.just4fun.site/scratch3-adapter-refactoring-note.html)
*  2018.11.30 v0.2.3
*  2018.12.03 0.3.0 支持eim_script
*  2018.12.14 0.3.1 fix bug：多个 ws 通道重复 pub；直接展示插件
*  2019.01.16 0.4.0
    *  支持第三方网站接入
    *  增加插件
    *  完善插件的管理，退出后自动清理子进程
    *  第三方库支持
        *  requests
        *  pyserial
        *  Pillow
*  2019.01.29 0.5.0
    *  修复 read 阻塞问题（导致需要额外的一条消息才能推出插件）
    *  支持前端启停插件
    *  将消息用作内部管理机制
    *  rename scratch3-adapter to codelab-adapter
    *  添加树莓派插件（gpiozero）
    *  支撑多个 client 并行作为 UI（同步）
*  2019.01.30 0.5.1
    *  添加调试（Debug）页面
*  2019.02.14 0.6.0 
    *  添加 REST API
    *  统一消息体命名规范：message.data/message.message -> message.payload
    *  添加`打开本地文件目录`功能
    *  内置微信插件（extension_wechat）
    *  添加 typing 库
    *  完善 cli mode
*  2019.02.14 0.6.1
    *  提高微信插件（extension_wechat）的易用性（内置）
*  2019.02.15 0.6.2
    *  fix bug
*  2019.02.16 0.7.0
    *  允许跨域访问 websocket/REST API, 方便开发者调试
    *  为 webdebug 添加 REST API 调试工具
*  2019.02.23 0.7.1
    *  让 Cozmo/Vector 插件支持同步模式（通过添加 messageID），至于采用同步模式还是异步模式，由 client 决定
    *  添加 [extension_mpfshell](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_mpfshell.py) 扩展（by [junhuanchen](https://github.com/junhuanchen)）
*  2019.02.26 0.8.0
    *  允许用户添加自定义配置：`~/codelab_adapter/user_settings.py`
        *  典型的配置包括：`cli_load_extension_threads = ["extension_iot"]` 命令行模式（./codelab-adapter --mode cli）默认启动插件
    *  add [gpiozero](https://github.com/RPi-Distro/python-gpiozero) for raspberrypi platform
    *  内置 mqtt client/broker：[hbmqtt](https://hbmqtt.readthedocs.io/en/latest/)
    *  内置 [extension_iot](https://github.com/CodeLabClub/codelab_adapter_extensions/blob/master/extension_iot.py)
    *  更新 extension_mpfshell
*  2019.03.16 0.8.1
    *  微信插件支持收发群消息
    *  添加 web 日志页面
    *  添加重构之后的 blender 插件
*  2019.08.28 2.3.1
*  2019.09.10 2.5.0
    *  安全性改进
*  2019.09.23 2.5.1
    *  使用 Scratch 配色风格的 Web UI
    *  版本号更新提醒（只提醒旧版本，不提醒测试版升级）
    *  报告 adapter core 信息（version）
*  2019.09.23 2.5.3
    *  将 GUI menu 迁移到 Web UI
*  2019.11.13 2.6.0
    *  2.6.x 专注于提高健壮性
    *  添加 rate limit 机制：TokenBucket
    *  为 usb_microbit 添加 TokenBucket
    *  提升 token 安全性（每次启动随机生成；也允许用户在配置文件里固化token）
    *  添加 token 复制按钮（用于粘贴到外部网站） 
    *  将 token 添加到 scratch 启动 url 里（提高安全性）
*  2019.11.13 2.6.1
    *  Scratch3Lab -> CodeLabClub
*  2019.11.13 2.6.2
    *  支持 headless 模式（linux），用于开机自启、无人值守的环境
*  2020.04.17 3.0.0
    *  [发行说明](https://www.codelab.club/blog/3-release/)
*  2020.04.30 3.1.0
    *  自动更新 adapter home 目录
    *  插件市场支持extension/node下载(统称为plugin)，node可以是任何有效的url链接
    *  Cozmo 插件支持 event、sensor
    *  Adapter 默认随最后一个client关闭而关闭，允许用户配置该行为
    *  重构 WebUI 的 Adatper socketio client，使其易于二次开发