#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 16:57:59 2024

@author: filiz
"""

import numpy as np

# Örnek diziler
import numpy as np

# Örnek diziler
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
array3 = np.array([11, 12, 13, 14, 15])
array4 = np.array([16, 17, 18, 19, 20])

# Dizilerin aynı indislerinin ortalamasını al
mean_array = np.mean([array1, array2, array3, array4], axis=0)

print(mean_array)

