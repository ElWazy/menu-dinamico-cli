from datetime import datetime

from conexion import Conexion
from data import Data
from producto import Producto


class Main:
    menu_principal = """
===== INICIO APLICACION =====
=== MANEJO PRODUCTOS ===
1- Agregar Producto
2- Ver Productos
3- Buscar Producto
4- Actualizar Producto
5- Eliminar Producto
6- Salir
    """

    def __init__(self, conexion: Conexion) -> None:
        self.conexion = conexion
        self.conexion.conectar()
        print(self.menu_principal)

    def agregar(self) -> None:
        print("=== AGREGAR PRODUCTO ===")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad_disponible = int(input("Ingrese la cantidad disponible: "))
        descripcion = input("Ingrese la descripcion del producto: ")
        fecha_creacion = datetime.now()
        categoria = input("Ingrese la categoria del producto: ")

        producto = Producto(
            id=1,
            nombre=nombre,
            precio=precio,
            cantidad_disponible=cantidad_disponible,
            descripcion=descripcion,
            fecha_creacion=fecha_creacion,
            categoria=categoria,
        )
        data = Data(self.conexion)
        data.insertar(producto)
        print("Producto agregado correctamente")

    def listar(self) -> None:
        print("=== LISTADO DE PRODUCTOS ===")
        data = Data(self.conexion)
        productos = data.ver()
        for producto in productos:
            print(producto)

    def buscar(self) -> None:
        print("=== BUSCAR PRODUCTO ===")
        id = int(input("Ingrese el id del producto a buscar: "))
        data = Data(self.conexion)
        producto = data.buscar(id)
        if producto:
            print(producto)
        else:
            print("Producto no encontrado")

    def actualizar(self) -> None:
        print("=== ACTUALIZAR PRODUCTO ===")
        id = int(input("Ingrese el id del producto a actualizar: "))

        buscador = Data(self.conexion)
        producto_anterior = buscador.buscar(id)
        if not producto_anterior:
            print("Producto no encontrado")
            return

        print(f"nombre: {producto_anterior.nombre}")
        nombre = input("Ingrese el nombre del producto: ")

        print(f"precio: {producto_anterior.precio}")
        precio = float(input("Ingrese el precio del producto: "))

        print(f"cantidad_disponible: {producto_anterior.cantidad_disponible}")
        cantidad_disponible = int(input("Ingrese la cantidad disponible: "))

        print(f"descripcion: {producto_anterior.descripcion}")
        descripcion = input("Ingrese la descripcion del producto: ")

        fecha_creacion = datetime.now()

        print(f"categoria: {producto_anterior.categoria}")
        categoria = input("Ingrese la categoria del producto: ")

        producto = Producto(
            id=id,
            nombre=nombre,
            precio=precio,
            cantidad_disponible=cantidad_disponible,
            descripcion=descripcion,
            fecha_creacion=fecha_creacion,
            categoria=categoria,
        )
        data = Data(self.conexion)
        data.actualizar(id, producto)
        print("Producto actualizado correctamente")

    def eliminar(self) -> None:
        print("=== ELIMINAR PRODUCTO ===")
        id = int(input("Ingrese el id del producto a eliminar: "))
        data = Data(self.conexion)
        data.eliminar(id)
        print("Producto eliminado correctamente")

    def salir(self) -> None:
        print("Saliendo de la aplicación...")
        self.conexion.desconectar()


if __name__=="__main__":
    conexion = Conexion()
    menus = Main(conexion)
    while True:
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            menus.agregar()
        if opcion == "2":
            menus.listar()
        if opcion == "3":
            menus.buscar()
        if opcion == "4":
            menus.actualizar()
        if opcion == "5":
            menus.eliminar()
        if opcion == "6":
            menus.salir()
            break
