'''
Author: Fengx
使用imgviz将深度图像着色
'''
import cv2
import os
import glob
import imgviz
import numpy as np

paths = glob.glob('C:/Users/fengxin_sx/Desktop/d/*.png')
index = 0
for data_path in paths:
    file_name = data_path.split('\\')[-1]
    
    depth = cv2.imread(data_path)
    depth = cv2.cvtColor(depth,cv2.COLOR_RGB2GRAY)
    depth = cv2.resize(depth, (912,684),interpolation=cv2.INTER_CUBIC)
    depth = np.array(depth/255,dtype=np.float32)
    depthviz = imgviz.depth2rgb(depth, min_value=0.2, max_value=1)
    cv2.imshow('1',depthviz)
    cv2.waitKey(0)
    
    #data_path = ''
    #file_name = '00006l.png'
    out_path = 'C:/Users/fengxin_sx/Desktop/d/dd/'
    cv2.imwrite(os.path.join(out_path,str(index))+'.png',depthviz)
    index += 1