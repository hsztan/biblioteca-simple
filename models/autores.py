from config.connection import Connection


class Autores:
    def __init__(self, nombres):
        self.nombres = nombres

    @classmethod
    def all_autores(cls):
        try:
            conn = Connection("autores")
            records = conn.select([])

            for record in records:
                print(f"ID: {record[0]}")
                print(f"Nombres: {record[1]}")
                print("=====================")
            return records
        except Exception as e:
            print(e)

    def insert_autor(self):
        try:
            conn = Connection("autores")
            conn.insert({"nombres": self.nombres})
            print(f"Se registro el aescolar: {self.nombres}")
        except Exception as e:
            print(e)

    def update_aescolar(self):
        try:
            conn = Connection("aescolar")
            conn.update(
                {"id": 8, "modelo": "Motorola"},
                {"precio": self.precio, "modelo": "Motorola 2021"},
            )
        except Exception as e:
            print(e)
