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


img = cv2.imread("image/21_MS.png")

down_img = cv2.blur(img,(3,3))

cv2.imwrite("image/21_MS(b).png", down_img)