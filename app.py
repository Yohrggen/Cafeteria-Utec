import web

urls = (
    '/', 'controllers.index.Index',
    '/lista comun', 'controllers.lista.lista_comun.ListaComun',
    '/registro', 'controllers.registro.registro_producto.RegistroPedido',
    '/listta_prioritaria', 'controllers.lista.lista_prioritaria.ListaPrioritaria',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()