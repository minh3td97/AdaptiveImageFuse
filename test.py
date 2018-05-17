import cv2
import numpy as np 
import math
import os
np.seterr(over='ignore')
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt

import resample
import histogram as h
import cumulative_histogram as ch
import convert 
import histogram_matching as hm
import replaceWithSsim as rws


img = cv2.imread("image/2_MS.png")

down_img = resample.downSample(img)

cv2.imwrite("image/2_MS(o).png", down_img)