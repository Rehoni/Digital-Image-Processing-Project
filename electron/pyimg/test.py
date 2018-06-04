from skimage import io, data_dir, data, exposure, img_as_float

import numpy as np
from matplotlib import pyplot as plt

# 直方图
# 直方图均衡化

# img1 = data.camera()
# img2 = img_as_float(img1)
# hist1, bin_centers1 = np.histogram(img2, bins=2)
# hist2, bin_centers2 = exposure.histogram(img2, nbins=2)
#
# print(img1)
# print(img2)
#
# print(hist1)
# print(hist2)
#
# io.imsave('C:/Users/Res0liya/Desktop/camera.png', hist1)

# 图片属性
# 一些信息

img = io.imread('lena.jpg')
shape = dict()
# shape = {'type': None, 'shape': None, 'size': None,'mean': None};
# print(type(img))  # 显示类型 <class 'numpy.ndarray'>
# print(img.shape)  # 显示尺寸 (482, 482, 3)
# print(img.shape[0])  # 图片宽度 482
# print(img.shape[1])  # 图片高度 482
# print(img.shape[2])  # 图片通道数 3
# print(img.size)  # 显示总像素个数 696972
# print(img.max())  # 最大像素值 255
# print(img.min())  # 最小像素值 0
# print(img.mean())  # 像素平均值 212.99801713698685

shape['type'] = type(img)
shape['shape'] = img.shape
shape['size'] = img.size
shape['mean'] = img.mean()


print(shape)
io.imshow(img)
