# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestiondeinventario.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class gestioninventario(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Gestion Inventario")
        Form.resize(400, 300)
        self.EliminarProducto = QPushButton(Form)
        self.EliminarProducto.setObjectName(u"EliminarProducto")
        self.EliminarProducto.setGeometry(QRect(50, 170, 121, 31))
        self.volverP = QPushButton(Form)
        self.volverP.setObjectName(u"volverP")
        self.volverP.setGeometry(QRect(250, 170, 121, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 211, 61))
        self.ActualizarCantidad = QPushButton(Form)
        self.ActualizarCantidad.setObjectName(u"ActualizarCantidad")
        self.ActualizarCantidad.setGeometry(QRect(250, 110, 121, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 110, 121, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Gestion Inventario", u"Gestion Inventario", None))
        self.EliminarProducto.setText(QCoreApplication.translate("Gestion Inventario", u"Eliminar Producto", None))
        self.volverP.setText(QCoreApplication.translate("Gestion Inventario", u"Volver", None))
        self.label.setText(QCoreApplication.translate("Gestion Inventario", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Gestion de inventario</span></p></body></html>", None))
        self.ActualizarCantidad.setText(QCoreApplication.translate("Gestion Inventario", u"Actualizar cantidad", None))
        self.pushButton.setText(QCoreApplication.translate("Gestion Inventario", u"Agregar Producto", None))
    # retranslateUi

# If you have additional PyQt5 setup code, you can include it here.

