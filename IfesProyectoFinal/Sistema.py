import tkinter as tk
from GUI.guiAlumnos import guiAlumnos
from GUI.guiDocentes import guiDocentes
from GUI.guiAlumnosCons import guiAlumnosCons
from GUI.guiDocentesCons import guiDocentesCons


def Alumnos(root):
    ventana = tk.Toplevel(root)
    ventana.title("Gestion de Alumnos")
    ventana.transient(root)
    app = guiAlumnos(root=ventana)


def Docentes(root):
    ventana = tk.Toplevel(root)
    ventana.title("Gestion de Docentes")
    ventana.transient(root)
    app = guiDocentes(root=ventana)


def AlumnosCons(root):
    ventana = tk.Toplevel(root)
    ventana.title("Consulta de Alumnos")
    ventana.transient(root)
    app = guiAlumnosCons(root=ventana)


def DocentesCons(root):
    ventana = tk.Toplevel(root)
    ventana.title("Consulta de Docentes")
    ventana.transient(root)
    app = guiDocentesCons(root=ventana)


def Barra_Menu(root):
    Barra_Menu = tk.Menu(root)
    root.config(menu=Barra_Menu, width=300, height=300)

    menu_datos = tk.Menu(Barra_Menu, tearoff=0)

    menu_datos1 = tk.Menu(Barra_Menu, tearoff=0)
    Barra_Menu.add_cascade(label='Datos Principales', menu=menu_datos)
    menu_datos.add_command(label='Alumnos', command=lambda: Alumnos(root))
    menu_datos.add_command(label='Docentes', command=lambda: Docentes(root))

    Barra_Menu.add_cascade(label='Consultar', menu=menu_datos1)

    menu_datos1.add_command(label='Alumnos', command=lambda: AlumnosCons(root))
    menu_datos1.add_command(label='Docentes', command=lambda: DocentesCons(root))
    Barra_Menu.add_cascade(label='Salir', command=root.destroy)


def main():
    root = tk.Tk()
    root.title('Sistema de Gestion Academica')
    Barra_Menu(root)

    root.mainloop()


if __name__ == "__main__":
    main()
