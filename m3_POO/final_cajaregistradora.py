import unittest

# Clase para crear objetos productos del supermercado con nombre y descuento, 
# metodo para calcular el precio final

class Producto(object):
    def __init__(self, nombre, precio, descuento=0):
        self.nombre = nombre
        self.precio_original = precio
        self.descuento = descuento

    def calcular_precio_final(self):
        descuento_en_pesos = self.precio_original * (self.descuento / 100)
        precio_final = self.precio_original - descuento_en_pesos
        return precio_final

# Clase de la caja registradora en si, agrega a una lista 
# sumando el total parcial sin descuentos y el total con descuentos
# permite el ingreso de pago y da el vuelto

class CajaRegistradora(object):
    def __init__(self):
        self.productos = []
        self.total_parcial = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total_parcial += producto.precio_original

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.calcular_precio_final()
        return total
    
    def pago(self, monto_pagado):
        total = self.calcular_total()
        if monto_pagado >= total:
            vuelto = monto_pagado - total
            return vuelto
        else:
            return None


# Tests

class TestProducto(unittest.TestCase):
    def test_calcular_precio_final_sin_descuento(self):
        producto = Producto("Manzana", 20)
        self.assertEqual(producto.calcular_precio_final(), 20)

    def test_calcular_precio_final_con_descuento(self):
        producto = Producto("Manzana", 20, 25)
        self.assertEqual(producto.calcular_precio_final(), 15)

class TestCajaRegistradora(unittest.TestCase):
    def test_agregar_producto(self):
        producto = Producto("Manzana", 20, 25)
        caja = CajaRegistradora()
        caja.agregar_producto(producto)
        self.assertEqual(caja.total_parcial, 20)
        self.assertEqual(len(caja.productos), 1)

    def test_calcular_total(self):
        producto1 = Producto("Manzana", 20, 25)
        producto2 = Producto("Banana", 30, 15)
        caja = CajaRegistradora()
        caja.agregar_producto(producto1)
        caja.agregar_producto(producto2)
        self.assertEqual(caja.calcular_total(), 40.5)

    def test_pago_suficiente(self):
        producto1 = Producto("Manzana", 20, 25)
        producto2 = Producto("Banana", 30, 15)
        caja = CajaRegistradora()
        caja.agregar_producto(producto1)
        caja.agregar_producto(producto2)
        self.assertEqual(caja.pago(50), 9.5)

    def test_pago_insuficiente(self):
        producto1 = Producto("Manzana", 20, 25)
        producto2 = Producto("Banana", 30, 15)
        caja = CajaRegistradora()
        caja.agregar_producto(producto1)
        caja.agregar_producto(producto2)
        self.assertIsNone(caja.pago(30))

if __name__ == '__main__':
    unittest.main()

# Programa para usar la caja registradora, es para ejecutar el programa
# Esta comentado para que solo corran los test

"""
#Productos de ejemplo agregados
productos_disponibles = { "f123": Producto("Manzana", 20, 25),
                    "f456": Producto("Banana", 30, 15), 
                    "f789": Producto("Lechuga", 10.5), 
                    "a123": Producto("Harina", 5.5), 
                    "a456": Producto("Aceite", 25, 15), 
                    "a789": Producto("Galletita", 22, 50)
}

#Programa funcional

carrito = CajaRegistradora()

while True:
    codigo = input("\nIngrese el codigo de producto, para finalizar escriba TOTAL: ... ")
    if codigo == "TOTAL":
        total = carrito.calcular_total()
        print ("\n\nEl TOTAL con descuentos aplicados es:  ", total)
        break
    
    producto = productos_disponibles.get(codigo) 
    if producto:
        carrito.agregar_producto(producto)
        print("Total parcial sin descuentos: ", carrito.total_parcial) 
    else: 
        print("Código de producto no encontrado.")

while True:
    monto = int(input ("\nIngrese el monto pagado por el cliente:  "))
    vuelto = carrito.pago(monto)
    if vuelto:
        print("\nVuelto a entregar:  ", vuelto)
        break
    else:
        print("\nMonto insuficiente!\n")

"""
