"""Interfaz Observador del patrón Observer."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from producto import Producto


class Observador(ABC):
    """Contrato que deben cumplir los clientes suscritos a un producto."""

    @abstractmethod
    def actualizar(self, producto: "Producto") -> None:
        """Recibe la notificación cuando el producto cambia de estado."""
        raise NotImplementedError
