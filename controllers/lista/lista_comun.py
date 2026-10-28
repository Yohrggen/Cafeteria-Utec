import web
import sqlite3

render = web.template.render('views', base = 'layout')

class ListaComun:
    def GET(self):
        pedidos = self.obtenerPedido()
        return render.listas.lista_comun()

    def obtenerPedido(self):
        try:
            conn = sqlite3.connect('sql/cafeteria.db')
            cursor = conn.cursor()
            query = "SELECT * FROM pedidos WHERE tipo_producto = 'comun'"
            cursor.execute(query)
            pedidos = cursor.fetchall()
            data = {'pedidos': pedidos}
            return render.listas.lista_comun(data)
        except sqlite3.Error as error:
            print(f"Error al conectar a la base de datos: {error.args}")
        finally:
            if conn:
                conn.close()