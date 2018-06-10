# todo: filters模块：边缘检测算子和几种常见滤波（filter）

from scikitfunc.imagefunc import Show
from skimage import io, color, data, filters, feature
from skimage.morphology import disk
import matplotlib.pyplot as plt


# image = io.imread('../lena.jpg')
# img = color.rgb2gray(image)


# 几种边缘检测算子
class EdgeShow(Show):

    def __init__(self):
        Show.__init__(self)

    def sobel(self):
        cache_path = self._cache_path + 'sobel.png'
        sobel = filters.sobel(self.curr_image)
        io.imsave(cache_path, sobel)
        return cache_path

    def laplace(self):
        cache_path = self._cache_path + 'laplace.png'
        laplace = filters.laplace(self.curr_image)
        io.imsave(cache_path, laplace)
        return cache_path

    def prewitt(self):
        cache_path = self._cache_path + 'prewitt.png'
        prewitt = filters.prewitt(self.curr_image)
        io.imsave(cache_path, prewitt)
        return cache_path

    def roberts(self):
        cache_path = self._cache_path + 'roberts.png'
        roberts = filters.roberts(self.curr_image)
        io.imsave(cache_path, roberts)
        return cache_path


img = data.camera()
sobel = filters.sobel(img)
laplace = filters.laplace(img)
prewitt = filters.prewitt(img)
roberts = filters.roberts(img)
plt.figure('suanzi', figsize=(8, 8))
plt.subplot(221)
plt.imshow(img, plt.gray())
plt.subplot(222)
io.imshow(sobel)
plt.subplot(223)
io.imshow(roberts)  # gaussian有点小问题
plt.subplot(224)
io.imshow(prewitt)
plt.show()
# canny
img = data.camera()
edges1 = feature.canny(img)  # sigma=1
edges2 = feature.canny(img, sigma=3)  # sigma=3

plt.figure('canny', figsize=(8, 8))
plt.subplot(121)
plt.imshow(edges1, plt.cm.gray)

plt.subplot(122)
plt.imshow(edges2, plt.cm.gray)

plt.show()

# gabor
img = data.camera()
filt_real, filt_imag = filters.gabor_filter(img, frequency=0.6)

plt.figure('gabor', figsize=(8, 8))

plt.subplot(121)
plt.title('filt_real')
plt.imshow(filt_real, plt.cm.gray)

plt.subplot(122)
plt.title('filt-imag')
plt.imshow(filt_imag, plt.cm.gray)

plt.show()
# 水平垂直
img = data.camera()
edges1 = filters.sobel_h(img)
edges2 = filters.sobel_v(img)

plt.figure('sobel_v_h', figsize=(8, 8))

plt.subplot(121)
plt.imshow(edges1, plt.cm.gray)

plt.subplot(122)
plt.imshow(edges2, plt.cm.gray)

plt.show()
# 交叉
img = data.camera()
dst = filters.roberts_neg_diag(img)

plt.figure('filters', figsize=(8, 8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img, plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst, plt.cm.gray)
plt.show()
img = data.camera()
dst = filters.roberts_pos_diag(img)

plt.figure('filters', figsize=(8, 8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img, plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst, plt.cm.gray)
plt.show()
# 高斯滤波
img = data.camera()
edges1 = filters.gaussian_filter(img, sigma=0.4)  # sigma=0.4
edges2 = filters.gaussian_filter(img, sigma=5)  # sigma=5

plt.figure('gaussian', figsize=(8, 8))
plt.subplot(121)
plt.imshow(edges1, plt.cm.gray)

plt.subplot(122)
plt.imshow(edges2, plt.cm.gray)

plt.show()
# 中值滤波
img = data.camera()
edges1 = filters.median(img, disk(5))
edges2 = filters.median(img, disk(9))

plt.figure('median', figsize=(8, 8))

plt.subplot(121)
plt.imshow(edges1, plt.cm.gray)

plt.subplot(122)
plt.imshow(edges2, plt.cm.gray)

plt.show()
# 维纳滤波和逆滤波的变换还没搞好

# inverse = filters.inverse(img)
# wiener = filters.wiener(img)
# gaussian1 = filters.gaussian(img, sigma=0.1)
# gaussian = filters.gaussian(img, sigma=1.0)
#
# median = filters.median(img, disk(5))
# median1 = filters.median(img, disk(9))

# plt.figure()
# plt.gray()
# plt.subplot(221)
# plt.imshow(gaussian)
# plt.subplot(222)
# plt.imshow(gaussian1)
# plt.subplot(223)
# plt.imshow(median)
# plt.subplot(224)
# plt.imshow(median1)
# plt.show()


# plt.subplot(221)
# io.imshow(inverse)
# plt.subplot(222)
# io.imshow(wiener)
# plt.subplot(223)
# io.imshow(gaussian)
# plt.subplot(224)
# io.imshow(median)
# plt.show()
