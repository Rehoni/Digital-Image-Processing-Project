from skimage import io,color, data,filters
from skimage.morphology import disk
import matplotlib.pyplot as plt

image=io.imread('../lena.jpg')
img=color.rgb2gray(image)

# 几种边缘检测算子
img = data.camera()
sobel = filters.sobel(img)
laplace = filters.laplace(img)
prewitt=filters.prewitt(img)
roberts = filters.roberts(img)
plt.figure('suanzi',figsize=(8,8))
plt.subplot(221)
plt.imshow(img,plt.gray())
plt.subplot(222)
io.imshow(sobel)
plt.subplot(223)
io.imshow(roberts) #gaussian有点小问题
plt.subplot(224)
io.imshow(prewitt)
plt.show()

# 几种滤波，用于图像复原
# 还存在一些问题
# 维纳滤波和逆滤波的变换还没搞好

# inverse = filters.inverse(img)
# wiener = filters.wiener(img)
gaussian1 = filters.gaussian(img, sigma=0.1)
gaussian = filters.gaussian(img, sigma=1.0)

median = filters.median(img,disk(5))
median1 = filters.median(img, disk(9))

plt.figure()
plt.gray()
plt.subplot(221)
plt.imshow(gaussian)
plt.subplot(222)
plt.imshow(gaussian1)
plt.subplot(223)
plt.imshow(median)
plt.subplot(224)
plt.imshow(median1)
plt.show()
# plt.subplot(221)
# io.imshow(inverse)
# plt.subplot(222)
# io.imshow(wiener)
# plt.subplot(223)
# io.imshow(gaussian)
# plt.subplot(224)
# io.imshow(median)
# plt.show()