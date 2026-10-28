CREATE table pedidos(
    no_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_cliente TEXT NOT NULL,
    producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    tipo_producto TEXT NOT NULL,
    tiempo_preparacion INT
);