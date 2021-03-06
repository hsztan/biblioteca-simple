from config.connection import Connection


class Usuarios:
    def __init__(self, nombres, correo, dni, celular, password, admin=False):
        self.nombres = nombres
        self.correo = correo
        self.dni = dni
        self.celular = celular
        self.password = password
        self.admin = admin

    @classmethod
    def all_usuarios(cls):
        try:
            conn = Connection("usuarios")

            records = conn.select([])

            for record in records:
                print(f"ID: {record[0]}")
                print(f"Nombres: {record[1]}")
                print(f"Correo: {record[2]}")
                print(f"DNI: {record[3]}")
                print(f"Celular: {record[4]}")
                print(f"Administrador?: {record[5]}")
                print("=====================")
            return records
        except Exception as e:
            print(e)

    def insert_usuario(self):
        try:
            conn = Connection("usuarios")
            conn.insert(
                {
                    "nombres": self.nombres,
                    "correo": self.correo,
                    "dni": self.dni,
                    "celular": self.celular,
                    "password": self.password,
                    "admin": self.admin,
                }
            )
            print(f"Se registro el usuario: {self.nombres}")
        except Exception as e:
            print(e)

    @classmethod
    def find_and_validate(cls, email, password):
        login = False
        admin = False
        conn = Connection("usuarios")
        query = f"""
            SELECT id, password, admin FROM usuarios
            WHERE correo = '{email}'
        """
        records = conn.execute_my_query(query)
        id = records[0][0]
        if records:
            if records[0][1] == str(password):
                login = True
            if records[0][2] == True:
                admin = True
        return login, admin, id
