# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EliminarProducto.ui'
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
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class eliminarproducto(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Eliminar Producto")
        Form.resize(400, 302)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 60, 131, 31))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 100, 231, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 170, 75, 31))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 170, 75, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Eliminar Producto", u"Eliminar Producto", None))
        self.label.setText(QCoreApplication.translate("Eliminar Producto", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">ID Producto</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Eliminar Producto", u"Eliminar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Eliminar Producto", u"Volver", None))
    # retranslateUi
