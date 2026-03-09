# Modelo que representa un libro (mangas o novelas de anime)

class Libro:

    def __init__(self, titulo, autor, categoria, isbn):

        # Título y autor se guardan como tupla (inmutable)
        self.titulo_autor = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn

    def obtener_titulo(self):
        return self.titulo_autor[0]

    def obtener_autor(self):
        return self.titulo_autor[1]

    def __str__(self):
        return f"{self.titulo_autor[0]} - {self.titulo_autor[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"