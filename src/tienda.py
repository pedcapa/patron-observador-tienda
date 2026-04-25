"""Implementación concreta del Sujeto: Tienda."""

from __future__ import annotations

from collections import defaultdict

from observador import Observador
from producto import Producto
from sujeto import Sujeto


class Tienda(Sujeto):
    """Administra productos y clientes interesados.

    La tienda evita revisar manualmente todos los días y evita enviar spam:
    solo notifica a quienes se suscribieron al producto específico.
    """

    def __init__(self, nombre: str) -> None:
        if not nombre.strip():
            raise ValueError("La tienda debe tener un nombre válido.")
        self.nombre = nombre.strip()
        self._suscripciones: dict[str, set[Observador]] = defaultdict(set)
        self._productos: dict[str, Producto] = {}

    def registrar_producto(self, producto: Producto) -> None:
        """Guarda un producto en el catálogo de la tienda."""
        self._productos[producto.clave] = producto

    def agregar_observador(self, producto: Producto, observador: Observador) -> None:
        """Suscribe un cliente a un producto específico."""
        self.registrar_producto(producto)
        self._suscripciones[producto.clave].add(observador)
        print(f"✅ {observador} se suscribió a '{producto.nombre}'.")

    def eliminar_observador(self, producto: Producto, observador: Observador) -> None:
        """Cancela la suscripción de un cliente a un producto específico."""
        suscriptores = self._suscripciones.get(producto.clave, set())
        suscriptores.discard(observador)
        print(f"🗑️  {observador} fue eliminado de '{producto.nombre}'.")

    def notificar_observadores(self, producto: Producto) -> None:
        """Notifica únicamente a clientes suscritos al producto recibido."""
        suscriptores = self._suscripciones.get(producto.clave, set())

        if not suscriptores:
            print(f"ℹ️  No hay clientes suscritos a '{producto.nombre}'.")
            return

        print(f"\n🔔 Aviso de {self.nombre}: '{producto.nombre}' está disponible.")
        for observador in suscriptores:
            observador.actualizar(producto)

    def actualizar_disponibilidad(self, producto: Producto, disponible: bool) -> None:
        """Cambia disponibilidad y dispara la notificación si llega inventario."""
        self.registrar_producto(producto)
        producto.disponible = disponible

        if producto.disponible:
            self.notificar_observadores(producto)
        else:
            print(f"ℹ️  '{producto.nombre}' continúa sin disponibilidad.")

    def obtener_suscriptores(self, producto: Producto) -> set[Observador]:
        """Devuelve una copia de los suscriptores de un producto."""
        return set(self._suscripciones.get(producto.clave, set()))
