from skimage import io, data_dir, data, exposure, img_as_float

import numpy as np
from matplotlib import pyplot as plt

img1 = data.camera()
img2 = img_as_float(img1)
hist1, bin_centers1 = np.histogram(img2, bins=2)
hist2, bin_centers2 = exposure.histogram(img2, nbins=2)

print(img1)
print(img2)

print(hist1)
print(hist2)

io.imsave('C:/Users/Res0liya/Desktop/camera.png', hist1)
