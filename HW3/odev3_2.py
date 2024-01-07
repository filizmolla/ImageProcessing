#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 02:22:45 2024

@author: filiz
"""
import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def image_to_matrix(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    return img_array


def show_image(images, index):
    plt.imshow(images[index])
    plt.axis('off')
    plt.show()

path = "/home/filiz/Desktop/ImageProcessing/HW3/images"
file_list = sorted(os.listdir(path))

print(len(file_list))
images = []

for file in file_list:
    image_path = os.path.join(path, file)
    image_matrix = image_to_matrix(image_path)

    print(file)
    print("Image shape:", image_matrix.shape)
    images.append(image_matrix)


images = np.array(images)

print(images.shape)

show_image()

