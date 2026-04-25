"""Modelo de producto observado por los clientes."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=False)
class Producto:
    """Representa un producto de la tienda.

    Atributos:
        nombre: Nombre visible del producto.
        disponible: Estado de disponibilidad en inventario.
    """

    nombre: str
    disponible: bool = False

    def __post_init__(self) -> None:
        if not self.nombre.strip():
            raise ValueError("El producto debe tener un nombre válido.")
        self.nombre = self.nombre.strip()

    def marcar_disponible(self) -> None:
        """Cambia el estado del producto a disponible."""
        self.disponible = True

    def marcar_no_disponible(self) -> None:
        """Cambia el estado del producto a no disponible."""
        self.disponible = False

    @property
    def clave(self) -> str:
        """Clave estable para agrupar suscripciones por producto."""
        return self.nombre.lower()
