# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autenticadorppal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

# vistas/autenticadorppal.py
from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton

class autenticador(object):
    def setupUi(self, Form):
        Form.setObjectName("Iniciar sesion")
        Form.resize(393, 349)
        self.Lbusuario = QLabel(Form)
        self.Lbusuario.setObjectName("Lbusuario")
        self.Lbusuario.setGeometry(QRect(70, 30, 161, 41))
        self.Lbcontrasena = QLabel(Form)
        self.Lbcontrasena.setObjectName("Lbcontrasena")
        self.Lbcontrasena.setGeometry(QRect(70, 120, 161, 41))
        self.linecontrasena = QLineEdit(Form)
        self.linecontrasena.setObjectName("linecontrasena")
        self.linecontrasena.setGeometry(QRect(70, 170, 251, 31))
        self.linecontrasena.setEchoMode(QLineEdit.Password)
        self.BtIngreso = QPushButton(Form)
        self.BtIngreso.setObjectName("BtIngreso")
        self.BtIngreso.setGeometry(QRect(120, 240, 75, 24))
        self.lineusuario = QLineEdit(Form)
        self.lineusuario.setObjectName("lineusuario")
        self.lineusuario.setGeometry(QRect(70, 70, 251, 31))
        self.BtBorrar = QPushButton(Form)
        self.BtBorrar.setObjectName("BtBorrar")
        self.BtBorrar.setGeometry(QRect(200, 240, 75, 24))

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Iniciar sesion", "Iniciar sesion", None))
        self.Lbusuario.setText(QCoreApplication.translate("Iniciar sesion", "USUARIO", None))
        self.Lbcontrasena.setText(QCoreApplication.translate("Iniciar sesion", "CONTRASEÑA", None))
        self.BtIngreso.setText(QCoreApplication.translate("Iniciar sesion", "INGRESAR", None))
        self.BtBorrar.setText(QCoreApplication.translate("Iniciar sesion", "BORRAR", None))


