
from timeit import default_timer as timer

from libgeometrica import *
from graficador import *
from analisis import *


def imagen(equis1, ygriega1):
	#cv2.destroyAllWindows()
	start = timer()
	#se setean los puntos
	print(equis1, ygriega1)
	img = cv2.imread('5.jpeg')
	pointsInside,res = contornos(img)
	#se ordena el arreglo de menor a mayor por la coordenada x.
	pointsInside.sort()
	#pointsInside = [(10, 20), (100, 80), (230, 106), (260, 230), (320, 310), (350, 360), (512,512)]
	#se setea el color de los puntos
	colorPuntos = [0, 0, 255]
	#se setea el color de las lineas
	colorLinea = [255, 0, 0]
	#se setea el grosor de la linea y los puntos
	thickness = 2
	##################Punto referencia#############
	equis = equis1
	ygriega = ygriega1
##############################################
#se definen los valores min y max de el rango permitido
	xmax = 700
	ymax = 500
	xmin = 0
	ymin = 0
#se define el valor de busqueda de siguiente nodo (fin de hilera)
	valordebusqueda = 300
	interseccion = []
#se agregan los valores permitidos a pointsInside2
	interseccion,sentido = graficar(res,pointsInside,xmax,ymax,xmin,ymin,colorPuntos,colorLinea,thickness,equis,ygriega,valordebusqueda)
#print("hola")
#print(interseccion)
#se muestran por pantalla las salidas
#las coordenadas del punto de referencia
	print("punto de referencia: (" + str(equis) + "," + str(ygriega) + ")")
#las coordenadas del punto de interseccion

#if (equis < res2[0] or equis > res1[0]) or (igriega < res2[1] ) or (igriega > res1[1]):
	if len(interseccion) != 0:
		print("punto de interseccion: (" + str(interseccion[0]) + "," + str(interseccion[1]) + ")")	
		# printing result  
		#la distancia entre el punto central de la linea y el punto de referencia
		print("Distancia entre el punto central de la linea y el punto de referencia")
		DistanciaFinal = lineMagnitude(equis,ygriega,interseccion[0],interseccion[1])
		print(DistanciaFinal*sentido)
	else:
#except NameError:
		print("no intersecta")	



	print("tiempo de ejecución en segundos")
	end = timer()
	print(end - start)
	#cv2.waitKey(delay=20)
	cv2.destroyAllWindows()
	print("Fin de main estados!!!!!!!!!!!") 
	return