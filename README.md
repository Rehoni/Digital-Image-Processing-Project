# DIP
数字图像处理大作业，根据数字图像处理课上讲的一些内容,进行一个简单的实现吧
基本上是调用scimage的API了

## 技术栈

1. pillow 似乎scimage包含pillow里边的功能啊, 放弃pillow了
2. **scikit-image** scimage(针对我需要实现的简单功能来说, 是一个很全面的数字图像处理包
3. openCV 看心情
4. electron 用作GUI

## 放个about图

![about图](UIassets\about.png)

## 需求抽离

1. 图像增强 空域增强 -> pillow

    - [x] 直方图修正(绘制, 均衡化)和均衡化
    - [x] 彩色增强
    - [x] 平滑和锐化处理

2. 图像增强 频域操作

    - [ ] 低通滤波
    - [ ] 高通滤波
    - [ ] 同态滤波

3. 图像操作

    - [ ] 旋转平移
    - [ ] 拉伸(调整尺寸)
    - [ ] 放大缩小

4. 边缘检测算子

    - [x] Sobel
    - [x] Laplace
    - [x] Prewitt
    - [x] Roberts

5. 高级

    - [x] 图像复原
    - [x] 图像分割
    - [ ] 图像压缩