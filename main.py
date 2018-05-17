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

ms_img = cv2.imread("image/2_MS(o).png")
pan_img = cv2.imread("image/2_PAN.png", 0)


def getIfromHSI(HSI_img):
    m,n,d = HSI_img.shape
    img = np.zeros((m, n), dtype=np.uint8)
    for i in range(m):
        for j in range(n):
            img[i][j] =HSI_img[i][j][2]*255

    return img

def editI2HSI(HSI_img, I):
    hsi_img = HSI_img
    m, n, d = HSI_img.shape

    for i in range(m):
        for j in range(n):
            hsi_img[i][j][2] = I[i][j]/255.0

    return hsi_img

ms_resample_img = resample.upSample(ms_img)
cv2.imwrite("resample/2.png", ms_resample_img)
hsi_img = convert.RGB2HSI(ms_resample_img)
I = getIfromHSI(hsi_img)
pnew = hm.histogram_match(pan_img, I)
Inew = rws.replaceWithSsim(I, pnew)
hsi_new = editI2HSI(hsi_img, Inew)

rgb_result_img = convert.HSI2RGB(hsi_new)

cv2.imwrite("result/result_2.png", rgb_result_img)


