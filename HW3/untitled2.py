#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:07:24 2024

@author: filiz
"""

import numpy as np

# 44 adet array örneği
arrays = [
    np.array([1, 2, 3, 4, 5]),
    np.array([6, 7, 8, 9, 10]),
    # diğer array'ler
    # ...
    np.array([41, 42, 43, 44, 45])
]

# NumPy stack fonksiyonu ile array'leri birleştir
stacked_arrays = np.stack(arrays)

# Belirtilen eksen (axis=0) üzerinde ortalamayı al
result_array = np.mean(stacked_arrays, axis=0)

print("Ortalama Array:", result_array)
