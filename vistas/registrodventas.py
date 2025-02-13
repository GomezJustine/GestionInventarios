# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrodventas.ui'
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

class registrarventa(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Registro de Ventas")
        Form.resize(429, 360)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 150, 111, 21))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 260, 101, 31))
        self.registrarventa = QPushButton(Form)
        self.registrarventa.setObjectName(u"registrarventa")
        self.registrarventa.setGeometry(QRect(90, 260, 101, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 70, 111, 21))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 100, 261, 31))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 190, 261, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Registro de Ventas", u"Registro de Ventas", None))
        self.label_2.setText(QCoreApplication.translate("Registro de Ventas", u"<html><head/><body><p><span style=\" font-size:12pt;\">Cantidad</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Registro de Ventas", u"Volver", None))
        self.registrarventa.setText(QCoreApplication.translate("Registro de Ventas", u"Registrar Venta", None))
        self.label.setText(QCoreApplication.translate("Registro de Ventas", u"<html><head/><body><p><span style=\" font-size:12pt;\">ID Producto</span></p></body></html>", None))
    # retranslateUi
