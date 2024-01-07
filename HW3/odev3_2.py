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
    def __init__(self, label, centroid, centroid_indice=None):
        self.histograms = [] 
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
    
    
    
    def fit(self, max_iterations=100):
        initial_centroids_indices =np.random.choice(len(histograms_array), k, replace=False)#[62,42,85,48,5]
        initial_centroids = self.all_histograms[initial_centroids_indices, :]
        i = 0
        for centroid_indice, centroid_hist in zip(initial_centroids_indices, initial_centroids):
            cluster = Cluster(i, centroid=centroid_hist, centroid_indice=centroid_indice)
            self.clusters.append(cluster)
            print(cluster)
            i += 1
        
        #print(self.all_histograms[0])
        #print(self.clusters[0].centroid_hist)
        # convergence = False 
        
        # while not convergence: 
        for _ in range(max_iterations):
            y = []
        
            for i, data_point in enumerate(self.all_histograms):
                distances = []
                for j, cluster in enumerate(self.clusters):
                    distance = KMeans.euclidian_distance(self.all_histograms[i], self.clusters[j].centroid_hist)
                    distances.append(distance)
                    
                    # print(f"{i}, {j}, {distance}")
                # print(f"{i} {distances} {min(distances)} {distances.index(min(distances))}" )
                indice = distances.index(min(distances))
                y.append(indice)
                self.clusters[indice].histograms.append(self.all_histograms[i])
    
            # print(y)
            # Her bir cluster içindeki histogramların ortalamasını al.
            for i,cluster in enumerate(self.clusters):
                stacked_arrays = np.stack(self.clusters[i].histograms)
                result_array = np.mean(stacked_arrays, axis=0)
                #print(f"{result_array}")
                
                # if np.array_equal(result_array, self.clusters[i].centroid_hist):
                #     # convergence = True
                #     print("Arrays are equal.")
                #else:
                    #print("Arrays are not equal.")
    
                
                
                self.clusters[i].centroid_hist = result_array
                self.clusters[i].centroid_indice = -1
    
                # print(cluster)

        return y





def image_to_matrix(image_path):
    img = Image.open(image_path)
    img_array = np.array(img)
    return img_array


def show_image(images, index):
    plt.imshow(images[index])
    plt.axis('off')
    plt.show()

def show_images_by_indices(images, indices, num_cols=4):
    num_images = len(indices)
    num_rows = int(np.ceil(num_images / num_cols))

    plt.figure(figsize=(24, 16))
    
    for i in range(num_images):
        plt.subplot(num_rows, num_cols, i + 1)
        idx = indices[i]
        plt.imshow(images[idx])
        plt.axis('off')
        plt.title(f'Index: {idx}') 

    plt.tight_layout()  
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

original_labels = []

for file in file_list:
    image_path = os.path.join(path, file)
    image_matrix = image_to_matrix(image_path)

    if file[:3] == 'blu':
        original_labels.append(0)
    elif file[:3] == 'gra':
        original_labels.append(1)
    elif file[:3] == 'gre':
        original_labels.append(2)
    elif file[:3] == 'red':
        original_labels.append(3)
    else: 
        original_labels.append(4)
        
    #print("Image shape:", image_matrix.shape)
    images.append(image_matrix)


images = np.array(images)



# 3. Goruntulerin histogramlarini elde et.

# for index in range(len(file_list)):
#     show_image(images, index)
#     plot_histogram(images[index], "RGB Histogram")
    
    
    
    
from sklearn.metrics import adjusted_rand_score
# from sklearn.metrics import confusion_matrix
from sklearn import metrics

histograms = generate_histograms(images)
histograms_array = np.array(histograms).reshape(len(images), -1)


# Choose k random histograms as initial centroids
k = 5
kmeans = KMeans(histograms_array)
labels = kmeans.fit()

print(original_labels)
print(labels)

ari = adjusted_rand_score(original_labels, labels)
print(ari)

print(kmeans.clusters)


confusion_matrix = metrics.confusion_matrix(original_labels, labels)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix)
cm_display.plot()
plt.show()


indices_by_value = {}

for target_value in range(5):
    indices = [index for index, value in enumerate(labels) if value == target_value]
    indices_by_value[target_value] = indices

# Her bir değere ait indisleri ekrana yazdır
for target_value, indices in indices_by_value.items():
    print(f"{target_value}'e sahip olan indisler:", indices)
    

for i, indeces in indices_by_value.items():
    # # print(indeces)
    # for x in indeces:
    #     print(x)
    
    show_images_by_indices(images, indeces)
    
    



