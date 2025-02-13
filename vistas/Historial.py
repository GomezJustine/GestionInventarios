from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QHeaderView, QPushButton, QSizePolicy,
    QTabWidget, QTableView, QWidget)

class historial(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Historial")
        Form.resize(397, 353)
        self.Historial = QTabWidget(Form)
        self.Historial.setObjectName(u"Historial")
        self.Historial.setGeometry(QRect(20, 10, 341, 261))
        self.Compras = QWidget()
        self.Compras.setObjectName(u"Compras")
        self.tableView = QTableView(self.Compras)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 11, 291, 211))
        self.Historial.addTab(self.Compras, "")
        self.Ventas = QWidget()
        self.Ventas.setObjectName(u"Ventas")
        self.tableView_2 = QTableView(self.Ventas)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(20, 10, 291, 211))
        self.Historial.addTab(self.Ventas, "")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 290, 75, 24))

        self.retranslateUi(Form)

        self.Historial.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Historial", u"Historial", None))
        self.Historial.setTabText(self.Historial.indexOf(self.Compras), QCoreApplication.translate("Historial", u"Compras", None))
        self.Historial.setTabText(self.Historial.indexOf(self.Ventas), QCoreApplication.translate("Historial", u"Ventas", None))
        self.pushButton.setText(QCoreApplication.translate("Historial", u"Volver", None))
    # retranslateUi

