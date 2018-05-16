# -*- coding: utf-8 -*-
from pylab import *
from PIL import ImageEnhance
from PIL import Image


image = Image.open('../ya.jpg').convert('L')
im = array(Image.open('../ya.jpg').convert('L'))

figure()
subplot(2, 1, 1)

imshow(image)
title('original图')

subplot(2, 1, 2)

hist(im.flatten(), 256)
title('直方图')

figure()
# Color、Brightness、Contrast和Sharpness。
enhancer = ImageEnhance.Brightness(image)
for i in range(1, 5):
    factor = i / 4.0
    subplot(2, 2, i)
    imshow(enhancer.enhance(factor))

show()
