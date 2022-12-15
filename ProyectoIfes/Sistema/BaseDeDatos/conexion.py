import sqlite3


class conexionDB:
    def __init__(self):

        self.con = sqlite3.connect("C:\\Cursos\\Python\\ProyectoIfes\\Sistema\\BaseDeDatos\\base")
        self.cursor = self.con.cursor()

    def cerrar(self):
        self.con.commit()
        self.con.close()
