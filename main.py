from config.connection import Connection
from models.autores import Autores
from models.editoriales import Editoriales
from models.libros import Libros
from models.usuarios import Usuarios


class Biblioteca:
    def __init__(self):
        self.login()

    def login(self):
        try:
            while True:
                print(
                    """
                    BIENVENIDOS A LA BIBLIOTECA

                """
                )
                usuario = input("Ingrese su correo: ")
                contra = input("Ingrese su contraseña: ")
                self.interfaz_admin()
        except Exception as e:
            print(e)

    def interfaz_lector(self):
        try:
            while True:
                print(
                    """
                    BIENVENIDOS A LA BIBLIOTECA
                    Seleccione el número de su opción:
                    1) Devolver libro
                    2) Prestar libro
                    3) Salir del programa
                """
                )
                opcion = input(">")
                if opcion == "1":
                    self.interfaz_alumno()
                if opcion == "2":
                    self.interfaz_profesor()
                if opcion == "3":
                    exit()
                else:
                    print("Ingrese una opción válida")
        except Exception as e:
            print(e)

    def interfaz_admin(self):
        try:
            while True:
                print(
                    """
                    BIENVENIDOS A LA BIBLIOTECA
                    Seleccione el número de su opción:
                    1) Gestionar Autores
                    2) Gestionar Editoriales
                    3) Gestionar Libros
                    4) Gestionar Usuarios
                    5) Salir del Progama
                """
                )
                opcion = input(">")
                if opcion == "1":
                    self.interfaz_autor()
                if opcion == "2":
                    self.interfaz_editoriales()
                if opcion == "3":
                    self.interfaz_libros()
                if opcion == "4":
                    self.interfaz_usuarios()
                if opcion == "5":
                    exit()
                else:
                    print("Ingrese una opción válida")
        except Exception as e:
            print(e)

    def interfaz_usuarios(self):
        while True:
            print(
                """
                USUARIOS
                1) Ver Usuarios
                2) Crear Usuario
                3) Regresar
            """
            )
            opcion = input(">")
            if opcion == "1":
                Usuarios.all_usuarios()
            if opcion == "2":
                self.ingresar_usuario()
            if opcion == "3":
                return
            else:
                print("Ingrese una opción válida")

    def interfaz_autor(self):
        while True:
            print(
                """
                NOTAS
                1) Ver Autores
                2) Crear Autores
                3) Regresar
            """
            )
            opcion = input(">")
            if opcion == "1":
                Autores.all_autores()
            if opcion == "2":
                self.ingresar_autor()
            if opcion == "3":
                return
            else:
                print("Ingrese una opción válida")

    def interfaz_editoriales(self):
        while True:
            print(
                """
                EDITORIALES
                1) Ver Editoriales
                2) Crear Editorial
                3) Regresar
            """
            )
            opcion = input(">")
            if opcion == "1":
                Editoriales.all_editoriales()
            if opcion == "2":
                self.ingresar_editorial()
            if opcion == "3":
                return
            else:
                print("Ingrese una opción válida")

    def interfaz_libros(self):
        while True:
            print(
                """
                LIBROS
                1) Mostrar Libros
                2) Crear Libro
                3) Regresar
            """
            )
            opcion = input(">")
            if opcion == "1":
                Libros.all_libros()
            if opcion == "2":
                self.ingresar_libro()
            if opcion == "3":
                return
            else:
                print("Ingrese una opción válida")

    def ingresar_autor(self):
        autor = input("Ingrese los nombres del autor > ")
        Autores(autor).insert_autor()

    def ingresar_editorial(self):
        editorial = input("Ingrese el nobmre de la editorial > ")
        Editoriales(editorial).insert_editoriales()

    def ingresar_usuario(self):
        nombres = input("Ingrese los nombres del usuario > ")
        correo = input("Ingrese el correo del usuario > ")
        dni = input("Ingrese el dni del usuario > ")
        celular = input("Ingrese el celular del usuario > ")
        while True:
            admin = input("El usuarios es administrador? Y/N > ")
            if admin == "Y" or admin == "y":
                admin = True
                break
            if admin == "N" or admin == "n":
                admin = False
                break
            else:
                print("Ingrese una opción válida")

        Usuarios(nombres, correo, dni, celular, admin).insert_usuario()

    def ingresar_libro(self):
        nombre = input("Ingrese nombre del libro > ")
        Autores.all_autores()
        autor_id = input("Ingrese el id del autor > ")
        Editoriales.all_editoriales()
        editorial_id = input("Ingrese el id de la editorial > ")
        edicion = input("Ingrese la edición del libro > ")
        Libros(nombre, autor_id, editorial_id, edicion).insert_libro()


Biblioteca()
