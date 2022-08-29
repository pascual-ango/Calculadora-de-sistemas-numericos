from tkinter import *
from conversor import Conversor

class Calculadora:
	def __init__(self, Conversor):
		self.ventana = Tk()
		self.ventana.title("Conversora")
		self.ventana.config(padx=25, pady=25)
		self.calculadora = Conversor
		self.pantalla1 = Entry(width=5)
		self.pantalla1.grid(row=0, column=0)

		self.pantalla2 = Entry(width=49)
		self.pantalla2.grid(row=0, column=1, columnspan=5)

		self.resultado1 = Entry(width=5)
		self.resultado1.grid(row=1, column=0)

		self.resultado2 = Entry(self.ventana, width=49,justify="right")
		self.resultado2.grid(row=1, column=1, pady=(10, 10), columnspan=5)

		self.botones1 = []	# '#{system}' buttons-> firs line of buttons
		self.botones2 = []	# Digits
		self.botones3 = []	# Buttons: Convert to #{system}
		self.binario = []
		self.cuartario = []
		self.quintal = []
		self.octal = []
		self.decimal = []
		self.hexadecimales = []
		self.crear_botones()
		self.numero = ""
		self.sistema_actual = 0
		self.sistema_a_pasar = 0
		self.ventana.mainloop()

	def crear_botones(self):
		"""Create the screen's buttons"""
		for i in range(6):
			boton = Button(width=4)
			boton.grid(row=2, column=i)
			self.botones1.append(boton)
		#Digits
		for i in range(3):
			for j in range(6):
				boton = Button(width=4, state="disabled")
				boton.grid(row=j+3, column=i)
				self.botones2.append(boton)
		##buttons: Convert to #{system}
		for i in range(6):
			boton = Button(width=21, state="disabled")
			boton.grid(column=3, row=i+3, columnspan=3)
			self.botones3.append(boton)
		##systems
		self.botones1[0].config(text="#2", command=self.activar_2)
		self.botones1[1].config(text="#4", command=self.activar_4)
		self.botones1[2].config(text="#5", command=self.activar_5)
		self.botones1[3].config(text="#8", command=self.activar_8)
		self.botones1[4].config(text="#10", command=self.activar_10)
		self.botones1[5].config(text="#16", command=self.activar_16)
		##Hexadecimal's letters
		self.botones2[0].config(text="D", command=self.imprimir_D)
		self.botones2[6].config(text="E", command=self.imprimir_E)
		self.botones2[12].config(text="F", command=self.imprimir_F)
		self.botones2[1].config(text="A", command=self.imprimir_A)
		self.botones2[7].config(text="B", command=self.imprimir_B)
		self.botones2[13].config(text="C", command=self.imprimir_C)
		##numbers
		self.botones2[2].config(text="7", command=self.imprimir_7)
		self.botones2[3].config(text="4", command=self.imprimir_4)
		self.botones2[4].config(text="1", command=self.imprimir_1)
		self.botones2[8].config(text="8", command=self.imprimir_8)
		self.botones2[9].config(text="5", command=self.imprimir_5)
		self.botones2[10].config(text="2", command=self.imprimir_2)
		self.botones2[11].config(text="0", command=self.imprimir_0)
		self.botones2[14].config(text="9", command=self.imprimir_9)
		self.botones2[15].config(text="6", command=self.imprimir_6)
		self.botones2[16].config(text="3", command=self.imprimir_3)
		self.botones2[5].config(text="C", command=self.borrar)
		self.botones2[17].config(text="CC", command=self.limpiar)
		##convert's buttons
		self.botones3[0].config(text="Convert to #2", command=self.convertir_a_binario)
		self.botones3[1].config(text="Convert to #4", command=self.convertir_a_cuartario)
		self.botones3[2].config(text="Convert to #5", command=self.convertir_a_quintal)
		self.botones3[3].config(text="Convert to #8", command=self.convertir_a_octal)
		self.botones3[4].config(text="Convert to #10", command=self.convertir_a_decimal)
		self.botones3[5].config(text="Convert to #16", command=self.convertir_a_hexadecimal)
		#binary's numbers
		self.binario.append(self.botones2[11])
		self.binario.append(self.botones2[4])

		#forth numbers
		for i in range(4, 17):
			if i == 11 or i == 10 or i == 4 or i == 16:
				self.cuartario.append(self.botones2[i])
		#base five system numbers
		for i in range(3, 17):
			if i == 11 or i == 10 or i == 4 or i == 16 or i == 3:
				self.quintal.append(self.botones2[i])
		#octal numbers
		for i in range(2, 17):
			if (i > 4 and i < 9) or (i > 11 and i < 15):
				continue
			else:
				self.octal.append(self.botones2[i])
		#decimal numbers
		for i in range(2, 17):
			if i == 5 or i == 6 or i == 7 or i==12 or i == 13:
				continue
			else:
				self.decimal.append(self.botones2[i])
		#hexadecimal numbers
		self.hexadecimales = self.botones2

		#------------Funciones ----------------#
	def borrar(self):
		"""Delete a digit on the screen"""
		self.pantalla2.delete(len(self.pantalla2.get()) - 1, "end")

	def limpiar(self):
		"""Clean the screen"""
		self.resultado1.delete(0, "end")
		self.resultado2.delete(0, "end")
		self.pantalla2.delete(0, "end")

	#The piece of code below is for activate buttons depending on the current activated system
	def activar_2(self):
		"""Active binary numbers"""
		for i in range(len(self.cuartario)):
			self.cuartario[i].config(state="disabled")
		for i in range(len(self.quintal)):
			self.quintal[i].config(state="disabled")
		for i in range(len(self.decimal)):
			self.decimal[i].config(state="disabled")
		for i in range(len(self.hexadecimales)):
			self.hexadecimales[i].config(state="disabled")
		for i in range(len(self.octal)):
			self.octal[i].config(state="disabled")
		for i in range(len(self.binario)):
			self.binario[i].config(state="active")
		for i in range(len(self.botones3)):
			self.botones3[i].config(state="active")
		self.botones2[5].config(state="active")
		self.botones2[17].config(state="active")
		self.pantalla1.delete(0, "end")
		self.pantalla1.insert(0, "N(2)")
		self.limpiar()
		self.sistema_actual = 2

	def activar_4(self):
		"""Activate forth base numbers"""
		for i in range(len(self.binario)):
			self.binario[i].config(state="disabled")
		for i in range(len(self.quintal)):
			self.quintal[i].config(state="disabled")
		for i in range(len(self.decimal)):
			self.decimal[i].config(state="disabled")
		for i in range(len(self.hexadecimales)):
			self.hexadecimales[i].config(state="disabled")
		for i in range(len(self.octal)):
			self.octal[i].config(state="disabled")
		for i in range(len(self.cuartario)):
			self.cuartario[i].config(state="active")
		for i in range(len(self.botones3)):
			self.botones3[i].config(state="active")
		self.botones2[5].config(state="active")
		self.botones2[17].config(state="active")
		self.pantalla1.delete(0, "end")
		self.pantalla1.insert(0, "N(4)")
		self.limpiar()
		self.sistema_actual = 4

	def activar_5(self):
		"""Activate five base numbers"""
		for i in range(len(self.binario)):
			self.binario[i].config(state="disabled")
		for i in range(len(self.cuartario)):
			self.cuartario[i].config(state="disabled")
		for i in range(len(self.decimal)):
				self.decimal[i].config(state="disabled")
		for i in range(len(self.hexadecimales)):
			self.hexadecimales[i].config(state="disabled")
		for i in range(len(self.octal)):
			self.octal[i].config(state="disabled")
		for i in range(len(self.quintal)):
			self.quintal[i].config(state="active")
		for i in range(len(self.botones3)):
			self.botones3[i].config(state="active")
		self.botones2[5].config(state="active")
		self.botones2[17].config(state="active")
		self.pantalla1.delete(0, "end")
		self.pantalla1.insert(0, "N(5)")
		self.limpiar()
		self.sistema_actual = 5

	def activar_8(self):
		"""Active eight base numbers"""
		for i in range(len(self.binario)):
			self.binario[i].config(state="disabled")
		for i in range(len(self.cuartario)):
			self.cuartario[i].config(state="disabled")
		for i in range(len(self.quintal)):
			self.quintal[i].config(state="disabled")
		for i in range(len(self.decimal)):
			self.decimal[i].config(state="disabled")
		for i in range(len(self.hexadecimales)):
			self.hexadecimales[i].config(state="disabled")
		for i in range(len(self.octal)):
			self.octal[i].config(state="active")
		for i in range(len(self.botones3)):
			self.botones3[i].config(state="active")
		self.botones2[5].config(state="active")
		self.botones2[17].config(state="active")
		self.pantalla1.delete(0, "end")
		self.pantalla1.insert(0, "N(8)")
		self.limpiar()
		self.sistema_actual = 8

	def activar_10(self):
		"""Activate decimal numbers"""
		for i in range(len(self.binario)):
			self.binario[i].config(state="disabled")
		for i in range(len(self.cuartario)):
			self.cuartario[i].config(state="disabled")
		for i in range(len(self.quintal)):
			self.quintal[i].config(state="disabled")
		for i in range(len(self.octal)):
			self.octal[i].config(state="disabled")
		for i in range(len(self.hexadecimales)):
			self.hexadecimales[i].config(state="disabled")
		for i in range(len(self.decimal)):
			self.decimal[i].config(state="active")
		for i in range(len(self.botones3)):
			self.botones3[i].config(state="active")
		self.botones2[5].config(state="active")
		self.botones2[17].config(state="active")
		self.pantalla1.delete(0, "end")
		self.pantalla1.insert(0, "N(10)")
		self.limpiar()
		self.sistema_actual = 10

	def activar_16(self):
		"""Activate hexadecimal numbers"""
		for i in range(len(self.binario)):
			self.binario[i].config(state="disabled")
		for i in range(len(self.cuartario)):
			self.cuartario[i].config(state="disabled")
		for i in range(len(self.quintal)):
			self.quintal[i].config(state="disabled")
		for i in range(len(self.decimal)):
			self.decimal[i].config(state="disabled")
		for i in range(len(self.octal)):
			self.octal[i].config(state="disabled")
		for i in range(len(self.hexadecimales)):
			self.hexadecimales[i].config(state="active")
		for i in range(len(self.botones3)):
			self.botones3[i].config(state="active")
		self.botones2[5].config(state="active")
		self.botones2[17].config(state="active")
		self.pantalla1.delete(0, "end")
		self.pantalla1.insert(0, "N(16)")
		self.limpiar()
		self.sistema_actual = 16

	def imprimir_1(self):
		"""Print '1' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "1")

	def imprimir_2(self):
		"""Print '2' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "2")

	def imprimir_3(self):
		"""Print '3' on the screens"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "3")

	def imprimir_4(self):
		"""Print '4' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "4")

	def imprimir_5(self):
		"""Print '5' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "5")

	def imprimir_6(self):
		"""Print '6' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "6")

	def imprimir_7(self):
		"""Print '7' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "7")

	def imprimir_8(self):
		"""Print '8' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "8")

	def imprimir_9(self):
		"""Print '9' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "9")

	def imprimir_0(self):
		"""Print '0' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "0")

	def imprimir_A(self):
		"""Print 'A' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "A")

	def imprimir_B(self):
		"""Print 'B' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "B")

	def imprimir_C(self):
		"""Print 'C' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "C")

	def imprimir_D(self):
		"""Print 'D' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "D")

	def imprimir_E(self):
		"""Print 'E' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "E")

	def imprimir_F(self):
		"""Print 'F' on the screen"""
		if self.resultado1.get() != "":
			self.limpiar()
		self.pantalla2.insert(len(self.pantalla2.get()), "F")

	def convertir_a_binario(self):
		"""Convert to binary"""
		self.numero = self.pantalla2.get()
		self.sistema_a_pasar = 2
		self.resultado1.delete(0, "end")
		self.resultado1.insert(0, "N(2)")
		self.resultado2.delete(0, "end")
		self.resultado2.insert(0, self.calculadora.conversion(self.numero, self.sistema_actual, self.sistema_a_pasar))

	def convertir_a_cuartario(self):
		"""Convert to forth system"""
		self.numero = self.pantalla2.get()
		self.sistema_a_pasar = 4
		self.resultado1.delete(0, "end")
		self.resultado1.insert(0, "N(4)")
		self.resultado2.delete(0, "end")
		self.resultado2.insert(0, self.calculadora.conversion(self.numero, self.sistema_actual, self.sistema_a_pasar))

	def convertir_a_quintal(self):
		"""Convert to five system"""
		self.numero = self.pantalla2.get()
		self.sistema_a_pasar = 5
		self.resultado1.delete(0, "end")
		self.resultado1.insert(0, "N(5)")
		self.resultado2.delete(0, "end")
		self.resultado2.insert(0, self.calculadora.conversion(self.numero, self.sistema_actual, self.sistema_a_pasar))

	def convertir_a_octal(self):
		"""Convert to octal system"""
		self.numero = self.pantalla2.get()
		self.sistema_a_pasar = 8
		self.resultado1.delete(0, "end")
		self.resultado1.insert(0, "N(8)")
		self.resultado2.delete(0, "end")
		self.resultado2.insert(0, self.calculadora.conversion(self.numero, self.sistema_actual, self.sistema_a_pasar))

	def convertir_a_decimal(self):
		"""Convert to decimal system"""
		self.numero = self.pantalla2.get()
		self.sistema_a_pasar = 10
		self.resultado1.delete(0, "end")
		self.resultado1.insert(0, "N(10)")
		self.resultado2.delete(0, "end")
		self.resultado2.insert(0, self.calculadora.conversion(self.numero, self.sistema_actual, self.sistema_a_pasar))

	def convertir_a_hexadecimal(self):
		"""Convert to hexadecimal system"""
		self.numero = self.pantalla2.get()
		self.sistema_a_pasar = 16
		self.resultado1.delete(0, "end")
		self.resultado1.insert(0, "N(16)")
		self.resultado2.delete(0, "end")
		self.resultado2.insert(0, self.calculadora.conversion(self.numero, self.sistema_actual, self.sistema_a_pasar))
