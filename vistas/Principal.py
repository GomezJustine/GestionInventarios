# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Principal.ui'
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

class principal(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Principal")
        Form.resize(488, 352)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 90, 131, 51))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 90, 131, 51))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 240, 131, 51))
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(270, 240, 131, 51))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 231, 61))

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Principal", u"Principal", None))
        self.pushButton.setText(QCoreApplication.translate("Principal", u"Gestionar inventario", None))
        self.pushButton_2.setText(QCoreApplication.translate("Principal", u"Gestionar ventas", None))
        self.pushButton_3.setText(QCoreApplication.translate("Principal", u"Historial", None))
        self.pushButton_5.setText(QCoreApplication.translate("Principal", u"Inventario", None))
        self.label.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">BIENVENIDO</span></p></body></html>", None))

