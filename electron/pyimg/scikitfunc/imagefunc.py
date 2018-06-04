from skimage import io, data_dir, data, exposure

import numpy as np
from matplotlib import pyplot as plt


class Show:

    def __init__(self):
        self.shape = dict()
        self.__curr_path = None
        self.__cache_path = 'C:/Users/Res0liya/Desktop/camera.png'
        self.curr_image = None
        self.hist_image = None
        self.hist_mod_image = None

    # open Image 读取html中的路径，存入curr_image
    # file_path = img.src
    #

    def openImage(self, file_path):
        image = io.imread(file_path)
        self.__curr_path = file_path
        self.curr_image = image

    def histImage(self):
        self.hist_image = exposure.histogram(image=self.curr_image, nbins=2)

    def imageShape(self):
        self.shape['type'] = type(self.curr_image)
        self.shape['size'] = self.curr_image.size
        self.shape['mean'] = self.curr_image.mean()
        self.shape['shape'] = self.curr_image.shape
        return self.shape
