import utils

datos = [12, 5, 20, 8, 3, 15]

promedio = utils.calcular_promedio(datos)
mayores = utils.filtrar_mayores(datos, promedio)

print("Datos:", datos)
print("Promedio:", promedio)
print("Números mayores al promedio:", mayores)
