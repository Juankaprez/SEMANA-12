from servicios.biblioteca_servicio import BibliotecaServicio

def menu():

    biblioteca = BibliotecaServicio()

    while True:

        print("\n==== Biblioteca de Anime ====")
        print("1. Añadir manga")
        print("2. Registrar usuario")
        print("3. Prestar manga")
        print("4. Buscar por título")
        print("5. Buscar por autor")
        print("6. Buscar por categoría")
        print("7. Ver libros de usuario")
        print("8. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría (Shonen, Seinen, etc): ")
            isbn = input("ISBN: ")

            biblioteca.añadir_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":

            nombre = input("Nombre: ")
            id_usuario = input("ID usuario: ")

            biblioteca.registrar_usuario(nombre, id_usuario)

        elif opcion == "3":

            id_usuario = input("ID usuario: ")
            isbn = input("ISBN del manga: ")

            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "4":

            titulo = input("Título a buscar: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "5":

            autor = input("Autor a buscar: ")
            biblioteca.buscar_por_autor(autor)

        elif opcion == "6":

            categoria = input("Categoría: ")
            biblioteca.buscar_por_categoria(categoria)

        elif opcion == "7":

            id_usuario = input("ID usuario: ")
            biblioteca.libros_usuario(id_usuario)

        elif opcion == "8":

            print("Saliendo del sistema...")
            break

menu()