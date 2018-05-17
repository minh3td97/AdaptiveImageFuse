import numpy as np 
import math

def RGB2HSI(rgb_img):
    m, n, d = rgb_img.shape
    
    hsi_img = np.zeros(rgb_img.shape)
    for i in range(m):
        for j in range(n):
            R = float(rgb_img[i][j][0]/255.0)
            G = float(rgb_img[i][j][1]/255.0)
            B = float(rgb_img[i][j][2]/255.0)

            hsi_img[i][j][2] = (B+G+R)/3  

            b= float(B/(3.0*hsi_img[i][j][2] + 0.000001))
            g=float(G/(3.0*hsi_img[i][j][2] + 0.000001))
            r=float(R/(3.0*hsi_img[i][j][2] + 0.000001))
            numi = 0.5*(r-g + r-b)
            denom = math.sqrt((r-g)**2 + (r-b)*(g-b)) + 0.00001
            w = numi/denom
            if w > 1.0:
                w = 1.0
            elif w < -1.0:
                w = -1.0
            angle = math.acos( w )*180.0/math.pi
            
            if (b<=g):
                hsi_img[i][j][0] = int(angle)
            else:
                hsi_img[i][j][0] = 360.0 - angle
            
            hsi_img[i][j][1] = 1.0 - 3.0*min(b,g,r)

    return hsi_img

def HSI2RGB(hsi_img):
    m, n, d = hsi_img.shape
    rgb_img = np.zeros(hsi_img.shape, dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            
            H = hsi_img[i][j][0]
            S = hsi_img[i][j][1]
            I = hsi_img[i][j][2]
            
            r=g=b=0.0
            
            if I>1.0:
                I = 1.0
            if S > 1.0:
                S = 1.0
            if S == 0:
                rgb_img[i][j][0] = I*255
                rgb_img[i][j][1] = I*255
                rgb_img[i][j][2] = I*255
            else:
                if H >= 0.0 and H < 120.0:
                    b = (1.0-S)/3.0
                    rad = H*math.pi/180.0
                    r = (1.0 + S*math.cos(rad)/math.cos(math.pi/3 - rad))/3.0
                    g = 1.0 - b -r
                elif H>=120.0 and H <240.0:
                    H = H - 120.0
                    r = (1.0-S)/3.0
                    rad = H*math.pi/180.0
                    g = (1.0 + S*math.cos(rad)/math.cos(math.pi/3 - rad))/3.0
                    b = 1.0 - r -g
                else:
                    H = H - 240.0
                    g = (1.0-S)/3.0
                    rad = H*math.pi/180.0
                    b = (1.0 + S*math.cos(rad)/math.cos(math.pi/3 - rad))/3.0
                    r = 1.0 - g -b
                
                
                if r < 0.0:
                    r = 0.0
                if g < 0.0:
                    g = 0.0
                if b < 0.0:
                    b = 0.0
                rgb_img[i][j][0] = 3*I*r*255
                rgb_img[i][j][1] = 3*I*g*255
                rgb_img[i][j][2] = 3*I*b*255
                
                if rgb_img[i][j][0] > 255:
                    rgb_img[i][j][0] = 255
                if rgb_img[i][j][1] > 255:
                    rgb_img[i][j][1] = 255
                if rgb_img[i][j][2] > 255:
                    rgb_img[i][j][2] = 255
                
                
    return rgb_img