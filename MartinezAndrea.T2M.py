import numpy as np
import matplotlib as plt
class punto():
#punto 1
	def __init__(self,x0,y0):
		self.x=x0
		self.y=y0
		self.r=((self.x**2.0)+(self.y**2.0))**(1.0/2.0)
#punto 2
	def move(self,x1,y1):
		self.x=x+x1
		self.y=y+y1
		self.r=((self.x**2.0)+(self.y**2.0))**(1.0/2.0)
		
#punto 3
	def posicion(self):
		print (self.x),(self.y),(self.r)

algo=punto(6.0,6.0)
algo.posicion()

#punto 4
archivo= open("caminata.txt","w")

#punto 5
px=(np.random.rand()*2)-0.5
py=(np.random.rand()*2)-0.5

while (algo.r<10):
	algo.move(px,py)
#	algo.move()
	
	
	
	



