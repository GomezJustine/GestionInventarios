from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from vistas.gestiondeinventario import gestioninventario
from Modelo.conexion import ConexionBaseDatos
import sys

class Gestionarinventario(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gestioninve = gestioninventario()
        self.gestioninve.setupUi(self)
        self.gestioninve.pushButton.clicked.connect(self.abrir_ventana_agregarProducto)
        self.gestioninve.ActualizarCantidad.clicked.connect(self.abrir_ventana_actualizarCantidad)
        self.gestioninve.EliminarProducto.clicked.connect(self.abrir_ventana_eliminarProducto)
        self.gestioninve.volverP.clicked.connect(self.abrir_ventana_principal)
        self.db = ConexionBaseDatos()
        self.db.connection()

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec()

    def abrir_ventana_agregarProducto(self):
        # Abre la ventana de agregar producto y cerramos la ventana actual
        from Controladores.controladorAgregarProducto import Agregarproducto
        self.agregarproducto_window = Agregarproducto()
        self.agregarproducto_window.show()
        self.close()

    def abrir_ventana_actualizarCantidad(self):
        # Abre la ventana de actualizar cantidad y cerramos la ventana actual
        from Controladores.controladorActualizarCantidad import Actualizarcantidad
        self.actualizarcantidad_window = Actualizarcantidad()
        self.actualizarcantidad_window.show()
        self.close()

    def abrir_ventana_eliminarProducto(self):
        # Abre la ventana de eliminar producto y cerramos la ventana actual
        from Controladores.controladorEliminarProducto import Eliminarproducto
        self.eliminarproducto_window = Eliminarproducto()
        self.eliminarproducto_window.show()
        self.close()

    def abrir_ventana_principal(self):
        # Abre la ventana principal de la aplicación y cerramos la ventana actual
        from Controladores.controladroPrincipal import main_window
        self.principal_window = main_window()
        self.principal_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Gestionarinventario()
    window.show()
    sys.exit(app.exec_())
