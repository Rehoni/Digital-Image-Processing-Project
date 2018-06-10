from skimage import io, data_dir, data, exposure, color
from matplotlib import pyplot as plt
import numpy as np


class Show:

    def __init__(self):
        self.shape = dict()
        self._curr_path = None
        self._cache_path = 'C:/Users/Res0liya/Desktop/'
        self.curr_image = None
        self.hist_image = None
        self.hist_mod_image = None

    # open Image 读取html中的路径，存入curr_image
    # file_path = img.src

    def open_image(self, file_path):
        image = io.imread(file_path)
        self._curr_path = file_path
        self.curr_image = image

    def hist_image(self):
        self.hist_image = exposure.histogram(image=self.curr_image, nbins=2)

    def image_size(self, file_path):
        image = io.imread(file_path)
        return str(image.size)

    def image_mean(self, file_path):
        image = io.imread(file_path)
        return str(image.mean())

    # self.shape['type'] = type(self.curr_image)
    # self.shape['size'] = self.curr_image.size
    # self.shape['mean'] = self.curr_image.mean()
    # self.shape['shape'] = self.curr_image.shape
    # val_shape = self.shape
    # return val_shape

    def image_shape(self, file_path):
        image = io.imread(file_path)
        return str(image.shape)

    def image_gray(self):
        gray_image = color.rgb2gray(self.curr_image)
        cache_path = self._cache_path + 'temp.png'
        io.imsave(cache_path, gray_image)
        self.curr_image = gray_image
        return cache_path
