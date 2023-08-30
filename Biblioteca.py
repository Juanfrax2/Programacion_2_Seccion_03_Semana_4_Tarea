class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.devuelto = False

class Catalogobiblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)
    
    def añadir_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def prestar_libro(self, libro, usuario):
        if libro.disponible:
            prestamo = Prestamo(libro,usuario)
            self.prestamos.append(prestamo)
            libro.disponible = False
            return prestamo
    
    def libro_devuelto(self, prestamo):
        if not prestamo.devuelto:
            prestamo.libro.disponible = True
            prestamo.devuelto = True
            
    def historial_prest_usuar(self, usuario):
        return [prestamo for prestamo in self.prestamos if prestamo.usuario == usuario]
    


biblioteca = Catalogobiblioteca()

for _ in range(2):
    titulo = str(input("Ingrese el título del libro: "))
    autor = str(input("Ingresa el autor del libro: "))
    libro = Libro (titulo,autor)
    biblioteca.agregar_libro(libro)

for _ in range(2):
    nom_usuario = str(input("Ingrese su nombre de usuario: "))
    usuario = Usuario(nom_usuario)
    biblioteca.añadir_usuario(usuario)

while True:
    print("\nLibros disponibles: ")
    for i in range (len(biblioteca.libros)):
        libro = biblioteca.libros [i]
        if libro.disponible:
            print(f"{i + 1}. Título:{libro.titulo}; Autor:{libro.autor}")

    

    libro_num = int(input("\nIngrese el número del libro que desea prestar o ingrese 0 para salir: ")) -1
    if libro_num == -1:
        break

    usuario_num = int(input("Ingrese el número del usuario al cuál le proveerá el libro: "))-1

    if 0 <= libro_num < len(biblioteca.libros) and 0 <= usuario_num < len(biblioteca.usuarios):
        prestamo = biblioteca.prestar_libro(biblioteca.libros[libro_num], biblioteca.usuarios[usuario_num])
        if prestamo:
            print (f"Se prestó '{biblioteca.libros[libro_num].titulo} a {biblioteca.usuarios[usuario_num].nombre}'")
            
            respuesta_devolución = str(input(f"¿Desea devolver el libro '{biblioteca.libros[libro_num].titulo}'? (Sí/No): ")).lower()

            if respuesta_devolución == "si" or respuesta_devolución == "sí":
                biblioteca.libro_devuelto(prestamo)
                print ("Usted ha devuelto el libro")

            else:
                print ("Usted no ha devuelto el libro") 
    else:
        print("Número de libro o de usuario no válido")


print("\nLibros en el catálogo:\n")
for libro in biblioteca.libros:
    print(f"Título: {libro.titulo}, Autor: {libro.autor}, Disponible: {libro.disponible}")

for usuario in biblioteca.usuarios:
    print(f"\nHistorial de préstamos de {usuario.nombre}:")
    for prestamo in biblioteca.historial_prest_usuar(usuario):
        print(f"Libro: {prestamo.libro.titulo}, Devuelto: {prestamo.devuelto}")

# Funcionalidades

# Agregar el título del libro y autor
# Agregar nombre de usuario
# Prestar libro
# Usuario decide si devolver o no el libro
# Muestra el catálogo de los libros y muestra el título, autor y si está disponible  
# Muestra el hisotrial de prestámo del usuario, mostrando el título del libro y si lo devolvió o no
