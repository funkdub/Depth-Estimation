#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
"""
Author:Fengx
用这玩意儿放大图像
"""
 
__author__ = 'zj'
 
import cv2
import os
 
if __name__ == '__main__':
    img = cv2.imread("00006.png", -1)
    if img.all()==None:
        print("Error: could not load image")
        os._exit(0)
    
    height, width = img.shape[:2]
 
    # 缩小图像
    size = (int(width*0.3), int(height*0.5))
    shrink = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
    
    # 放大图像
    fx = 10
    fy = 10
    # 304 228
    enlarge = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
    #enlarge = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_LANCZOS4)
    #enlarge = cv2.resize(img, (0, 0), fx=fx, fy=fy, interpolation=cv2.INTER_CUBIC)
    # 显示
    cv2.imwrite('00006l.png',enlarge)
    cv2.imshow("src", img)
    cv2.imshow("shrink", shrink)
    cv2.imshow("enlarge", enlarge)
 
    cv2.waitKey(0)
