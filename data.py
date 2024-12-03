from conexion import Conexion
from producto import Producto


class Data:
    def __init__(self, conexion: Conexion) -> None:
        self.conexion = conexion

    def insertar(self, producto: Producto) -> None:
        cnx = self.conexion.ver_conexion_actual()
        if cnx:
            cursor = cnx.cursor()
            query = (
                "INSERT INTO producto (nombre, precio, cantidad_disponible, descripcion, fecha_creacion, categoria) "
                "VALUES (%s, %s, %s, %s, %s, %s)"
            )
            data = (
                producto.nombre,
                producto.precio,
                producto.cantidad_disponible,
                producto.descripcion,
                producto.fecha_creacion,
                producto.categoria,
            )
            cursor.execute(query, data)
            cnx.commit()
            cursor.close()

    def ver(self) -> list[Producto]:
        cnx = self.conexion.ver_conexion_actual()
        productos = []
        if cnx:
            cursor = cnx.cursor()
            query = (
                "SELECT id, nombre, precio, cantidad_disponible, descripcion, fecha_creacion, categoria "
                "FROM producto"
            )
            cursor.execute(query)
            for (
                id,
                nombre,
                precio,
                cantidad_disponible,
                descripcion,
                fecha_creacion,
                categoria,
            ) in cursor:
                productos.append(
                    Producto(
                        id,
                        nombre,
                        precio,
                        cantidad_disponible,
                        descripcion,
                        fecha_creacion,
                        categoria,
                    )
                )
            cursor.close()
        return productos

    def buscar(self, id: int) -> Producto:
        cnx = self.conexion.ver_conexion_actual()
        producto = None
        if cnx:
            cursor = cnx.cursor()
            query = (
                "SELECT id, nombre, precio, cantidad_disponible, descripcion, fecha_creacion, categoria "
                "FROM producto "
                "WHERE id = %s"
            )
            cursor.execute(query, (id,))
            result = cursor.fetchone()
            if result:
                producto = Producto(*result)
            cursor.close()
        return producto

    def actualizar(self, id: int, producto: Producto) -> None:
        cnx = self.conexion.ver_conexion_actual()
        if cnx:
            cursor = cnx.cursor()
            query = (
                "UPDATE producto "
                "SET nombre = %s, precio = %s, cantidad_disponible = %s, descripcion = %s, fecha_creacion = %s, categoria = %s "
                "WHERE id = %s"
            )
            data = (
                producto.nombre,
                producto.precio,
                producto.cantidad_disponible,
                producto.descripcion,
                producto.fecha_creacion,
                producto.categoria,
                id,
            )
            cursor.execute(query, data)
            cnx.commit()
            cursor.close()

    def eliminar(self, id: int) -> None:
        cnx = self.conexion.ver_conexion_actual()
        if cnx:
            cursor = cnx.cursor()
            query = "DELETE FROM producto WHERE id = %s"
            cursor.execute(query, (id,))
            cnx.commit()
            cursor.close()
