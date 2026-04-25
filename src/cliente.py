"""Implementación concreta del Observador: Cliente."""

from __future__ import annotations

from observador import Observador
from producto import Producto


class Cliente(Observador):
    """Cliente interesado en recibir avisos de disponibilidad."""

    def __init__(self, nombre: str, correo: str) -> None:
        if not nombre.strip():
            raise ValueError("El cliente debe tener un nombre válido.")
        if "@" not in correo:
            raise ValueError("El correo del cliente no parece válido.")
        self.nombre = nombre.strip()
        self.correo = correo.strip()
        self.notificaciones: list[str] = []

    def actualizar(self, producto: Producto) -> None:
        """Recibe la notificación enviada por la tienda."""
        mensaje = (
            f"Hola {self.nombre}, el producto '{producto.nombre}' "
            "ya está disponible en la tienda."
        )
        self.notificaciones.append(mensaje)
        print(f"📩 Notificación enviada a {self.correo}: {mensaje}")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cliente):
            return False
        return self.correo.lower() == other.correo.lower()

    def __hash__(self) -> int:
        return hash(self.correo.lower())

    def __repr__(self) -> str:
        return f"Cliente(nombre='{self.nombre}', correo='{self.correo}')"
