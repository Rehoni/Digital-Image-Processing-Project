# todo: filters模块：图像自动阈值分割：了解各个api具体含义

from skimage import data, filters
import matplotlib.pyplot as plt

image = data.camera()
# threshold_yen
# threshold_li
# threshold_isodata 此三者用法和threshold_otsu相同
thresh = filters.threshold_otsu(image=image,nbins=256)  # 返回一个阈值
# block_size: 块大小，指当前像素的相邻区域大小，一般是奇数（如3，5，7。。。）
# method: 用来确定自适应阈值的方法，有'mean', 'generic', 'gaussian' 和 'median'。省略时默认为gaussian
# 该函数直接访问一个阈值后的图像，而不是阈值。
thresh1 = filters.threshold_adaptive(image=image,block_size=5,method='gaussian') # 返回一个阈值图像
dst = (image <= thresh) * 1.0  # 根据阈值进行分割

plt.figure('thresh', figsize=(8, 8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image, plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst, plt.cm.gray)

plt.show()
