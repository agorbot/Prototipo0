# -*- coding: utf-8 -*-
# Load the opencv library and drawing tools
# ------------------------------------------------------
import cv2
import matplotlib.pyplot
import numpy as np
from PIL import Image
import math

cap = cv2.VideoCapture('Video1variable-1.m4v')
#image = cv2.imread('diegoxxxxxxx.jpg')
#cv2.imshow("images",image)



while(cap.isOpened()):
    ret, frame = cap.read()

    ##===================cambio de dimenciones===============    
    height , width , layers =  frame.shape
    new_h=300
    new_w=500
    frame = cv2.resize(frame, (new_w, new_h)) 
##=======================================================

    norm=np.zeros((new_h,new_w,layers),np.float32)
    norm_rgb=np.zeros((new_h,new_w,layers),np.uint8)
    b=frame[:,:,0]
    g=frame[:,:,1]
    r=frame[:,:,2]
    sum=b+g+r
    norm[:,:,0]=(b/sum)*255.0
    norm[:,:,1]=(g/sum)*255.0
    norm[:,:,2]=(r/sum)*255.0
    


    norm_rgb=cv2.convertScaleAbs(norm)
    #se convierte a uint8
    b_n=norm_rgb[:,:,0]
    g_n=norm_rgb[:,:,1]
    r_n=norm_rgb[:,:,2]

##============se calculan los indices===============

    exg = 2 * g- r - b   #######Exg sin normalizar
    exr = 1.3*r_n-g_n
    exgr = exg-exr
    mexg = 1.262*g_n-0.884*r_n-0.311*b_n
    sumaton=0.000000001
    #sumaton=1
    veg = g_n / ((r_n ** 0.667) * (b_n ** (1 - 0.667))+sumaton)
    cive = 0.441 * r_n - 0.811 * g_n + 0.385 * b_n + 18.75
    Indice_comb_1 = 0.25 * exg + 0.3 * exgr + 0.33 * cive + 0.12 * veg
    COM2= 0.36*exg+0.47*cive+0.17*veg 
    
##====================================================
##====================================================
    #hsv_green = cv2.cvtColor(exg, cv2.COLOR_GRAY2RGB)
    #hsv_green = cv2.cvtColor(hsv_green,cv2.COLOR_BGR2HSV)
    
##==================Filtros===========================
   
    #kernel = np.ones((3,3),np.float32)/9
    #blurred = cv2.filter2D(exg,-1,kernel)
    #bilateral=cv2.bilateralFilter(exg,10,1,1)
    #cv2.imshow("bilateralFilter",bilateral)
    blurred=cv2.blur(exg, (5,5),0.0001) 
    #blurredgaus=cv2.GaussianBlur(blurred, (5,5),0.0001) 
    
    #gaussiano = cv2.GaussianBlur(blurred,(5,5),cv2.BORDER_DEFAULT)
    
    #sobelx = cv2.Sobel(threshold,cv2.CV_64F,1,0,ksize=5)

    kernel = np.ones((1,1),np.uint8)
    erosion = cv2.erode(blurred,kernel,iterations = 2)
    #sobel  = cv2.Sobel(blurred,cv2.CV_64F,1,0,ksize=5)
    #erosion=cv2.blur(erosion, (5,5),0.0001)
##=====================COnversion 8 bits====================

    #out = mexg
    processedimg = cv2.convertScaleAbs(erosion) # Convierte a 8 bits
    erosion_negado = cv2.bitwise_not(processedimg)  # NIega los pixeles

##==========================Threshold====================
   
    #======otsu erosion
    ret2,otsux = cv2.threshold(erosion_negado,0,255,cv2.THRESH_OTSU)  
    print("otsux",otsux)
    #======mean
##==========================================================


##==========================Segunda capa====================
    blurred_salida=cv2.blur(otsux, (5,5),0.0001) 

    kernel_2 = np.ones((2,2),np.uint8)
    erosion_2 = cv2.erode(blurred_salida,kernel_2,iterations = 1)

##=====================Conversion 8 bits====================

    #out = mexg
    processedimg_2 = cv2.convertScaleAbs(erosion_2) # Convierte a 8 bits
    #erosion_negado_2 = cv2.bitwise_not(processedimg_2)  # NIega los pixeles

##==========================Threshold 2====================
   
    #======otsu erosion
    ret2,otsux_2 = cv2.threshold(processedimg_2,0,255,cv2.THRESH_OTSU)  
    #======mean

##==========================================================

##==================================================== 
##================FIND CONTOURS=======================
    #contours, _ = cv2.findContours(erosion, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours, _ = cv2.findContours(otsux, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        #print ('area =', area)
        if area < (new_h*new_h)/100:  # Definicion para eleccion de imagen
            #M = cv2.moments(contour)
            #cx = int((M['m10']/M['m00']))
            #cy = int((M['m01']/M['m00']))
            
            x,y,w,h = cv2.boundingRect(contour)
            #cv2.rectangle(otsux,(x,y),(x+w,y+h),(255,255,255),-1)
            
            #cv2.circle(otsux,(cx, cy), 5, (0,0,255), -1)
            #print("centro =", cx, cy)
            #pointsInside.append((cx,cy))
            #print("contornos", contours)
            #v2.fillPoly(otsux, area, color=(255,255,255))
            #cv2.drawContours(otsux, contour, -1, (0,255,0), -1)
            cv2.fillConvexPoly(otsux, contour, color=(255,255,255))
    cv2.imshow("otsux",otsux)
    print("coordenadas", otsux)

##==================================================== 

  ##===================Adaptativo=====================
    #th2 = cv2.adaptiveThreshold(exg_negado,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    #otsux = cv2.adaptiveThreshold(erosion_negado,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    #adaptiveThreshold(exg_negado, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C)
##==================================================

##==============Conversion a 8 bit RGB===============

    #convertido = cv2.convertScaleAbs(blurred)

    frame8bits = cv2.convertScaleAbs(frame)  
    otsuxRGB = cv2.cvtColor(otsux, cv2.COLOR_GRAY2RGB)
    otsuxRGB_2 = cv2.cvtColor(otsux_2, cv2.COLOR_GRAY2RGB)
    #print("frame8bits",type(frame8bits[0,0,0]))
    #print("otsux",type(otsux[0,0]))
    
    ##########Juntar imagenes con and ############

    #salidia = cv2.bitwise_and(frame8bits, convertido)
    outputx= cv2.bitwise_and(frame8bits, otsuxRGB)
    outputx_2= cv2.bitwise_and(frame8bits, otsuxRGB_2)

    
##===============================================


    cv2.rectangle(frame,(20,20),(30,30),(0,255,0),2)

##================Mostrar imagenes===============
    
    
    cv2.imshow("salida_frame",frame)
    cv2.imshow("otsux_2",otsux_2)
    cv2.imshow("erosion",erosion)    
    cv2.imshow("salida_erosion",outputx)
    cv2.imshow("outputx_2",outputx_2)
        
    #cv2.imshow("th3",th3)
    #cv2.imshow("exg",blurred)
    #cv2.imshow("mexg",mexg)
#    cv2.imshow("images",outputx)

##===============================================

    #cv2.imshow("imagesframe",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()