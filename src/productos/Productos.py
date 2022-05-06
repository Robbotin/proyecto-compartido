from dataclasses import dataclass
from productos.Producto import Producto

@dataclass
class Productos:
    def __init__(self):
        self.productos: list[Producto] = []

    def recuperarTodos(self) -> list[Producto]:
        return self.productos

    def añadir(self, producto: Producto) -> None:
        self.productos.append(producto)

    def recuperar(self, productoId: int) -> Producto:
        for producto in self.productos:
            if producto.id == productoId:
                return producto

                