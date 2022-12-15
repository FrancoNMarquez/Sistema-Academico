from tkinter import messagebox
from BaseDeDatos.conexion import conexionDB


class Alumnos():
    def __init__(self, id=0, nombre="", domicilio="", dni=0, edad=0):
        self.id = id
        self.nombre = nombre
        self.domicilio = domicilio
        self.dni = dni
        self.edad = edad

    def Agregar(self):
        # Agregamos lo relativo a conexion a base datos, insert en tabla alumnos
        # y finalmente el cierre de la conexion a la base.
        conexDB = conexionDB()
        sql = "insert into Alumnos(Nombre,Domicilio,Dni,Edad) values ('%s','%s',%s,%s)"
        conexDB.cursor.execute(sql % (self.nombre, self.domicilio, self.dni, self.edad))
        conexDB.con.commit
        messagebox.showinfo('Agregar', 'Nuevo alumno ingresado!!')
        conexDB.cerrar()

    def listaAlumnos():
        conexDB = conexionDB()
        sql = 'select * from Alumnos  order by id desc'
        conexDB.cursor.execute(sql)
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos

    def Modificar(self):
        conexDB = conexionDB()
        sql = "update Alumnos set Nombre='%s',Domicilio='%s',Dni=%s,Edad=%s where id=%s"
        conexDB.cursor.execute(sql % (self.nombre, self.domicilio, self.dni, self.edad, self.id))
        conexDB.con.commit
        messagebox.showinfo('Modificar', 'Datos de alumno modificados!!')
        conexDB.cerrar()

    def Eliminar(self):
        conexDB = conexionDB()
        sql = "delete from Alumnos where id=%s"
        try:
            conexDB.cursor.execute(sql % self.id)
            conexDB.cerrar()
            messagebox.showinfo('Eliminar', 'Alumno eliminado!!')
        except:
            messagebox.showerror('Eliminar', 'No se ha seleccionado ningun alumno')

    # NUEVO METODO AGREGADO
    def BuscarAlumnos(self):
        conexDB = conexionDB()
        Texto = self.nombre.strip() + "%"
        sql = "select * from Alumnos where Nombre like '%s' order by Nombre " % Texto
        conexDB.cursor.execute(sql)
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos
