"""Demostración del patrón Observador en una tienda.

Ejecutar:
    python src/main.py
"""

from cliente import Cliente
from producto import Producto
from tienda import Tienda


def main() -> None:
    tienda = Tienda("Tienda Aurora")

    consola = Producto("Consola Nova X")
    audifonos = Producto("Audífonos Luna Pro")

    ana = Cliente("Ana", "ana@example.com")
    bruno = Cliente("Bruno", "bruno@example.com")
    carla = Cliente("Carla", "carla@example.com")

    # Ana y Bruno solo quieren saber sobre la consola.
    tienda.agregar_observador(consola, ana)
    tienda.agregar_observador(consola, bruno)

    # Carla solo quiere saber sobre los audífonos.
    tienda.agregar_observador(audifonos, carla)

    print("\n--- Llega inventario de la consola ---")
    tienda.actualizar_disponibilidad(consola, True)

    print("\n--- Llega inventario de los audífonos ---")
    tienda.actualizar_disponibilidad(audifonos, True)

    print("\n--- Bruno cancela su suscripción a la consola ---")
    tienda.eliminar_observador(consola, bruno)

    consola.marcar_no_disponible()
    print("\n--- La consola vuelve a llegar ---")
    tienda.actualizar_disponibilidad(consola, True)

    print("\n--- Resumen de notificaciones recibidas ---")
    for cliente in [ana, bruno, carla]:
        print(f"{cliente.nombre}: {len(cliente.notificaciones)} notificación(es)")


if __name__ == "__main__":
    main()
