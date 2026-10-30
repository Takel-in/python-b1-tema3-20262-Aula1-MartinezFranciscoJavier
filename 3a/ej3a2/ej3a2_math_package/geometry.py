# geometry.py

def validar_Parametro(param):
	if not isinstance(param, (int, float)):
		raise TypeError("ERROR. tipo de dato erroneo")

def square_area(side_length: float) -> float:
    """
    Calculate the area of a square.

    Args:
    - side_length (float): the length of one side of the square.

    Returns:
    - float: the area of the square.
    """
    # Write here your code
    validar_Parametro(side_length)

    # El áre de un cuadrado se define como el lado al cuadrado.
    return side_length * side_length
    


def rectangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
    - base_length (float): the length of the base of the rectangle.
    - height (float): the height of the rectangle.

    Returns:
    - float: the area of the rectangle.
    """
    # Write here your code
    validar_Parametro(base_length)
    validar_Parametro(height)

    # El área de un rectangulo se define como la base por la altura.
    return base_length * height


def triangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
    - base_length (float): the length of the base of the triangle.
    - height (float): the height of the triangle.

    Returns:
    - float: the area of the triangle.
    """
    # Write here your code

    # El área del tríangulo se define como la base por la altura dividida entre 2
    return rectangle_area(base_length, height) / 2


def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
    - radius (float): the radius of the circle.

    Returns:
    - float: the area of the circle
    """
    # Write here your code
    validar_Parametro(radius)

    # El área de un cículo se define como 2 * Pi * Radio al cuadrado.
    return (3.1416 * radius * radius)
