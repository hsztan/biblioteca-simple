from config.connection import Connection


class Libros:
    def __init__(self, nombre, autor_id, editorial_id, edicion, status=True):
        self.nombre = nombre
        self.autor_id = autor_id
        self.editorial_id = editorial_id
        self.edicion = edicion
        self.status = status

    @classmethod
    def all_libros(cls):
        try:
            conn = Connection("libros")
            query = """
                SELECT l.id, l.nombre, a.nombres, e.nombre, l.disponible FROM libros l
                JOIN autores a ON l.autor_id = a.id
                JOIN editoriales e ON l.editorial_id = e.id
            """
            records = conn.execute_my_query(query)

            for record in records:
                print(f"ID: {record[0]}")
                print(f"Nombre: {record[1]}")
                print(f"Autor: {record[2]}")
                print(f"Editorial: {record[3]}")
                print(f"Disponibilidad: {record[4]}")
                print("=====================")
            return records
        except Exception as e:
            print(e)

    def insert_libro(self):
        try:
            conn = Connection("libros")
            conn.insert(
                {
                    "nombre": self.nombre,
                    "autor_id": self.autor_id,
                    "editorial_id": self.editorial_id,
                    "edicion": self.edicion,
                    "disponible": self.status,
                }
            )
            print(f"Se registro la editorial: {self.nombre}")
        except Exception as e:
            print(e)
