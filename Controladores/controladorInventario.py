from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from vistas.Inventario import inventario
from Modelo.conexion import ConexionBaseDatos
import sys

class Inventario(QMainWindow):

    def __init__(self):
        super().__init__()
        self.inventario = inventario()
        self.inventario.setupUi(self)
        self.inventario.pushButton.clicked.connect(self.actualizar_tabla)
        self.inventario.pushButton_2.clicked.connect(self.abrir_ventana_principal)
        self.db = ConexionBaseDatos()
        self.db.connection()
        self.init_table()
        self.cargar_datos()

    def init_table(self):
        # Inicializa el modelo de la tabla
        self.table_model = QStandardItemModel()
        self.inventario.tableView.setModel(self.table_model)
        self.table_model.setHorizontalHeaderLabels(["ID", "Nombre", "Cantidad", "Precio"])

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec()

    def cargar_datos(self):
        # Carga los datos de inventario en la tabla
        inventario = self.db.consulta_inventario()
        self.table_model.setRowCount(0)  # Limpia los datos existentes
        for row_data in inventario:
            items = [QStandardItem(str(col_data)) for col_data in row_data]
            self.table_model.appendRow(items)

    def actualizar_tabla(self):
        # Actualiza los datos de la tabla
        self.cargar_datos()
        self.messagebox("Actualizar", "Tabla actualizada")

    def abrir_ventana_principal(self):
        # Abre la ventana principal de la aplicación y cierra la ventana actual
        from Controladores.controladroPrincipal import main_window
        self.principal_window = main_window()
        self.principal_window.show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Inventario()
    window.show()
    sys.exit(app.exec_())
