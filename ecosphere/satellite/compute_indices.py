import numpy as np

def compute_ndvi(nir, red):
    return (nir - red) / (nir + red + 1e-8)

def compute_ndwi(green, nir):
    return (green - nir) / (green + nir + 1e-8)
