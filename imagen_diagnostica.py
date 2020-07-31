import numpy as np
import pydicom as pd
import matplotlib.pyplot as plt




ds =pd.dcmread('IMG/IMG10.dcm')
img  = ds.pixel_array

matriz_cero = np.zeros(img.shape, np.uint12)
np.copyto(matriz_cero, img)





