# todo: transform模块：提供缩放和旋转
from skimage import io, transform, data
import numpy as np
import matplotlib.pyplot as plt

img = data.camera()

resizeImg = transform.resize(img, (80, 60))

rescaleImg = transform.rescale(img, scale=0.1)

print(img.shape)  # 图片原始大小
print(transform.rescale(img, 0.1).shape)  # 缩小为原来图片大小的0.1倍
print(transform.rescale(img, [0.5, 0.25]).shape)  # 缩小为原来图片行数一半，列数四分之一
print(transform.rescale(img, 2).shape)  # 放大为原来图片大小的2倍

rotateImg = transform.rotate(img, angle=60, resize=False)  # resize是改变大小的意思

# # 图像金字塔
# img = data.astronaut()
# rows, cols, dim = img.shape
# pyramid = tuple(transform.pyramid_gaussian(image=img, downscale=2))  # 产生高斯金字塔图像
# # 共生成了log(512)=9幅金字塔图像，加上原始图像共10幅，pyramid[0]-pyramid[1]
# composite_image = np.ones((rows, cols + cols / 2, 3), dtype=np.double)  # 生成背景
#
# composite_image[:rows, :cols, :] = pyramid[0]  # 融合原始图像
#
# i_row = 0
# for p in pyramid[1:]:
#     n_rows, n_cols = p.shape[:2]
#     composite_image[i_row:i_row + n_rows, cols:cols + n_cols] = p  # 循环融合9幅金字塔图像
#     i_row += n_rows

plt.figure()
plt.gray()
plt.subplot(221)
plt.title('original pic')
plt.imshow(img)

plt.subplot(222)
plt.title('resize pic')
plt.imshow(resizeImg)

plt.subplot(223)
plt.title('rescale pic')
plt.imshow(rescaleImg)

plt.subplot(224)
plt.title('rotate pic')
plt.imshow(rotateImg)

# plt.figure()
# plt.gray()
# plt.imshow(composite_image)
plt.show()
