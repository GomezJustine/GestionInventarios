from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os
from Controladores.controladorAutenticador import iniciarsesion



class MainWin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = iniciarsesion()
        self.ui.setupUi(self)
        self.show()

# Creamos aplicacion Qt e iniciamos la pantalla de inicio
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = iniciarsesion()
    window.show()
    sys.exit(app.exec_())
