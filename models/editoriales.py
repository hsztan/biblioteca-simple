from config.connection import Connection


class Editoriales:
    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def all_editoriales(cls):
        try:
            conn = Connection("editoriales")
            records = conn.select([])

            for record in records:
                print(f"ID: {record[0]}")
                print(f"Editorial: {record[1]}")
                print("=====================")
            return records
        except Exception as e:
            print(e)

    def insert_editoriales(self):
        try:
            conn = Connection("editoriales")
            conn.insert({"nombre": self.nombre})
            print(f"Se registro la editorial: {self.nombre}")
        except Exception as e:
            print(e)
