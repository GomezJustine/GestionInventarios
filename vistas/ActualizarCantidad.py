from PyQt5.QtCore import QCoreApplication, QRect, QMetaObject
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QWidget

class actualizarcantidad(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Actualizar Cantidad")
        Form.resize(371, 300)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 221, 31))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 60, 256, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 110, 221, 31))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 150, 256, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 210, 75, 31))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 210, 75, 31))

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Actualizar Cantidad", u"Actualizar Cantidad", None))
        self.label.setText(QCoreApplication.translate("Actualizar Cantidad", u"ID Producto", None))
        self.label_2.setText(QCoreApplication.translate("Actualizar Cantidad", u"Nueva cantidad", None))
        self.pushButton.setText(QCoreApplication.translate("Actualizar Cantidad", u"Actualizar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Actualizar Cantidad", u"Volver", None))
