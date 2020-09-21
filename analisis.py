import cv2
import numpy as np
from matplotlib import pyplot as plt
def contornos(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Se convierte imagen a hsv
    #arreglo para guardar las cordenadas finales
    pointsInside = []





    #///////////componentes imagenes/////////////

    #h,s,v = cv2.split(hsv)
    b,g,r = cv2.split(img)
    b1=0
    r1=0
    #//////////filtrado imagen///////

    #print("b=",b,"g=",g,"r=",r)
    g1=g
    g2=2*g-b-r
    E=g2+b1+r1

    #if (g2>=r1 & g2>=b1 & g2>=120)
    #a=np.shape(g2)
    #print(a)
    #print("E=",E)
    #grayscaled = cv2.cvtColor(E,cv2.COLOR_BGR2GRAY)

    retval, threshold = cv2.threshold(E, 200,255 , cv2.THRESH_BINARY_INV)
    kernel = np.ones((5,5),np.uint8)
    #sobelx = cv2.Sobel(threshold,cv2.CV_64F,1,0,ksize=5)
    erosion = cv2.erode(threshold,kernel,iterations = 2)
    # #lower_red = np.array([40,0,0])
    # #upper_red = np.array([255,255,255])
    # #mask = cv2.inRange(hsv, lower_red, upper_red)
    # #res = cv2.bitwise_and(img,img, mask= mask)
    # #grayscaled = cv2.cvtColor(E,cv2.COLOR_BGR2GRAY)

    contours, _ = cv2.findContours(erosion, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    res = cv2.bitwise_and(img,img, mask= erosion)

    # cv2.drawContours(res, contours, -1, (0, 255, 0), 3)
    print("numero de contornos ="  + str(len(contours)))

    #print(contours[0])
    #x,y,w,h = cv2.boundingRect(contours[4])


    # cnt = contours[3]
    # M = cv2.moments(cnt)
    # x,y,w,h = cv2.boundingRect(cnt)
    # cv2.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)
    # print ("momento =", M)
    # cx = int((M['m10']/M['m00']))
    # cy = int((M['m01']/M['m00']))

    # cv2.circle(res,(cx, cy), 5, (0,0,255), -1)



    #cv2.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)
    #cv2.drawContours(res, contours[2], -1, (0, 255, 0), 3)
    ##############################################################################
    for contour in contours:
        area = cv2.contourArea(contour)
        #print ('area =', area)
        if area > 200:  # Definicion para eleccion de imagen
            M = cv2.moments(contour)
            cx = int((M['m10']/M['m00']))
            cy = int((M['m01']/M['m00']))
            x,y,w,h = cv2.boundingRect(contour)
            cv2.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(res,(cx, cy), 5, (0,0,255), -1)
            #print("centro =", cx, cy)
            pointsInside.append((cx,cy))

    # #     cv2.drawContours(res, contour, -1, (0, 255, 0), 3)
    # ###########////centro del rectangulo
    #              centro=cv2.rectangle(res,(x,y),(x+w,y+h),(255,0,0),2)
    #              #print("centro",centro)
    ################################################################################
    #cv2.imshow('E',E)
    #cv2.imshow('img',img)
    #cv2.imshow('erosion',erosion)

    #cv2.imshow('contours',contours)
    #cv2.imshow('res',res)
    #cv2.imshow('grayscaled',grayscaled)

    #cv2.imshow('threshold',threshold)
    #cv2.imshow('h',h)
    #cv2.imshow('s',s)
    #cv2.imshow('v',v)
    #cv2.imshow('b',b)
    #cv2.imshow('g',g)
    #cv2.imshow('r',r)
    #print("aqui################")
    #//////////////Esperar a tecla para cerrar////////////
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return(pointsInside,res)
    ########Histogramas#########

    #plt.hist(E.ravel(), 256, [0,256])
    #plt.hist(b.ravel(), 256, [0,256])
    #plt.hist(g.ravel(), 256, [0,256])
    #plt.hist(r.ravel(), 256, [0,256])

    #plt.show()
#img = cv2.imread('5.jpeg')
#print(contornos(img))