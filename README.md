# 风云4号卫星云图壁纸

这是一个自用脚本，尚未进行过多的用户体验优化。

## 介绍

图像来源：风云4号4B，官方更新为15min一次，该壁纸设置为60min一次，可自行更改。

> 风云四号B星（FY-4B）于2021年6月3日0时17分，在西昌卫星发射中心搭乘长征三号乙运载火箭发射，是我国新一代静止轨道气象卫星风云四号系列卫星的首发业务星，标志着我国新一代静止轨道卫星观测系统正式进入业务化发展阶段，对确保我国静止气象卫星升级换代和连续、可靠、稳定业务运行意义重大。

## 软件说明

- 该软件每60分钟自动获取风云4B卫星的云图。
- 它会根据主屏幕的分辨率进行裁剪、缩放和填充。
- 自动抹除水印并将图片设置为壁纸。
- 如果设置壁纸失败，软件会在60秒后自动再次尝试。

## 使用方法

请在C盘创建以下文件夹，并设置指定文件及缓存路径（已预设，请按路径放置修改）：

- 软件路径：C:\软件\风云壁纸
- 缓存路径：C:\软件\风云壁纸\img

# 设置开机启动

请给 "main.exe" 创建一个快捷方式，并将快捷方式放入以下文件夹：

- C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup

注意：该软件在运行时不会显示窗口，如果需要关闭软件，请通过任务管理器结束进程（进程名称：main.exe）。
