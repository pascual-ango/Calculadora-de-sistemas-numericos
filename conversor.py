#This variables will be used to the conversion from/of the hexadecimal system
hexadecimal = {
	10: 'A',
	11: 'B',
	12: 'C',
	13: 'D',
	14: 'E',
	15: 'F'
}

hexadecima = {
	'A': 10,
	'B': 11,
	'C': 12,
	'D': 13,
	'E': 14,
	'F': 15
}

class Conversor:
	def __init__(self):
		self.resultado = 0

	def from_10(self, num:int, sis:int):
		"""convert a number from the decimal system to another system"""
		num = int(num)
		resultado = []
		while(num >= sis):
			resto = num % sis
			num = num // sis
			resultado.append(resto)
		resultado.append(num)
		resultado = resultado[::-1]
		if sis == 16:
			resultado = [hexadecimal[digito] if digito > 9 else digito for digito in resultado]
		resultado = "".join(str(x) for x in resultado)
		return resultado

	def to_10(self, num, sis):
		"""Convert a number from another system to decimal system"""
		num = str(num)

		if sis == 16:
			num = [hexadecima[digito] if digito in hexadecima else digito for digito in num]

		num = [int(i) for i in num]
		num = num[::-1]
		resultado = [sis** i * num[i] for i in range(len(num))]
		final = sum(int(x) for x in resultado)
		return final

	def conversion(self, num, fr, to):
		"""Convert a number (num) from a system (fr) to another system (to)"""
		num = self.to_10(num, fr)
		num = self.from_10(num, to)
		return num