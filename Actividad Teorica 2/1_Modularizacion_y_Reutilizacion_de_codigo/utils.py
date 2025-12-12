def calcular_promedio(numeros):
    """ Calcula el promedio de una lista de números."""
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def filtrar_mayores(numeros, minimo):
    """ Filtra los números mayores que un valor mínimo."""
    resultado = []
    for n in numeros:
        if n > minimo:
            resultado.append(n)
    return resultado