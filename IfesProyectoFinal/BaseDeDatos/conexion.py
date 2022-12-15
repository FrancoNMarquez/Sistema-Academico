import sqlite3


class conexionDB:
    def __init__(self):

        self.con = sqlite3.connect("C:\\Users\\franc\\Documents\\GitHub\\Sistema-Academico\\IfesProyectoFinal\\base")
        self.cursor = self.con.cursor()

    def cerrar(self):
        self.con.commit()
        self.con.close()