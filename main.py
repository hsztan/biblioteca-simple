from datetime import date, timedelta
from config.connection import Connection
from models.autores import Autores
from models.editoriales import Editoriales
from models.libros import Libros
from models.usuarios import Usuarios
from models.prestamos import Prestamos


class Biblioteca:
    user_id = None
    loan_time = 10

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
                ##devuelve el user_id si logra autenticar
                login_valid, admin, self.user_id = Usuarios.find_and_validate(
                    usuario, contra
                )
                print(self.user_id)
                if login_valid and admin:
                    self.interfaz_admin()
                elif login_valid:
                    self.interfaz_lector()
                else:
                    print("Usuario o contraseña incorrecta, intente otra vez!")
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
                    pass
                if opcion == "2":
                    self.prestar_libro()
                if opcion == "3":
                    exit()
                else:
                    print("Ingrese una opción válida")
        except Exception as e:
            print(e)

    def prestar_libro(self):
        Libros.libros_disponibles(True)
        libro_id = input("Selecciona el ID del libro que desea prestarse > ")
        seguro = input(f"Seguro que desea prestarse el libro {libro_id}? Y/N > ")
        if seguro == "Y" or seguro == "y":
            fecha_pres = date.today()
            fecha_dev = date.today() + timedelta(days=self.loan_time)
            Prestamos(self.user_id, libro_id, fecha_pres, fecha_dev)
            Libros.disponible(libro_id, False)
            print(f"No se olvide que la fecha de entrega del libro es {fecha_dev}")

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
        password = input("Ingrese el password del usuario > ")
        dni = input("Ingrese el dni del usuario > ")
        celular = input("Ingrese el celular del usuario > ")
        while True:
            admin = input("El usuarios es administrador? Y/N > ")
            if admin == "Y" or admin == "y":
                admin = True
                Usuarios(
                    nombres, correo, dni, celular, password, admin
                ).insert_usuario()
                break
            if admin == "N" or admin == "n":
                admin = False
                Usuarios(
                    nombres, correo, dni, celular, password, admin
                ).insert_usuario()
                break
            else:
                print("Ingrese una opción válida")

    def ingresar_libro(self):
        nombre = input("Ingrese nombre del libro > ")
        Autores.all_autores()
        autor_id = input("Ingrese el id del autor > ")
        Editoriales.all_editoriales()
        editorial_id = input("Ingrese el id de la editorial > ")
        edicion = input("Ingrese la edición del libro > ")
        Libros(nombre, autor_id, editorial_id, edicion).insert_libro()


Biblioteca()

# login, admin = Usuarios.find_and_validate("hnawrocki@test.com", 12345)
