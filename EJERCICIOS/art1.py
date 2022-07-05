class Usuarios:
    #atributos

    #constructor
    def __init__(self, nombre):
        self.nombre=nombre.title()
        print(f'Creado usuario de nombre {self.nombre}')

usu1 = Usuarios('arture')
usu1 = Usuarios('axel')
usu1 = Usuarios('bruno')
usu1 = Usuarios('rael')
usu1 = Usuarios('ale')
