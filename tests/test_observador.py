"""Pruebas unitarias del patrón Observador."""

import unittest

from cliente import Cliente
from producto import Producto
from tienda import Tienda


class TestPatronObservador(unittest.TestCase):
    def test_notifica_solo_a_clientes_suscritos(self) -> None:
        tienda = Tienda("Tienda de prueba")
        producto = Producto("Teclado Mecánico")
        otro_producto = Producto("Mouse Gamer")

        ana = Cliente("Ana", "ana@test.com")
        bruno = Cliente("Bruno", "bruno@test.com")

        tienda.agregar_observador(producto, ana)
        tienda.agregar_observador(otro_producto, bruno)

        tienda.actualizar_disponibilidad(producto, True)

        self.assertEqual(len(ana.notificaciones), 1)
        self.assertEqual(len(bruno.notificaciones), 0)

    def test_eliminar_observador_evita_notificacion(self) -> None:
        tienda = Tienda("Tienda de prueba")
        producto = Producto("Cámara")
        ana = Cliente("Ana", "ana@test.com")

        tienda.agregar_observador(producto, ana)
        tienda.eliminar_observador(producto, ana)
        tienda.actualizar_disponibilidad(producto, True)

        self.assertEqual(len(ana.notificaciones), 0)


if __name__ == "__main__":
    unittest.main()
