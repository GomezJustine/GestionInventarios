from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from vistas.ActualizarCantidad import actualizarcantidad
from Modelo.conexion import ConexionBaseDatos
import sys
class Actualizarcantidad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.actualizarcantidad = actualizarcantidad()
        self.actualizarcantidad.setupUi(self)  # Configura la interfaz de usuario
        self.actualizarcantidad.pushButton.clicked.connect(self.actualizar_producto)
        self.actualizarcantidad.pushButton_2.clicked.connect(self.abrir_ventana_gestioninventario)
        self.db = ConexionBaseDatos()
        self.db.connection()

        # Mostramos un cuadro de mensaje con el título y mensaje especificados
    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec()

    def actualizar_producto(self):
        # Actualizamos la cantidad de un producto en la base de datos
        id_producto = self.actualizarcantidad.lineEdit.text()
        nueva_cantidad = self.actualizarcantidad.lineEdit_2.text()

        # Validacion que ambos campos estén completos y que sea un número positivo
        if id_producto and nueva_cantidad.isdigit() and int(nueva_cantidad) > 0:
            try:
                if self.db.actualizar_cantidad_producto(id_producto, int(nueva_cantidad)):
                    self.messagebox("Actualizar Producto", "Cantidad actualizada exitosamente")
                else:
                    self.messagebox("Error", "No se pudo actualizar la cantidad en la base de datos")
            except Exception as e:
                self.messagebox("Error", f"Ocurrió un error: {str(e)}")
        else:
            self.messagebox("Error", "Por favor, complete todos los campos correctamente")

    def abrir_ventana_gestioninventario(self):
        # Abre la ventana de gestión de inventario y cierra la ventana actual
        from Controladores.controladorGestionInventario import Gestionarinventario
        self.principal_window = Gestionarinventario()
        self.principal_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Actualizarcantidad()
    window.show()
    sys.exit(app.exec_())