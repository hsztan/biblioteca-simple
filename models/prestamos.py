from config.connection import Connection


class Prestamos:
    def __init__(self, usuario_id, libro_id, fecha_pres, fecha_dev):
        self.usuario_id = usuario_id
        self.libro_id = libro_id
        self.fecha_pres = fecha_pres
        self.fecha_dev = fecha_dev

    @classmethod
    def all_prestamos(cls):
        try:
            conn = Connection("prestamos")
            query = f"""
                SELECT l.id, l.nombre, u.nombres, p.fecha_pres, p.fecha_dev FROM prestamos p
                JOIN libros l ON p.libro_id = l.id
                JOIN usuarios u ON p.usuario_id = u.id
            """
            records = conn.execute_my_query(query)

            for record in records:
                print(f"ID: {record[0]}")
                print(f"Libro: {record[1]}")
                print(f"Usuario: {record[2]}")
                print(f"Fecha de préstamo: {record[3]}")
                print(f"Fecha de devolución: {record[4]}")
                print("=====================")
            return records
        except Exception as e:
            print(e)

    def insert_prestamo(self):
        try:
            conn = Connection("prestamos")
            conn.insert(
                {
                    "usuario_id": self.usuario_id,
                    "libro_id": self.libro_id,
                    "fecha_pres": self.fecha_pres,
                    "fecha_dev": self.fecha_dev,
                }
            )
            print(f"Se registro el préstamo!")
        except Exception as e:
            print(e)

    @classmethod
    def encontrar_libros_usuario(cls, user_id):
        try:
            conn = Connection("prestamos")
            query = f"""
                SELECT l.id, l.nombre, u.nombres, p.fecha_pres, p.fecha_dev FROM prestamos p
                JOIN libros l ON p.libro_id = l.id
                JOIN usuarios u ON p.usuario_id = u.id
                WHERE p.usuario_id = {user_id}
            """
            records = conn.execute_my_query(query)

            for record in records:
                print(f"ID: {record[0]}")
                print(f"Libro: {record[1]}")
                print(f"Usuario: {record[2]}")
                print(f"Fecha de préstamo: {record[3]}")
                print(f"Fecha de devolución: {record[4]}")
                print("=====================")
            return records
        except Exception as e:
            print(e)

    @classmethod
    def borrar_prestamo(cls, id):
        try:
            conn = Connection("prestamos")
            query = f"""
                DELETE FROM prestamos
                WHERE id = {id}
            """
            records = conn.execute_my_query(query)

            return records
        except Exception as e:
            print(e)
