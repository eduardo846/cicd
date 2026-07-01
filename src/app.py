"""
Simple Python app — punto de entrada principal.
"""


def sumar(a: int | float, b: int | float) -> int | float:
    """Retorna la suma de dos números."""
    return a + b


def saludar(nombre: str) -> str:
    """Retorna un saludo personalizado."""
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    return f"Hola, {nombre.strip()}!"


if __name__ == "__main__":
    print(saludar("Mundo"))
    print(f"2 + 3 = {sumar(2, 3)}")
