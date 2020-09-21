import numpy as np
import cv2
import matplotlib.pyplot as plt
from libgeometrica import *
class Point: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 

def graficar(img,pointsInside,xmax,ymax,xmin,ymin,colorPuntos,colorLinea,thickness,equis,ygriega,valordebusqueda):
	#img = np.zeros([512, 512, 3],np.uint8)
	pointsInside2 = []
	length = len(pointsInside) 
	for i in range(length): 
		if i == len(pointsInside) :
			break
		
		if pointsInside[i][0] <= xmax and pointsInside[i][0] >= xmin and pointsInside[i][1] <= ymax and pointsInside[i][1] >= ymin:
			#pointsInside[i] = ("x","x")
			pointsInside2.append(pointsInside[i])
			print(pointsInside[i])
	#se dibuja el primer circulo
	cv2.circle(img, pointsInside2[0], 10, colorPuntos, thickness) 
	#se dibujan los puntos siguientes
	for index, item in enumerate(pointsInside2):

		if index == len(pointsInside2) -1:
			break
		cv2.circle(img, pointsInside2[index + 1], 10, colorPuntos, thickness) 
		cv2.line(img, item, pointsInside2[index + 1], colorLinea, thickness)
	starpoint = (equis,ygriega)
	endpoint = (equis,ymax) #se arregló esto
	endpoint2 = (equis,ymin)
	interseccion = []
	sentido=0
	
	for index, item in enumerate(pointsInside2): 
		if index == len(pointsInside2) -1:
			break
		# Driver program to test above functions: 
		# print(item)
		p1 = Point(item[0],item[1]) 
		q1 = Point(pointsInside2[index + 1][0], pointsInside2[index + 1][1]) 
		p2 = Point(starpoint[0], starpoint[1]) 
		q2 = Point(endpoint[0],endpoint[1])
		q3 = Point(endpoint2[0],endpoint2[1])
		largo = len(pointsInside2) - 1
		if equis > pointsInside2[largo][0]:
			print("se llegó al final de la hilera")
			break
		
	  
		if doIntersect(p1, q1, p2, q2):
			cv2.line(img, starpoint, endpoint, colorLinea, thickness) 
			sentido=1
			interseccion = line_intersection((starpoint, endpoint), (item, pointsInside2[index + 1]))
			a = np.float32(interseccion[0])
			b = np.float32(interseccion[1])
			cv2.circle(img, (a,b), 10, [0, 255, 100], thickness)
			#print("Yes")
			
			#sprint(pointsInside2[largo][0])
			#se crea un if para detectar si se llego al final de la hilera
			
			if lineMagnitude(a,b,pointsInside2[largo][0],pointsInside2[largo][1]) < valordebusqueda:

				print("se llegó al final de la hilera")
				break
		if doIntersect(p1, q1, p2, q3):
			cv2.line(img, starpoint, endpoint2, colorLinea, thickness)
			sentido=-1
			interseccion = line_intersection((starpoint, endpoint2), (item, pointsInside2[index + 1]))
			a = np.float32(interseccion[0])
			b = np.float32(interseccion[1])
			cv2.circle(img, (a,b), 10, [0, 255, 100], thickness)
			#print("Yes")
			
			#sprint(pointsInside2[largo][0])
			#se crea un if para detectar si se llego al final de la hilera
			
			if lineMagnitude(a,b,pointsInside2[largo][0],pointsInside2[largo][1]) < valordebusqueda:
				print("se llegó al final de la hilera")
				break
				
			
		#else:
		#	return None 
	#se dibuja el punto de referencia
	cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,0,255),3)
	cv2.circle(img, starpoint, 10, [0, 255, 0], thickness)
	#cv2.imshow('Navegacion',img) 
	#print("Aqui grafica!!!!!!!!!!!!!!!!!!!")
	#cv2.waitKey(0)
	plt.imshow(img)
	plt.ion()
	plt.pause(0.01)
	plt.show()

	return (interseccion,sentido)