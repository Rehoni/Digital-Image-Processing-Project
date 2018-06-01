# todo : restoration模块：仅仅实现了wiener滤波复原
# 提供图像恢复功能

import numpy as np
from skimage import io, data, util, restoration
from scipy.signal import convolve2d  # 用于psf
from skimage.filters.rank import noise_filter

from matplotlib import pyplot as plt
from skimage.morphology import disk

img = data.camera()

noiseGaus = util.random_noise(image=img, mode='gaussian')  # 加高斯噪声, 有各种可选参数
noiseSP = util.random_noise(image=img, mode='s&p')  # 椒盐噪声

filter = noise_filter(noiseGaus, selem=disk(5))  # 效果不好 可能是出了问题


def wiener_restoration(noisePicture):
    # wiener滤波复原
    psf = np.ones((5, 5)) / 25
    img = convolve2d(noisePicture, psf, 'same')
    img += 0.1 * img.std() * np.random.standard_normal(img.shape)
    deconvolved_img = restoration.wiener(image=img, psf=psf, balance=1100)
    return deconvolved_img



def show_pictures():
    plt.figure()
    plt.gray()

    plt.subplot(221)
    plt.imshow(noiseGaus)

    plt.subplot(222)
    plt.imshow(noiseSP)

    plt.subplot(223)
    plt.imshow(wiener_restoration(noiseGaus))

    plt.subplot(224)
    plt.imshow(wiener_restoration(noiseSP))

    plt.show()


if __name__ == '__main__':
    show_pictures()
