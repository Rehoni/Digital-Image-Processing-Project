# todo: exposure模块：直方图和均衡化（hist）


import numpy as np
from skimage import exposure, data
from matplotlib import pyplot as plt




# 分成两个bin，每个bin的统计量是一样的，但numpy返回的是每个bin的两端的范围值，而skimage返回的是每个bin的中间值
def simpleTest():
    image = data.camera() * 1.0
    hist1 = np.histogram(image, bins=2)
    hist2 = exposure.histogram(image=image, nbins=2)
    print(hist1)
    print(hist2)


# @param: hist的参数非常多，但常用的就这六个，只有第一个是必须的，后面四个可选
# arr: 需要计算直方图的一维数组
# bins: 直方图的柱数，可选项，默认为10
# normed: 是否将得到的直方图向量归一化。默认为0
# facecolor: 直方图颜色
# edgecolor: 直方图边框颜色
# alpha: 透明度
# histtype: 直方图类型，‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’
# @return ：
# n: 直方图向量，是否归一化由参数normed设定
# bins: 返回各个bin的区间范围
# patches: 返回每个bin里面包含的数据，是一个list

# n, bins, patches = plt.hist(arr, bins=10, normed=0, facecolor='black', edgecolor='black',alpha=1, histtype='bar')
def simpleHist():
    image = data.camera()
    plt.figure('hist')
    array = image.flatten()  # flatten()函数是numpy包里面的，用于将二维数组序列化成一维数组。
    n, bins, patches = plt.hist(array, bins=256, normed=1, edgecolor='None', facecolor='black')
    plt.show()


def rgbHist():
    image = data.astronaut()
    ar = image[:, :, 0].flatten()
    ag = image[:, :, 1].flatten()
    ab = image[:, :, 2].flatten()
    plt.hist(ar, bins=256, normed=1, facecolor='r', edgecolor='r', hold=1)
    plt.hist(ag, bins=256, normed=1, facecolor='g', edgecolor='g', hold=1)
    plt.hist(ab, bins=256, normed=1, facecolor='b', edgecolor='b')
    plt.show()


def equal_hist():
    image = data.moon()
    plt.figure('hist', figsize=(8, 8))
    array = image.flatten()
    plt.subplot(221)
    plt.imshow(image, cmap='gray')
    # plt.imshow(image, plt.cm.gray)  # 原始图像
    plt.subplot(222)
    plt.hist(array, bins=256, normed=1, edgecolor='None', facecolor='red')  # 原始图像直方图

    image1 = exposure.equalize_hist(image=image, nbins=256)
    array1 = image1.flatten()
    plt.subplot(223)
    plt.imshow(image1,plt.cm.gray)  # 均衡化图像
    plt.subplot(224)
    plt.hist(array1, bins=256, normed=1, edgecolor='None', facecolor='red')  # 均衡化直方图
    plt.show()



if __name__ == '__main__':
    simpleHist()
    rgbHist()
    equal_hist()
