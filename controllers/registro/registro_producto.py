import web
import sqlite3

render = web.template.render('views', base  = 'layout')


class RegistroPedido:

    def GET(self):
        return render.registro.registro_producto()

    def POST(self):
        try:
            conn = sqlite3.connect('sql/cafeteria.db')
            cursor = conn.cursor()
            pedido = web.input()

            nombre_cliente = pedido.nombre_cliente
            producto = pedido.producto
            cantidad = pedido.cantidad
            tipo_producto = pedido.tipo_producto

            query = "INSERT INTO pedidos (nombre_cliente, producto, cantidad, tipo_producto) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (nombre_cliente, producto, cantidad, tipo_producto))
            conn.commit()
            return render.registro.registro_producto()

        except sqlite3.Error as error:
            print(f"Error al conectar a la base de datos: {error.args}")
            return render.registro.registro_producto()

        except Exception as error:
                    print(f"Ocurrio otro error: {error.args}")
                    return render.registro.registro_producto()

        finally:
            if conn:
                conn.close()