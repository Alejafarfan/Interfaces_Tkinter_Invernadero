from tkinter import messagebox
from VistaMenu import VistaMenu
from conexion import Conexion

class controladorInicio:
    def __init__(self, view):
        self.view = view

    def validar_login(self):
        usuario = self.view.entry_usuario.get()
        clave = self.view.entry_clave.get()

        db = Conexion()
        conn = db.conectar()

        if conn:
            cursor = conn.cursor()
            query = "SELECT * FROM usuarios WHERE usuario = %s AND clave = %s"
            cursor.execute(query, (usuario, clave))
            resultado = cursor.fetchone()
            conn.close()

            if resultado:
                messagebox.showinfo("Acceso permitido", "Bienvenido al sistema")
                self.view.destroy()
                VistaMenu()
            else:
                messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")
