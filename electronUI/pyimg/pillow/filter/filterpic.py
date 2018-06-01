# -*- coding: utf-8 -*-
from pylab import *
from PIL import ImageFilter
from PIL import Image


im = Image.open('../lena.jpg').convert('L')
# im = array(Image.open('../ya.jpg').convert('L'))

smooth = im.filter(ImageFilter.SMOOTH)
smoothmore = im.filter(ImageFilter.SMOOTH_MORE)
sharp = im.filter(ImageFilter.SHARPEN)
filter = im.filter(ImageFilter.MedianFilter)

figure()
subplot(231)

imshow(im)
title('original pic')

subplot(232)

hist(array(im).flatten(), 256)
title('imhist pic')

subplot(233)
imshow(smooth)
title('smooth pic')

subplot(234)
imshow(smoothmore)
title('smooth more pic')

subplot(235)
imshow(sharp)
title('sharp pic')

subplot(236)
imshow(filter)
title('median filter pic')

show()