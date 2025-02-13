from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from vistas.Principal import principal
import sys
from Controladores.controladorHistorial import Historial
from Controladores.controladorGestionInventario import Gestionarinventario
from Controladores.controladorInventario import Inventario
from Controladores.controladorRegistroVentas import Registroventas
from Modelo.conexion import ConexionBaseDatos

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.principal = principal()
        self.principal.setupUi(self)
        self.principal.pushButton.clicked.connect(self.abrir_ventana_gestionarinventario)
        self.principal.pushButton_2.clicked.connect(self.abrir_ventana_registroventas)
        self.principal.pushButton_3.clicked.connect(self.abrir_ventana_historial)
        self.principal.pushButton_5.clicked.connect(self.abrir_ventana_inventario)
        self.db = ConexionBaseDatos()
        self.db.connection()

    def show_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Acción del botón")
        msg.setText(f"Has seleccionado: {message}")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def abrir_ventana_gestionarinventario(self):
        # Abre la ventana de gestión de inventario y cierra la ventana actual
        self.gestionarinventario_window = Gestionarinventario()
        self.gestionarinventario_window.show()
        self.close()

    def abrir_ventana_inventario(self):
        # Abre la ventana de inventario y cierra la ventana actual
        self.inventario_window = Inventario()
        self.inventario_window.show()
        self.close()

    def abrir_ventana_historial(self):
        # Abre la ventana de historial y cierra la ventana actual
        self.historial_window = Historial()
        self.historial_window.show()
        self.close()

    def abrir_ventana_registroventas(self):
        # Abre la ventana de registro de ventas y cierra la ventana actual
        self.registroventas_window = Registroventas()
        self.registroventas_window.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec_())