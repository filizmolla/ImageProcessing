#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:04:53 2024

@author: filiz
"""
def mean(arrays):
    # Dizilerin uzunluğunu kontrol et
    length = len(arrays[0])
    for arr in arrays:
        if len(arr) != length:
            raise ValueError("Dizilerin uzunlukları eşit olmalıdır.")

    # Yeni dizi için boş bir liste oluştur
    result_array = []

    # İndisler üzerinde dönerek ortalamayı hesapla
    for i in range(length):
        current_sum = sum(arr[i] for arr in arrays)
        average = current_sum / len(arrays)
        result_array.append(average)

    print("Ortalama Dizi:", result_array)
    return result_array
    
    
# 44 adet dizi örneği
arrayler = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [41, 42, 43, 44, 45]
]


result_Arr = mean(arrayler)