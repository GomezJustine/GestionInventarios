from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from vistas.registrodventas import registrarventa
from Modelo.conexion import ConexionBaseDatos
import sys


class Registroventas(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.registrarventa = registrarventa()
        self.registrarventa.setupUi(self)
        self.registrarventa.registrarventa.clicked.connect(self.registrar_venta)
        self.registrarventa.pushButton_2.clicked.connect(self.abrir_ventana_principal)
        self.db = ConexionBaseDatos()
        self.db.connection()

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec()

    def registrar_venta(self):
        # Registra una venta en la base de datos
        id_producto = self.registrarventa.lineEdit.text()
        cantidad = self.registrarventa.lineEdit_2.text()

        # Valida que ambos campos estén completos y que cantidad sea un número positivo
        if id_producto and cantidad.isdigit() and int(cantidad) > 0:
            try:
                if self.db.registrar_venta(id_producto, int(cantidad)):
                    self.messagebox("Venta Registrada", "La venta se ha registrado correctamente")
                else:
                    self.messagebox("Error", "No se pudo registrar la venta en la base de datos")
            except Exception as e:
                self.messagebox("Error", f"Ocurrió un error: {str(e)}")
        else:
            self.messagebox("Error", "Por favor, complete todos los campos correctamente")

    def abrir_ventana_principal(self):
        # Abre la ventana principal de la aplicación y cierra la ventana actual
        from Controladores.controladroPrincipal import main_window
        self.principal_window = main_window()
        self.principal_window.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Registroventas()
    window.show()
    sys.exit(app.exec_())
