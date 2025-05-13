from conexion import Conexion
from tkinter import messagebox, simpledialog

class ControlInventario:
    def __init__(self, view):
        self.view = view

    def cargar_invernaderos(self):
        db = Conexion()
        conn = db.conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre, estado FROM invernaderos")
            invernaderos = cursor.fetchall()
            self.view.mostrar_invernaderos(invernaderos)
            conn.close()
        else:
            print("Error al conectar a la base de datos")

    def editar(self, nombre):
            nuevo_estado = simpledialog.askstring("Editar estado", f"Ingrese el nuevo estado para '{nombre}':")
            if nuevo_estado:
                db = Conexion()
                conn = db.conectar()
                if conn:
                    cursor = conn.cursor()
                    try:
                        query = "UPDATE invernaderos SET estado = %s WHERE nombre = %s"
                        cursor.execute(query, (nuevo_estado, nombre))
                        conn.commit()
                        messagebox.showinfo("Éxito", f"Estado actualizado a: {nuevo_estado}")
                        self.cargar_invernaderos()  # refresca la tabla
                    except Exception as e:
                        messagebox.showerror("Error", f"No se pudo actualizar:\n{e}")
                    finally:
                        conn.close()
                else:
                    messagebox.showerror("Error", "No se pudo conectar a la base de datos")
            else:
                messagebox.showwarning("Cancelado", "No se realizó ninguna modificación.")
    
            self.cargar_invernaderos() 
     
    def eliminar(self, nombre):
        db = Conexion()
        conn = db.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM invernaderos WHERE nombre = %s", (nombre,))
                conn.commit()
                self.cargar_invernaderos()  # refrescar vista
            except Exception as e:
                print("Error al eliminar:", e)
            finally:
                conn.close()
    def detalles(self, nombre):
        db = Conexion()
        conn = db.conectar()
        if conn:
            cursor = conn.cursor()
            try:
                query = """
                    SELECT nombre, superficie, cultivo, fecha_creacion, responsable, capacidad, sistema_riego, estado
                    FROM invernaderos WHERE nombre = %s
                """
                cursor.execute(query, (nombre,))
                resultado = cursor.fetchone()
                if resultado:
                    detalles = (
                        f"Nombre: {resultado[0]}\n"
                        f"Superficie: {resultado[1]} m²\n"
                        f"Cultivo: {resultado[2]}\n"
                        f"Fecha de creación: {resultado[3]}\n"
                        f"Responsable: {resultado[4]}\n"
                        f"Capacidad: {resultado[5]}\n"
                        f"Sistema de riego: {resultado[6]}\n"
                        f"Estado: {resultado[7]}"
                    )
                    messagebox.showinfo("Detalles del invernadero", detalles)
                else:
                    messagebox.showwarning("No encontrado", f"No se encontró información del invernadero: {nombre}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudieron obtener los detalles:\n{e}")
            finally:
                conn.close()
        else:
            messagebox.showerror("Conexión fallida", "No se pudo conectar a la base de datos.")

    def regresar(self):
        self.view.destroy()
        from VistaMenu import VistaMenu
        VistaMenu()
