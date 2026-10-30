# arithmetic.py
import math

def validar_Parametro(param):
	if not isinstance(param, (int, float)):
		raise TypeError("ERROR. tipo de dato erroneo")

def power(base: float, exponent: float) -> float:
	# Write your code here
	validar_Parametro(base)
	validar_Parametro(exponent)

	return math.pow(base, exponent)

def square_root(num_1: float) -> float:
	# Write your code here
	validar_Parametro(num_1)

	return math.sqrt(num_1)


