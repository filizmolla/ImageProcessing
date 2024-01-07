#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 22:25:20 2024

@author: filiz
"""
import shutil
import os

path = "/home/filiz/Desktop/ImageProcessing/HW3/color.v1-color_v7.multiclass"
target_path = "/home/filiz/Desktop/ImageProcessing/HW3/images"
train_path = path + "/valid"

print(train_path)

train_file_list = sorted(os.listdir(train_path))
print(len(train_file_list))

colors= ['red', 'whi', 'blu', "gre", "gra"] 

if not os.path.exists(target_path):
    os.makedirs(target_path)


for color in colors:
    i = 0
    for file in train_file_list:
        if file.split(".")[0][0:3] == color :
            filename = f"{color}{i}_jpg.rf"
            i += 1
            original_file_path = os.path.join(train_path, file)
            target_file_path = os.path.join(target_path, filename)
            shutil.copy(original_file_path, target_file_path)
            if i == 20:
                break

