# archivo ej3a1_operations.py

def validad_numeros(num1, num2):
    if not isinstance(num1, (float, int)) or not isinstance(num2, (float, int)):
        raise TypeError("ERROR. uno de los números no es decimal.")
    

def add(num_1: float, num_2: float) -> float:
    # Write here your code
    # Comprobamos los valores facilitados
    validad_numeros(num_1, num_2)

    return num_1 + num_2


def subtract(num_1: float, num_2: float) -> float:
    # Write here your code
    # Comprobamos los valores facilitados
    validad_numeros(num_1, num_2)

    return num_1 - num_2


def multiply(num_1: float, num_2: float) -> float:
    # Write here your code
    # Comprobamos los valores facilitados
    validad_numeros(num_1, num_2)

    return num_1 * num_2


def divide(num_1: float, num_2: float) -> float:
    # Write here your code
    # Comprobamos los valores facilitados
    validad_numeros(num_1, num_2)
    if num_2 == 0:
        raise ZeroDivisionError("ERROR. No puede usa 0 como divisor.")

    return num_1 / num_2
