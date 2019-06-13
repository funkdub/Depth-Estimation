'''
Author: Fengx
用这玩意将灰度 深度图像变成 彩虹图
'''
import cv2
import os

data_path = ''
file_name = '00006l.png'
out_path = 'd/'
im_dir = os.path.join(data_path,file_name)
img = cv2.imread(im_dir)

ht = img.shape[0]
wd = img.shape[1]
for i in range(0,ht):
    for j in range(0,wd):
        B = img[i][j][0]
        G = img[i][j][1]
        R = img[i][j][2]
        if B <= 21:
            img[i][j][0] = 255
        elif B <= 42:
            img[i][j][0] = 255 - (B-21)*5
        elif B <= 63:
            img[i][j][0] = 255 - (B-42)*5
        elif B <= 84:
            img[i][j][0] = 255 - (B-63)*5
        elif B <= 102:
            img[i][j][0] = 255 - (B-84)*5
        elif B <= 126:
            img[i][j][0] = 255 - (B-102)*5
        elif B <= 153:
            img[i][j][0] = 0
        else : img[i][j][0] = 0

        if G <= 21:
            img[i][j][1] = G*5
        elif G <= 42:
            img[i][j][1] = 255
        elif G <= 62:
            img[i][j][1] = 255
        elif G <= 84:
            img[i][j][1] = 255
        elif G <= 102:
            img[i][j][1] = 255
        elif G <= 128:
            img[i][j][1] = 255
        elif G <= 153:
            img[i][j][1] = 255
        elif G <= 204:
            img[i][j][1] = 255 - int(128.0*(G-153.0)/51.0 + 0.5)
        else : img[i][j][1] = 127 - int(127.0*(G-204.0)/51.0 + 0.5)

        if R <= 21:
            img[i][j][2] = 0
        elif R <= 42:
            img[i][j][2] = 0
        elif R <= 63:
            img[i][j][2] = 0
        elif R <= 84:
            img[i][j][2] = 0
        elif R <= 102:
            img[i][j][2] = 0
        elif R <= 128:
            img[i][j][2] = 0
        elif R <= 153:
            img[i][j][2] = (R-102)*5
        elif G <= 204:
            img[i][j][2] = 255
        else : img[i][j][2] = 255
cv2.imwrite(os.path.join(out_path,file_name),img)