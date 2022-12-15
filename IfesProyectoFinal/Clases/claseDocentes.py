from tkinter import messagebox
from BaseDeDatos.conexion import conexionDB

#Franco Marquez

class Docentes:
    def __init__(self,id=0,nombre="",domicilio="",dni=0,categ="",antig=0,sueldo=0):
        self.id = id
        self.nombre = nombre
        self.domicilio = domicilio
        self.dni = dni
        self.categ = categ
        self.antig = antig
        self.sueldo = sueldo

    def Agregar(self):
        conexDB = conexionDB()
        sql = "insert into Docentes(nombre,domicilio,dni,categ,antig,sueldo) values ('%s','%s',%s,'%s',%s,%s)"
        conexDB.cursor.execute(sql % (self.nombre, self.domicilio, self.dni, self.categ,self.antig,self.sueldo))
        conexDB.con.commit
        messagebox.showinfo('Agregar', 'Nuevo Docente ingresado!!!')
        conexDB.cerrar()
    def ListarDocentes():
        conexDB = conexionDB()
        sql = 'select * from Docentes  order by id desc'
        conexDB.cursor.execute(sql)
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos

    def Modificar(self):
        conexDB = conexionDB()
        sql = "update Docentes set Nombre='%s',Domicilio='%s',Dni=%s,categ='%s',antig=%s,sueldo=%s where id=%s"
        conexDB.cursor.execute(sql % (self.nombre, self.domicilio, self.dni, self.categ,self.antig,self.sueldo, self.id))
        conexDB.con.commit
        messagebox.showinfo('Modificar', 'Datos de Docente modificados!!')
        conexDB.cerrar()

    def Eliminar(self):
        conexDB = conexionDB()
        sql = "delete from Docentes where id=%s"
        try:
            conexDB.cursor.execute(sql % self.id)
            conexDB.cerrar()
            messagebox.showinfo('Eliminar', 'Docente eliminado!!')
        except:
            messagebox.showerror('Eliminar', 'No se ha seleccionado ningun Docente')

    def BuscarDocentes(self):
        conexDB = conexionDB()
        Texto = self.nombre.strip() + "%"
        sql = "select * from Docentes where Nombre like '%s' order by Nombre " % Texto
        conexDB.cursor.execute(sql)
        datos = conexDB.cursor.fetchall()
        conexDB.cerrar()
        return datos