import numpy as np
from scipy.signal import gaussian

def gaussian_filter(y_size, x_size, sigma):
    ret =  np.outer(gaussian(y_size, sigma), gaussian(x_size, sigma))
    return ret / np.sum(ret)

def mexican_hat(x_size,y_size,width):
    '''generate a 2D-mexican hat filter'''
    x_linear=np.arange(-np.floor(x_size/2.0),np.ceil(x_size/2.0))
    y_linear=np.arange(-np.floor(y_size/2.0),np.ceil(y_size/2.0))
    x_grid, y_grid = np.meshgrid(x_linear,y_linear)
    t = np.sqrt(x_grid**2 + y_grid**2)

    mexican = 2.0 / np.sqrt(3.0) / width / np.pi**(1/4) * (1-1/2.0*t**2/width**2) \
            * np.exp(-t**2/2/width**2) 
    return np.real(mexican)
