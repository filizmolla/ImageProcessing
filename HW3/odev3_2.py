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
import cv2
from sklearn.cluster import KMeans


class Cluster:
    def __init__(self, label, centroid, centroid_indice):
        self.histograms = None 
        self.label = label 
        self.centroid_hist = centroid
        self.centroid_indice = centroid_indice
        
    def __repr__(self):
        return f"Cluster {self.label}, center indice: {self.centroid_indice}: Centroid hist: [{self.centroid_hist[0]}...{self.centroid_hist[767]}]"
        

class KMeans: 
    def __init__(self, all_histograms, k=5):
        self.k = k
        self.all_histograms = all_histograms 
        self.clusters = [] 
    
    @staticmethod
    def euclidian_distance(data_point_histogram, centroid_histogram):
        data_point = np.array(data_point_histogram)
        centroids = np.array(centroid_histogram)
        
        temp = data_point_histogram - centroid_histogram
        distance = np.linalg.norm(temp)

        return distance
    
    
    
    def fit(self, max_iterations=200 ):
        initial_centroids_indices = [49, 6, 47, 40, 22] #np.random.choice(len(histograms_array), k, replace=False)
        initial_centroids = self.all_histograms[initial_centroids_indices, :]
        i = 0
        for centroid_indice, centroid_hist in zip(initial_centroids_indices, initial_centroids):
            cluster = Cluster(i, centroid=centroid_hist, centroid_indice=centroid_indice)
            self.clusters.append(cluster)
            # print(cluster)
            i += 1
        
        #print(self.all_histograms[0])
        #print(self.clusters[0].centroid_hist)
        
        
        for i, data_point in enumerate(self.all_histograms):
            distances = []
            for j, cluster in enumerate(self.clusters):
                distance = KMeans.euclidian_distance(self.all_histograms[i], self.clusters[j].centroid_hist)
                distances.append(distance)
                # print(f"{i}, {j}, {distance}")
            # print(f"{i} {distances}")










def image_to_matrix(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    return img_array


def show_image(images, index):
    plt.imshow(images[index])
    plt.axis('off')
    plt.show()


def plot_histogram(image, title):
    hist_blue = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist_green = cv2.calcHist([image], [1], None, [256], [0, 256])
    hist_red = cv2.calcHist([image], [2], None, [256], [0, 256])

    total_pixels = np.prod(image.shape[:2])
    hist_blue /= total_pixels
    hist_green /= total_pixels
    hist_red /= total_pixels

    # plt.plot(hist_blue, color='blue', label='Blue')
    # plt.plot(hist_green, color='green', label='Green')
    # plt.plot(hist_red, color='red', label='Red')

    # plt.title(title)
    # plt.xlabel('Pixel Value')
    # plt.ylabel('Frequency')
    # plt.legend()
    # plt.show()
    return hist_red, hist_green, hist_blue



def generate_histograms(images):
    
    all_histograms = []

    for i, image_matrix in enumerate(images):
        #show_image(images, i)
        title = f"Histogram for Image {i + 1}"
        hist_red, hist_green, hist_blue = plot_histogram(image_matrix, title)
        all_histograms.append([hist_blue, hist_green, hist_red])

    return all_histograms



# 2 Goruntu matrisi elde et.
path = "/home/filiz/Desktop/ImageProcessing/HW3/images"
file_list = sorted(os.listdir(path))

print(len(file_list))
images = []

for file in file_list:
    image_path = os.path.join(path, file)
    image_matrix = image_to_matrix(image_path)

    #print(file)
    #print("Image shape:", image_matrix.shape)
    images.append(image_matrix)


images = np.array(images)



# 3. Goruntulerin histogramlarini elde et.

# for index in range(len(file_list)):
#     show_image(images, index)
#     plot_histogram(images[index], "RGB Histogram")

histograms = generate_histograms(images)
histograms_array = np.array(histograms).reshape(len(images), -1)


# Choose k random histograms as initial centroids
k = 5
kmeans = KMeans(histograms_array)
lables = kmeans.fit()












