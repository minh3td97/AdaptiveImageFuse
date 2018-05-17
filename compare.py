import cv2
import numpy as np 
import math

img1 = cv2.imread("resample/22.png")
img2 = cv2.imread("result/result_22.png")

m, n, d = img1.shape

for i in range(m):
    for j in range(n):
        dr = int(img1[i][j][0]) - int(img2[i][j][0])
        dg = int(img1[i][j][1]) - int(img2[i][j][1])
        db = int(img1[i][j][2]) - int(img2[i][j][2])
        dist = math.sqrt(dr**2 + dg**2 + db**2)
        if dist>50:
            print(dist)
            print(img1[i][j])
            print(img2[i][j])
            print(".")