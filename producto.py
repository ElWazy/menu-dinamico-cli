from datetime import datetime


class Producto:
    id: int
    nombre: str
    precio: float
    cantidad_disponible: int
    descripcion: str
    fecha_creacion: datetime
    categoria: str

    def __init__(
        self,
        id: int | None = None,
        nombre: str = "",
        precio: float = 0.0,
        cantidad_disponible: int = 0,
        descripcion: str = "",
        fecha_creacion: datetime = datetime.now(),
        categoria: str = "Otros",
    ) -> None:
        if not id:
            raise ValueError("No se puede crear un producto sin id")
        self.id: int = id
        self.nombre: str = nombre
        self.precio: float = precio
        self.cantidad_disponible: int = cantidad_disponible
        self.descripcion: str = descripcion
        self.fecha_creacion: datetime = fecha_creacion
        self.categoria: str = categoria

    def __str__(self) -> str:
        return f"Producto n° {self.id}: {self.nombre} | {self.precio}"
