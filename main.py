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

ms_img = cv2.imread("image/3_MS.png")
pan_img = cv2.imread("image/3_PAN.png", 0)


def getIfromHSI(HSI_img):
    m,n,d = HSI_img.shape
    img = np.zeros((m, n), dtype=np.uint8)
    for i in range(m):
        for j in range(n):
            img[i][j] =HSI_img[i][j][2]*255
    #print("I: " + str(img))
    return img

def editI2HSI(HSI_img, I):
    hsi_img = HSI_img
    m, n, d = HSI_img.shape

    for i in range(m):
        for j in range(n):
            #print("hsi_I: ")
            hsi_img[i][j][2] = I[i][j]/255.0

    return hsi_img


hsi_img = convert.RGB2HSI(ms_img)
I = getIfromHSI(hsi_img)
pnew = hm.histogram_match(pan_img, I)
Inew = rws.replaceWithSsim(I, pnew, win_size=7)
hsi_new = editI2HSI(hsi_img, Inew)

#result_img 
rgb_result_img = convert.HSI2RGB(hsi_new)
cv2.imwrite("result/result_3.png", rgb_result_img)

# combine MS_img and result_img 
combine_img = np.concatenate((ms_img, rgb_result_img), axis=1)
cv2.imwrite("combine/combine_3.png", combine_img)


