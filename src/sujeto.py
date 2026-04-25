"""Interfaz Sujeto del patrón Observer."""

from __future__ import annotations

from abc import ABC, abstractmethod

from observador import Observador
from producto import Producto


class Sujeto(ABC):
    """Contrato para objetos que pueden administrar observadores."""

    @abstractmethod
    def agregar_observador(self, producto: Producto, observador: Observador) -> None:
        """Agrega un observador interesado en un producto específico."""
        raise NotImplementedError

    @abstractmethod
    def eliminar_observador(self, producto: Producto, observador: Observador) -> None:
        """Elimina un observador de la lista de interesados de un producto."""
        raise NotImplementedError

    @abstractmethod
    def notificar_observadores(self, producto: Producto) -> None:
        """Notifica a todos los observadores suscritos a un producto."""
        raise NotImplementedError
