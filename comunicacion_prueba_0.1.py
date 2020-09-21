## Comunicación con microcontrolador, envía un byte al microcontrolador --> uno.write(b'1')
##

import serial
import time
import sys

uno = serial.Serial('/dev/ttyUSB0',9600,timeout=None)
time.sleep(2)



def led_off(datos):

	print("hola off")
	print("datos", datos)
	uno.write(datos) # Escribir
	
	print("enviado=============")
	time.sleep(2)
	#uno.close()
	#time.sleep(2)
	print("ahora si quedo libre")
	llegada = uno.read(6)
	print(llegada[0]) 
	print(llegada[1])
	print(llegada[2])
	print(llegada[3])
	print(llegada[4])
	print(llegada[5])
	if llegada[0] == 60:
		print("El valor es igual a = <")
		valor = ((llegada[2]-48)*100)+((llegada[3]-48)*10)+(llegada[4]-48)
		print(valor)
		print("llegada = >")


# 	llegada = uno.read(5)

# 	print("llegada = ", llegada[0])
# 	print("tipo llegada", type(llegada[4]))
# 	print("tipo llegada", len(llegada))
# 	if llegada[4] == 10:
# 		print("Sisisisi")


n=-306
tres = str(n)
inicio = "<"
fin = ">"
mensaje = inicio + tres + fin
mensaje_byte = mensaje.encode('ascii')
print (mensaje_byte)
print("mensaje--- = ",type(mensaje_byte))
######Lectura para envios#####
# 60 = <
# 62 = > 

#n=400

# enviar = bytearray(4)
# enviar[0] = 60
# print (enviar)
# print (type(enviar))
# enviar[1:2] = n
# enviar[3] = 62
# print (enviar)

#for i in range(10):
#	led_on()

led_off(mensaje_byte)
# print("#========================#")