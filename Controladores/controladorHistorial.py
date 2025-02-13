from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from vistas.Historial import historial
from Modelo.conexion import ConexionBaseDatos
import sys

class Historial(QMainWindow):

    def __init__(self):
        super().__init__()
        self.historial = historial()
        self.historial.setupUi(self)
        self.historial.pushButton.clicked.connect(self.abrir_ventana_principal)
        self.db = ConexionBaseDatos()
        self.db.connection()
        self.init_tables()
        self.cargar_datos()

    def init_tables(self):
        # Inicializa los modelos de las tablas de compras y ventas
        self.table_model_compras = QStandardItemModel()
        self.historial.tableView.setModel(self.table_model_compras)
        self.table_model_compras.setHorizontalHeaderLabels(["ID", "IDProducto", "Cantidad", "Precio"])

        self.table_model_ventas = QStandardItemModel()
        self.historial.tableView_2.setModel(self.table_model_ventas)
        self.table_model_ventas.setHorizontalHeaderLabels(["ID", "IDProducto", "Cantidad"])

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec()

    def cargar_datos(self):
        # Carga los datos de compras y ventas en las tablas
        self.cargar_compras()
        self.cargar_ventas()


    def cargar_compras(self):
        # Carga el historial de compras en la tabla correspondiente
        compras = self.db.obtener_historial_compras()
        self.table_model_compras.setRowCount(0)  # Limpia los datos existentes
        for row_data in compras:
            items = [QStandardItem(str(col_data)) for col_data in row_data]
            self.table_model_compras.appendRow(items)

    def cargar_ventas(self):
        # Carga el historial de ventas en la tabla correspondiente
        ventas = self.db.obtener_historial_ventas()
        self.table_model_ventas.setRowCount(0)  # Limpia los datos existentes
        for row_data in ventas:
            items = [QStandardItem(str(col_data)) for col_data in row_data]
            self.table_model_ventas.appendRow(items)


    def abrir_ventana_principal(self):
        # Abre la ventana principal de la aplicación y cierra la ventana actual
        from Controladores.controladroPrincipal import main_window
        self.principal_window = main_window()
        self.principal_window.show()
        self.close()

    def showEvent(self, event):
        # Carga los datos al mostrar la ventana
        self.cargar_datos()
        super().showEvent(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Historial()
    window.show()
    sys.exit(app.exec_())
