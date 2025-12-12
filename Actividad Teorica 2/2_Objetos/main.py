class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            total = self.precio * cantidad
            return f"Venta realizada. Total: ${total}"
        else:
            return "Stock insuficiente."

    def reponer(self, cantidad):
        self.stock += cantidad

    def info(self):
        return f"{self.nombre} - Precio: ${self.precio} - Stock: {self.stock}"

p1 = Producto("Teclado", 25000, 10)
print(p1.info())
print(p1.vender(3))
print(p1.info())
p1.reponer(5)
print(p1.info())
