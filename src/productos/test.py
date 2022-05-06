from Producto import Producto
from Productos import Productos

producto1 = Producto(1, 'Bolígrafo azul', 1.15, 4)
producto2 = Producto(2, 'Pañales', 6.75, 3)
producto3 = Producto(3, 'Galletas de chocolate', 0.95, 4)
producto4 = Producto(4, 'Pasta de dientes', 1.70, 3)

print(producto1)
print(producto2)
print(producto3.precio)
print(producto4.precio)

productos = Productos()
productos.añadir(producto1)
productos.añadir(producto2)
productos.añadir(producto3)
productos.añadir(producto4)
print(productos)
print(productos.recuperar(3))
print(productos.recuperar(4))
print(productos.recuperarTodos())
