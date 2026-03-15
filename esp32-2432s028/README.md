# ESP32-2432S028 项目模板

这是一个可直接用 **PlatformIO + Arduino** 打开的 ESP32-2432S028 入门项目，包含：

- ILI9341 屏幕初始化（`TFT_eSPI`）
- 背光控制
- 串口日志
- 每 500ms 刷新一次的状态 UI（运行时间 + LED 状态）

## 1. 环境准备

1. 安装 VS Code
2. 安装 PlatformIO 插件
3. 打开本目录 `esp32-2432s028`

## 2. 编译与烧录

```bash
cd esp32-2432s028
pio run
pio run -t upload
pio device monitor
```

> 默认串口波特率为 `115200`。

## 3. 默认引脚定义

本项目在 `platformio.ini` 中通过 `build_flags` 为 `TFT_eSPI` 注入了常见的 ESP32-2432S028 引脚参数：

- `TFT_MISO=12`
- `TFT_MOSI=13`
- `TFT_SCLK=14`
- `TFT_CS=15`
- `TFT_DC=2`
- `TFT_RST=-1`
- `TOUCH_CS=33`
- `TFT_BL=21`

不同批次开发板可能有差异。如果屏幕显示异常，请按你手上的板卡原理图调整这些参数。

## 4. 代码入口

主程序在：

- `src/main.cpp`

你可以从这几个方向继续扩展：

- 加入触摸驱动（XPT2046）
- 改成 LVGL 界面
- 接入 Wi-Fi + MQTT + 传感器
