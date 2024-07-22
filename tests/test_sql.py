import sqlite3
import unittest

#db = sqlite3.connect("testPytest.db")
# sql = """
# CREATE TABLE personas (
#     nombre TEXT,
#     apellido TEXT,
#     dni INTEGER UNIQUE
# );
# """

# cursor = db.cursor()
# cursor.execute(sql)

# 1 = Cada vez que inicie un test, el setUp tiene que limpiar la tabla
        
# 2 = Cada vez que termine un test, el tearDown tiene que limpiar la tabla
        
# 3 = Cada vez que se inicie un test, el setup tiene que limpiar la tabla y el test eliminar lo que ha creado
        
# 4 = Cada vez que termine un test, tiene que limpiar lo que ha creado y tearDown tiene que limpiar la tabla
        
# 5 = Combinar todos



# class TestQSL(unittest.TestCase):
#     def setUp(self):
#         self.db = sqlite3.connect("tests/testPytest.db")
#         self.cursor = self.db.cursor()
#         # Crear la tabla 'personas' si no existe
#         # self.cursor.execute('''
#         #     CREATE TABLE IF NOT EXISTS personas (
#         #         nombre TEXT NOT NULL,
#         #         apellido TEXT NOT NULL,
#         #         dni INTEGER UNIQUE
#         #     )
#         # ''')
#         self.cursor.execute("DELETE FROM personas where dni=1234")
#         self.db.commit()

#     def test_crear_persona(self):
#         self.cursor.execute(
#             "INSERT INTO personas (nombre, apellido, dni) VALUES (?, ?, ?)",
#             ("Facundo", "Padilla", 1234)
#         )
#         self.db.commit()

#         # Verificar que la persona se haya insertado correctamente
#         self.cursor.execute("SELECT * FROM personas WHERE dni=?", (1234,))
#         persona = self.cursor.fetchone()
#         # self.assertIsNotNone(persona)
#         # self.assertEqual(persona[0], "Facundo")
#         # self.assertEqual(persona[1], "Padilla")
#         # self.assertEqual(persona[2], 1234)
#         #o
#         assert persona == ("Facundo", "Padilla", 1234)
        
#     def tearDown(self):
#         self.cursor.close()
#         self.db.close()


        
class TestSQLPytest:
    def test_crear_persona(self, fxt_db, fxt_cursor, fake_persona):
        fxt_cursor.execute(
            "INSERT INTO personas(nombre, apellido, dni) VALUES  (?, ? , ?)",
            fake_persona
        )
        fxt_db.commit()
        
        persona = fxt_cursor.execute(
            "SELECT * FROM personas WHERE personas.dni = 1234"
        ).fetchone()
        assert persona == fake_persona
        
        fxt_cursor.execute(
            "DELETE FROM personas WHERE personas.dni = 1234"
        )
        fxt_db.commit()
        persona = fxt_cursor.execute(
            "SELECT * FROM personas WHERE personas.dni = 1234"
        ).fetchone()
        assert persona is None
        
        # print(f"""
        #       {fxt_db}
        #       {fxt_cursor.connection}
        #       """)
        # assert fxt_db == fxt_cursor.connection
          