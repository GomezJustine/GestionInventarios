from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from vistas.AgregarProducto import agregarproducto
from Modelo.conexion import ConexionBaseDatos
import sys


class Agregarproducto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.agregarproducto = agregarproducto()
        self.agregarproducto.setupUi(self)
        self.agregarproducto.pushButton.clicked.connect(self.controlador_agregar_producto)
        self.agregarproducto.pushButton_2.clicked.connect(self.abrir_ventana_gestioninventario)
        self.db = ConexionBaseDatos()
        self.db.connection()

        # Configurar validadores para los campos de entrada
        self.agregarproducto.lineEdit_3.setValidator(QtGui.QIntValidator())  # ID
        self.agregarproducto.lineEdit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("["
                                                                                         ""
                                                                                         ""
                                                                                         "a-zA-Z\\s]+")))  # Nombre
        self.agregarproducto.lineEdit_2.setValidator(QtGui.QIntValidator())  # Cantidad
        self.agregarproducto.lineEdit_4.setValidator(QtGui.QDoubleValidator(0.0, 1000000.0, 2))  # Precio

        # Establecer texto de marcador de posición para guiar la entrada del usuario
        self.agregarproducto.lineEdit_3.setPlaceholderText("Ingrese solo números enteros")
        self.agregarproducto.lineEdit.setPlaceholderText("Ingrese solo letras")
        self.agregarproducto.lineEdit_2.setPlaceholderText("Ingrese solo números enteros")
        self.agregarproducto.lineEdit_4.setPlaceholderText("Ingrese precio en formato decimal")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec()

    def controlador_agregar_producto(self):
        # Agrega un nuevo producto a la base de datos
        ID = self.agregarproducto.lineEdit_3.text()  # ID
        Nombre = self.agregarproducto.lineEdit.text()  # Nombre del producto
        Cantidad = self.agregarproducto.lineEdit_2.text()  # Cantidad
        Precio = self.agregarproducto.lineEdit_4.text()  # Precio

        # Validar los datos
        if not ID or not Nombre or not Cantidad or not Precio:
            self.messagebox("Error", "Todos los campos son obligatorios")
            return

        # Convertir valores
        try:
            ID = int(ID)
            Cantidad = int(Cantidad)
            Precio = float(Precio)
        except ValueError:
            self.messagebox("Error", "ID y Cantidad deben ser números enteros y Precio debe ser un número decimal")
            return

        # Agregar el producto a la base de datos
        if self.db.agregar_producto(ID, Nombre, Cantidad, Precio):
            self.messagebox("Éxito", "Producto agregado exitosamente")
            self.agregarproducto.lineEdit_3.clear()  # Id
            self.agregarproducto.lineEdit.clear()  #Nombre del producto
            self.agregarproducto.lineEdit_2.clear()  # Cantidad
            self.agregarproducto.lineEdit_4.clear()  # Precio
        else:
            self.messagebox("Error", "No se pudo agregar el producto a la base de datos")

    def abrir_ventana_gestioninventario(self):
        # Abre la ventana de gestión de inventario y cerramos la ventana actual
        from Controladores.controladorGestionInventario import Gestionarinventario
        self.principal_window = Gestionarinventario()
        self.principal_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Agregarproducto()
    window.show()
    sys.exit(app.exec_())
