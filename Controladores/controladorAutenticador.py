from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QLabel
from vistas.autenticadorppal import autenticador
from Modelo.conexion import ConexionBaseDatos
from Controladores.controladroPrincipal import main_window
import sys

class iniciarsesion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.autenticador = autenticador()
        self.autenticador.setupUi(self)

        # Etiqueta para el error
        self.error_label = QLabel(self)
        self.error_label.setGeometry(100, 200, 300, 20)
        self.error_label.setStyleSheet("color: red")
        self.error_label.hide()

        self.autenticador.BtIngreso.clicked.connect(self.ingresar)
        self.autenticador.BtBorrar.clicked.connect(self.borrar_campos)

        self.db = ConexionBaseDatos()
        self.db.connection()

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec()

    def borrar_campos(self):
        # Borra los campos de usuario y contraseña
        self.autenticador.lineusuario.clear()
        self.autenticador.linecontrasena.clear()
        self.error_label.hide()  # Ocultar error

    def ingresar(self):
        # Ingresar a la aplicacion validando los credenciales
        usuario = self.autenticador.lineusuario.text()
        contrasena = self.autenticador.linecontrasena.text()
        print(f"Intentando ingresar con usuario: {usuario} y contraseña: {contrasena}")

        if self.db.validar_usuario(usuario, contrasena):
            print("Credenciales correctas")
            self.messagebox("Login", "Inicio de sesión exitoso")
            self.abrir_ventana_principal()
        else:
            print("Credenciales incorrectas")
            self.error_label.setText("Usuario o contraseña incorrectos")
            self.error_label.show()

    def abrir_ventana_principal(self):
        # Abre la ventana principal de la aplicación y cierra la ventana actual
        self.principal_window = main_window()
        self.principal_window.show()
        self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = iniciarsesion()
    window.show()
    sys.exit(app.exec_())
