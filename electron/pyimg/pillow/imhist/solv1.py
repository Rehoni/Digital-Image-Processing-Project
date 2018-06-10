# 直方图均衡化

# -*- coding: utf-8 -*-

from PIL import Image

from pylab import *

# 读取图像到数组中，并灰度化
im = array(Image.open('../../lena.jpg').convert('L'))

# 绘制原始直方图
subplot(2, 3, 1)

hist(im.flatten(), 256)

# 计算图像直方图（每个bins数组的区间值对应一个imhist数组中的强度值）
imhist, bins = histogram(im.flatten(), 256, normed=True)

# 计算累积分布函数
cdf = imhist.cumsum()

# 累计函数归一化（由0～1变换至0~255）
cdf = cdf * 255 / cdf[-1]

# 绘制累计分布函数
subplot(2, 3, 2)

plot(bins[:256], cdf)

# 依次对每一个灰度图像素值（强度值）使用cdf进行线性插值，计算其新的强度值
# interp（x，xp，yp） 输入原函数的一系列点（xp，yp），使用线性插值方法模拟函数并计算f（x）
im2 = interp(im.flatten(), bins[:256], cdf)

# 将压平的图像数组重新变成二维数组
im2 = im2.reshape(im.shape)

# 显示均衡化之后的直方图图像
subplot(233)

hist(im2.flatten(), 256)

# 显示原始图像
gray()

subplot(234)

imshow(im)

# 显示变换后图像
subplot(236)

imshow(im2)

show()
