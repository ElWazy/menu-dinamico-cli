import mysql.connector
from mysql.connector import Error
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from producto import Producto


class Conexion:
    def __init__(self) -> None:
        self.conexion = None

    def conectar(self) -> PooledMySQLConnection | MySQLConnectionAbstract:
        try:
            self.conexion = mysql.connector.connect(
                user="root", password="pato1324", database="bd_productos"
            )
            if self.conexion.is_connected():
                print("Conexión exitosa")
            return self.conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def ver_conexion_actual(self) -> PooledMySQLConnection | MySQLConnectionAbstract:
        return self.conexion

    def desconectar(self) -> None:
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            self.conexion = None
            print("Conexión cerrada")


# Ejemplo de uso
if __name__ == "__main__":
    conexion = Conexion()
    cnx = conexion.conectar()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT id, nombre, precio, cantidad_disponible FROM producto"
        cursor.execute(query)

        for id, nombre, precio, cantidad_disponible in cursor:
            print(Producto(id, nombre, precio, cantidad_disponible))

        cursor.close()
        conexion.desconectar()
