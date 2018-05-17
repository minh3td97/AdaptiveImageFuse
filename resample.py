import numpy as np 
import math

def downSample(image):
    m, n, d = image.shape
    im = np.zeros(( int(m/2), int(n/2), d), dtype=np.uint8)
    
    for i in range( int(m/2)):
        for j in range(int(n/2)):
            im[i][j] = image[i*2][j*2]
    return im


def upSample(image):
    m, n, d = image.shape
    im = np.zeros((m*2, n*2, d), dtype=np.uint8)
    
    for i in range(m*2):
        for j in range(n*2):
            im[i][j] = image[int(i/2)][int(j/2)]
    return im