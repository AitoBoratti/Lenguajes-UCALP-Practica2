def is_zero(value):
    s = str(value).strip()
    try:
        num = float(s)
        return num == 0
    except ValueError:
        return False

# Pruebas
value = " "
print("Es Valido" if (value and not is_zero(value)) else "No es valido")