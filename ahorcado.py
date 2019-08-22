class Ahorcado ():
	def __init__ (self, no_fallos, palabra):
		self.no_fallos = no_fallos
		self.palabra = palabra
		self.adivinadas = []
		self.ya_gane = False
		self.falle = 0 
		self.ya_perdí = False

	def jugar(self, letra):
		if letra in self.palabra:
			self.adivinadas.append(letra)
			gane = True
			for letra in self.palabra:
				if letra not in self.adivinadas:
					gane = False
				if gane == True:
					self.ya_gane = True
		self.estado()

	def estado (self):
		temp_palabra = ""
		for letra in self.palabra:
			if letra in self.adivinadas:
				temp_palabra += letra
			else:
				temp_palabra = "_"
		print (temp_palabra)
		print ("has cometido %d errores"% (self.falle))

no_fallos = int(input ("Escribe el numero de fallos permitidos "))
palabra = input ("Escribe una palabra ")
ah = Ahorcado(no_fallos, palabra)

while not ah.ya_gane != True:
	if gane != True:
		nueva_letra = input("Ingresa una letra")
		ah.jugar(nueva_letra)
	else:
		print ("Felicidades, has ganado")
		