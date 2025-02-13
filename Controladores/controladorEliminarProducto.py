from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from vistas.EliminarProducto import eliminarproducto
from Modelo.conexion import ConexionBaseDatos
import sys

class Eliminarproducto(QMainWindow):

    def __init__(self):
        super().__init__()
        self.eliminarproducto = eliminarproducto()
        self.eliminarproducto.setupUi(self)
        self.eliminarproducto.pushButton.clicked.connect(self.eliminar_producto)
        self.eliminarproducto.pushButton_2.clicked.connect(self.abrir_ventana_gestioninventario)
        self.db = ConexionBaseDatos()
        self.db.connection()

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec()

    def eliminar_producto(self):
        # Elimina un producto de la base de datos
        id_producto = self.eliminarproducto.lineEdit.text()
        if id_producto:
            try:
                #Si vuelve verdadero se ejecuta esta accion
                if self.db.eliminar_producto(id_producto):
                    self.messagebox("Eliminar Producto", f"Producto con ID {id_producto} eliminado")
                else:
                    self.messagebox("Error", f"No se pudo eliminar el producto con ID {id_producto}")
            except Exception as e:
                self.messagebox("Error", f"Ocurrió un error: {str(e)}")
        else:
            self.messagebox("Error", "Por favor, ingrese el ID del producto a eliminar")

    def abrir_ventana_gestioninventario(self):
        # Abre la ventana de gestión de inventario y cierra la ventana actual
        from Controladores.controladorGestionInventario import Gestionarinventario
        self.principal_window = Gestionarinventario()
        self.principal_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Eliminarproducto()
    window.show()
    sys.exit(app.exec_())
