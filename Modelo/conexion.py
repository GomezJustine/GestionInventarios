import mysql.connector
from mysql.connector import Error

class ConexionBaseDatos:
    def __init__(self, host='localhost', database='proyectofinal', user='adm', password='abcd1234*'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None
        self.cursor = None

    def connection(self):
        # Establece la conexión a la base de datos
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.conn.is_connected():
                db_info = self.conn.get_server_info()
                print("Connected to MySql Server", db_info)
                self.cursor = self.conn.cursor()
                self.cursor.execute("SELECT DATABASE();")
                record = self.cursor.fetchone()
                print("Connected to database", record)
        except Error as e:
            print("Error connecting to MySQL", e)
            self.conn = None

    def cerrar_conexion(self):
        # Cierra la conexión a la base de datos
        if self.conn is not None and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Connection closed")

    def esta_conectado(self):
        # Verifica si hay una conexión activa
        return self.conn is not None and self.conn.is_connected()

    def validar_usuario(self, Usuario, Contrasena):
        # Valida las credenciales del usuario
        if self.conn is None or not self.conn.is_connected():
            print("No hay conexión activa a la base de datos")
            return False

        try:
            cur = self.conn.cursor()
            sql = "SELECT * FROM Seguridad WHERE Usuario = %s AND Contraseña = %s"
            cur.execute(sql, (Usuario, Contrasena))
            datos = cur.fetchone()
            cur.close()
            return datos is not None
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return False

    def agregar_producto(self, ID, Nombre, Cantidad, Precio):
        # Agrega un nuevo producto a la base de datos
        if self.conn is None or not self.conn.is_connected():
            print("No hay conexión activa a la base de datos")
            return False

        try:
            cur = self.conn.cursor()
            sql = "INSERT INTO Productos (ID, Nombre, Cantidad, Precio) VALUES (%s, %s, %s, %s)"
            cur.execute(sql, (ID, Nombre, Cantidad, Precio))
            self.conn.commit()
            cur.close()
            print("Producto agregado exitosamente")
            return True
        except mysql.connector.Error as err:
            print(f"Error al agregar el producto: {err}")
            return False

    def actualizar_cantidad_producto(self, ID, Cantidad):
        # Actualiza la cantidad de un producto en la base de datos
        if self.conn is None or not self.conn.is_connected():
            print("No hay conexión activa a la base de datos")
            return False

        try:
            cur = self.conn.cursor()
            sql = "UPDATE Productos SET Cantidad = %s WHERE ID = %s"
            cur.execute(sql, (Cantidad, ID))
            self.conn.commit()
            cur.close()
            print("Cantidad actualizada exitosamente")
            return True
        except mysql.connector.Error as err:
            print(f"Error al actualizar la cantidad del producto: {err}")
            return False

    def eliminar_producto(self, ID):
        # Elimina un producto de la base de datos
        if self.conn is None or not self.conn.is_connected():
            print("No hay conexión activa a la base de datos")
            return False

        try:
            cur = self.conn.cursor()
            sql = "DELETE FROM Productos WHERE ID = %s"
            cur.execute(sql, (ID,))
            self.conn.commit()
            cur.close()
            print("Producto eliminado exitosamente")
            return True
        except mysql.connector.Error as err:
            print(f"Error al eliminar el producto: {err}")
            return False

    def consulta_inventario(self):
        # Consulta el inventario de productos
        if self.conn is None or not self.conn.is_connected():
            print("No hay conexión activa a la base de datos")
            return []

        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Productos")
            datos = cur.fetchall()
            cur.close()
            return datos
        except mysql.connector.Error as err:
            print(f"Error al consultar el inventario: {err}")
            return []

    def registrar_venta(self, IDProducto, Cantidad):
        # Registra una venta en la base de datos
        if self.conn is None or not self.conn.is_connected():
            print("No hay conexión activa a la base de datos")
            return False

        try:
            cur = self.conn.cursor()
            sql = "INSERT INTO Venta (IDProducto, Cantidad) VALUES (%s, %s)"
            cur.execute(sql, (IDProducto, Cantidad))
            self.conn.commit()
            cur.close()
            print("Venta registrada exitosamente")
            return True
        except mysql.connector.Error as err:
            print(f"Error al registrar la venta: {err}")
            return False

    def registrar_compra(self, IDProducto, Cantidad, Precio):
        # Registra una compra en la base de datos
        if self.conn is None or not self.conn.is_connected():
            print("No hay conexión activa a la base de datos")
            return False

        try:
            cur = self.conn.cursor()
            sql = "INSERT INTO Compra (IDProducto, Cantidad, Precio) VALUES (%s, %s, %s)"
            cur.execute(sql, (IDProducto, Cantidad, Precio))
            self.conn.commit()
            cur.close()
            print("Compra registrada exitosamente")
            return True
        except mysql.connector.Error as err:
            print(f"Error al registrar la compra: {err}")
            return False

    def obtener_historial_ventas(self):
        # Obtiene el historial de ventas de la base de datos
        if self.conn is None or not self.conn.is_connected():
            print("No hay conexión activa a la base de datos")
            return []

        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Venta")
            datos = cur.fetchall()
            cur.close()
            return datos
        except mysql.connector.Error as err:
            print(f"Error al obtener el historial de ventas: {err}")
            return []

    def obtener_historial_compras(self):
        # Obtiene el historial de compras de la base de datos
        if self.conn is None or not self.conn.is_connected():
            print("No hay conexión activa a la base de datos")
            return []

        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Compra")
            datos = cur.fetchall()
            cur.close()
            return datos
        except mysql.connector.Error as err:
            print(f"Error al obtener el historial de compras: {err}")
            return []









