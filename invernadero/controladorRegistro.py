from conexion import Conexion
from tkinter import messagebox
from invernadero import Invernadero

class controladorRegistro:
    def __init__(self, view):
        self.view = view

    def guardar(self):
        nombre = self.view.entry_nombre.get()
        superficie = self.view.entry_superficie.get()
        cultivo = self.view.entry_cultivo.get()
        fecha = self.view.entry_fecha.get()
        responsable = self.view.entry_responsable.get()
        capacidad = self.view.entry_capacidad.get()
        riego = self.view.entry_riego.get()

        db = Conexion()
        conn = db.conectar()

        if conn:
            cursor = conn.cursor()
            query = """
                INSERT INTO invernaderos 
                (nombre, superficie, cultivo, fecha_creacion, responsable, capacidad, sistema_riego)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            datos = (nombre, superficie, cultivo, fecha, responsable, capacidad, riego)
            try:
                cursor.execute(query, datos)
                conn.commit()
                messagebox.showinfo("Éxito", "Invernadero registrado correctamente")
                self.view.destroy()
                from VistaMenu import VistaMenu
                VistaMenu()
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"No se pudo guardar: {e}")
            finally:
                conn.close()
        else:
            messagebox.showerror("Error", "No se pudo conectar a la base de datos")

    def regresar(self):
        self.view.destroy()
        from VistaMenu import VistaMenu
        VistaMenu()
