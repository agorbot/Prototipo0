from random import randint
import time 
from main_estados import imagen  

import serial

##======================================

uno = serial.Serial('/dev/ttyUSB0',9600,timeout=None)
time.sleep(2)

#####Maquina de estados finita##########


#######Que hace cada estado######

State = type("State",(object,),{})

class Analisis(State):
	def Execute(self):
		print("Analisis de imagen")
		for i in range(0,2):
			x=50
			y=50
			print("xixixix,y",x,y)
			x=x*i
			y=y*i
			print("iii",i)
			print("xxx,yyy",x,y)
			time.sleep(1)
			imagen(x,y) ########################


class Comunicacion(State):
	def Execute(self):
		print("En Estado comunicación con micro")
		uno.write(b'1') # Escribir(0)
		llegada1 = uno.read(3)
		if llegada1 == b'1\r\n':   #si llegada = '1' ('1\r\n'), 
			print("Se recibio lo esperado")
		print("#=========================#")
		#equis=i*60
		#ygriega1=i*50
##======================================




######## Transicion ########
class Transition1(object):
	def __init__(self,toState):
		self.toState=toState

	def Execute(self):
		print("Transicionando")

##======================================
######## Maquina #########
class SimpleFSM(object):
	def __init__(self, char):
		
		self.char=char    	   # Caracter entregado
		self.states={}         # Se guardan los estados
		self.transitions={}	   # Se guardan transiciones
		self.curState=None     # Estado actual
		self.trans=None        # Transicion actual

	def SetState(self,stateName):  #Busca el string que se le pasa dentro de el diccionario de estados
		self.curState=self.states[stateName]

	def Transition(self,transName):
		self.trans=self.transitions[transName]

	def Execute(self):
		if(self.trans):
			self.trans.Execute()
			self.SetState(self.trans.toState)
			self.trans = None
		self.curState.Execute()

##==========================================
############Definicion inicial maquina######
class Char(object):
	"""docstring for Char"""
	def __init__(self):
		self.FSM=SimpleFSM(self)
		self.Analisis = True
##==========================================
#if __name__== "__main__":

#1._ Definicion de maquina de estados
light = Char()

#2._ llenado de diccionario de estados, con nombre y apuntando al estado
light.FSM.states["Analisis"]=Analisis()
light.FSM.states["Comunicacion"]=Comunicacion()

#3._ llenado de diccionario de transiciones
light.FSM.transitions["A_Analisis"]=Transition1("Analisis")
light.FSM.transitions["A_Comunicacion"]=Transition1("Comunicacion")

#4._ Setear Estado inicial 
light.FSM.SetState("Analisis")




for i in range(10):
	if(light.Analisis):
		light.FSM.Transition("A_Comunicacion")
		light.Analisis=False	
	else:
		light.FSM.Transition("A_Analisis")
		light.Analisis=True
		light.FSM.Execute()






for i in range(10):
	startTime=time.process_time()
	timeInterval=1
	while(startTime + timeInterval>time.process_time()):
		pass
	if(randint(0,2)):
		if(light.Analisis):
			light.FSM.Transition("A_Comunicacion")
			light.Analisis=False	
		else:
			light.FSM.Transition("A_Analisis")
			light.Analisis=True
		light.FSM.Execute()

##==========================================
