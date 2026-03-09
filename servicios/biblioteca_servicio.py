from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:

    def __init__(self):

        # Diccionario de libros disponibles
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Set para controlar IDs únicos
        self.ids_usuarios = set()

    # ---------------- LIBROS ----------------

    def añadir_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.libros:
            print("El libro ya existe.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.libros[isbn] = libro

        print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # ---------------- USUARIOS ----------------

    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print("El ID ya está registrado.")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario
        self.ids_usuarios.add(id_usuario)

        print("Usuario registrado.")

    def baja_usuario(self, id_usuario):

        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # ---------------- PRÉSTAMOS ----------------

    def prestar_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        if isbn not in self.libros:
            print("Libro no disponible.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]

        usuario.prestar_libro(libro)

        del self.libros[isbn]

        print("Libro prestado correctamente.")

    def devolver_libro(self, id_usuario, libro):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        usuario.devolver_libro(libro)

        self.libros[libro.isbn] = libro

        print("Libro devuelto.")

    # ---------------- BÚSQUEDAS ----------------

    def buscar_por_titulo(self, titulo):

        for libro in self.libros.values():
            if titulo.lower() in libro.obtener_titulo().lower():
                print(libro)

    def buscar_por_autor(self, autor):

        for libro in self.libros.values():
            if autor.lower() in libro.obtener_autor().lower():
                print(libro)

    def buscar_por_categoria(self, categoria):

        for libro in self.libros.values():
            if categoria.lower() in libro.categoria.lower():
                print(libro)

    # ---------------- LISTAR ----------------

    def libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return

        usuario = self.usuarios[id_usuario]

        print("Libros prestados:")

        for libro in usuario.libros_prestados:
            print(libro)