# Implementación del Patrón Observador en una Tienda — Python

Este proyecto implementa el **patrón de diseño Observador** para resolver el caso de una tienda que desea avisar la disponibilidad de un producto **solo a los clientes interesados**, evitando revisiones manuales y notificaciones irrelevantes.

## Estructura

```text
patron-observador-tienda-python/
├── src/
│   ├── observador.py
│   ├── sujeto.py
│   ├── producto.py
│   ├── cliente.py
│   ├── tienda.py
│   └── main.py
├── tests/
│   └── test_observador.py
├── docs/
│   ├── diagrama_uml.png
│   ├── diagrama_uml.svg
│   ├── diagrama_uml.dot
│   └── diagrama_uml.mmd
├── salida_ejecucion.txt
└── README.md
```

## Clases principales

### `Observador`
Interfaz con el método `actualizar(producto)`. Cualquier cliente que desee recibir avisos debe implementar este contrato.

### `Cliente`
Implementa `Observador`. Cuando la tienda lo notifica, guarda y muestra el mensaje recibido.

### `Sujeto`
Interfaz con los métodos:

- `agregar_observador(producto, observador)`
- `eliminar_observador(producto, observador)`
- `notificar_observadores(producto)`

### `Producto`
Representa el producto que puede cambiar de estado: disponible o no disponible.

### `Tienda`
Implementa `Sujeto`. Mantiene las suscripciones por producto mediante un diccionario:

```python
_suscripciones: dict[str, set[Observador]]
```

Así, cuando un producto llega a inventario, la tienda notifica únicamente a los clientes suscritos a ese producto.

## Cómo ejecutar

Desde la carpeta raíz del proyecto:

```bash
python src/main.py
```

En algunos sistemas puede usarse:

```bash
python3 src/main.py
```

## Cómo ejecutar pruebas

```bash
PYTHONPATH=src python -m unittest discover tests
```

O, si tu sistema usa `python3`:

```bash
PYTHONPATH=src python3 -m unittest discover tests
```

## Justificación del patrón

El patrón Observador es adecuado porque desacopla a la tienda de los clientes. La tienda no necesita conocer detalles internos de cada cliente; únicamente conserva una lista de observadores por producto y llama a `actualizar()` cuando hay un cambio relevante.

La solución evita dos problemas:

1. Que el cliente revise la tienda todos los días.
2. Que la tienda envíe avisos a todos los clientes, incluso a quienes no están interesados.

Con este diseño, cada producto actúa como punto de interés y la tienda funciona como sujeto que administra la comunicación. El aviso cae solamente donde debe caer: como una campana pequeña, no como ruido en toda la ciudad.

## Salida esperada

La salida completa de una ejecución está incluida en `salida_ejecucion.txt`.
