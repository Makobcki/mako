

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(727, 633)
        MainWindow.setMinimumSize(QSize(300, 500))
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #121212;\n"
"	font-famuly: Rubik;\n"
"	font-size: 16pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb = QLabel(self.centralwidget)
        self.lb.setObjectName(u"lb")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb.sizePolicy().hasHeightForWidth())
        self.lb.setSizePolicy(sizePolicy)
        self.lb.setStyleSheet(u"color: #888;")

        self.verticalLayout.addWidget(self.lb)

        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy1)
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
"border: none;")
        self.le_entry.setMaxLength(16)
        self.le_entry.setReadOnly(True)

        self.verticalLayout.addWidget(self.le_entry)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.x = QPushButton(self.centralwidget)
        self.x.setObjectName(u"x")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.x.sizePolicy().hasHeightForWidth())
        self.x.setSizePolicy(sizePolicy2)
        self.x.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.x, 6, 3, 1, 1)

        self.plus = QPushButton(self.centralwidget)
        self.plus.setObjectName(u"plus")
        sizePolicy2.setHeightForWidth(self.plus.sizePolicy().hasHeightForWidth())
        self.plus.setSizePolicy(sizePolicy2)
        self.plus.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.plus, 8, 3, 1, 1)

        self.point = QPushButton(self.centralwidget)
        self.point.setObjectName(u"point")
        sizePolicy2.setHeightForWidth(self.point.sizePolicy().hasHeightForWidth())
        self.point.setSizePolicy(sizePolicy2)
        self.point.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.point, 9, 2, 1, 1)

        self.bak = QPushButton(self.centralwidget)
        self.bak.setObjectName(u"bak")
        sizePolicy2.setHeightForWidth(self.bak.sizePolicy().hasHeightForWidth())
        self.bak.setSizePolicy(sizePolicy2)
        self.bak.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.bak, 0, 2, 1, 1)

        self.n0 = QPushButton(self.centralwidget)
        self.n0.setObjectName(u"n0")
        sizePolicy2.setHeightForWidth(self.n0.sizePolicy().hasHeightForWidth())
        self.n0.setSizePolicy(sizePolicy2)
        self.n0.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.n0, 9, 1, 1, 1)

        self.n6 = QPushButton(self.centralwidget)
        self.n6.setObjectName(u"n6")
        sizePolicy2.setHeightForWidth(self.n6.sizePolicy().hasHeightForWidth())
        self.n6.setSizePolicy(sizePolicy2)
        self.n6.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.n6, 7, 2, 1, 1)

        self.dev = QPushButton(self.centralwidget)
        self.dev.setObjectName(u"dev")
        sizePolicy2.setHeightForWidth(self.dev.sizePolicy().hasHeightForWidth())
        self.dev.setSizePolicy(sizePolicy2)
        self.dev.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.dev, 0, 3, 1, 1)

        self.n1 = QPushButton(self.centralwidget)
        self.n1.setObjectName(u"n1")
        sizePolicy2.setHeightForWidth(self.n1.sizePolicy().hasHeightForWidth())
        self.n1.setSizePolicy(sizePolicy2)
        self.n1.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.n1, 8, 0, 1, 1)

        self.n3 = QPushButton(self.centralwidget)
        self.n3.setObjectName(u"n3")
        sizePolicy2.setHeightForWidth(self.n3.sizePolicy().hasHeightForWidth())
        self.n3.setSizePolicy(sizePolicy2)
        self.n3.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.n3, 8, 2, 1, 1)

        self.n8 = QPushButton(self.centralwidget)
        self.n8.setObjectName(u"n8")
        sizePolicy2.setHeightForWidth(self.n8.sizePolicy().hasHeightForWidth())
        self.n8.setSizePolicy(sizePolicy2)
        self.n8.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.n8, 6, 1, 1, 1)

        self.n4 = QPushButton(self.centralwidget)
        self.n4.setObjectName(u"n4")
        sizePolicy2.setHeightForWidth(self.n4.sizePolicy().hasHeightForWidth())
        self.n4.setSizePolicy(sizePolicy2)
        self.n4.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.n4, 7, 0, 1, 1)

        self.n5 = QPushButton(self.centralwidget)
        self.n5.setObjectName(u"n5")
        sizePolicy2.setHeightForWidth(self.n5.sizePolicy().hasHeightForWidth())
        self.n5.setSizePolicy(sizePolicy2)
        self.n5.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.n5, 7, 1, 1, 1)

        self.pls = QPushButton(self.centralwidget)
        self.pls.setObjectName(u"pls")
        sizePolicy2.setHeightForWidth(self.pls.sizePolicy().hasHeightForWidth())
        self.pls.setSizePolicy(sizePolicy2)
        self.pls.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.pls, 9, 0, 1, 1)

        self.n2 = QPushButton(self.centralwidget)
        self.n2.setObjectName(u"n2")
        sizePolicy2.setHeightForWidth(self.n2.sizePolicy().hasHeightForWidth())
        self.n2.setSizePolicy(sizePolicy2)
        self.n2.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.n2, 8, 1, 1, 1)

        self.c = QPushButton(self.centralwidget)
        self.c.setObjectName(u"c")
        sizePolicy2.setHeightForWidth(self.c.sizePolicy().hasHeightForWidth())
        self.c.setSizePolicy(sizePolicy2)
        self.c.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.c, 0, 0, 1, 1)

        self.ce = QPushButton(self.centralwidget)
        self.ce.setObjectName(u"ce")
        sizePolicy2.setHeightForWidth(self.ce.sizePolicy().hasHeightForWidth())
        self.ce.setSizePolicy(sizePolicy2)
        self.ce.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.ce, 0, 1, 1, 1)

        self.res = QPushButton(self.centralwidget)
        self.res.setObjectName(u"res")
        sizePolicy2.setHeightForWidth(self.res.sizePolicy().hasHeightForWidth())
        self.res.setSizePolicy(sizePolicy2)
        self.res.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.res, 9, 3, 1, 1)

        self.n7 = QPushButton(self.centralwidget)
        self.n7.setObjectName(u"n7")
        sizePolicy2.setHeightForWidth(self.n7.sizePolicy().hasHeightForWidth())
        self.n7.setSizePolicy(sizePolicy2)
        self.n7.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.n7, 6, 0, 1, 1)

        self.min = QPushButton(self.centralwidget)
        self.min.setObjectName(u"min")
        sizePolicy2.setHeightForWidth(self.min.sizePolicy().hasHeightForWidth())
        self.min.setSizePolicy(sizePolicy2)
        self.min.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.min, 7, 3, 1, 1)

        self.n9 = QPushButton(self.centralwidget)
        self.n9.setObjectName(u"n9")
        sizePolicy2.setHeightForWidth(self.n9.sizePolicy().hasHeightForWidth())
        self.n9.setSizePolicy(sizePolicy2)
        self.n9.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.n9, 6, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb.setText(QCoreApplication.translate("MainWindow", u"45312.31.0", None))
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.x.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(shortcut)
        self.x.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.point.setText(QCoreApplication.translate("MainWindow", u".", None))
#if QT_CONFIG(shortcut)
        self.point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
        self.bak.setText(QCoreApplication.translate("MainWindow", u"<-", None))
#if QT_CONFIG(shortcut)
        self.bak.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.n0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.n0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.n6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.n6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.dev.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.dev.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.n1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.n1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.n3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.n3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.n8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.n8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.n4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.n4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.n5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.n5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.pls.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
#if QT_CONFIG(shortcut)
        self.pls.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.n2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.n2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.c.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.ce.setText(QCoreApplication.translate("MainWindow", u"ce", None))
        self.res.setText(QCoreApplication.translate("MainWindow", u"=", None))
#if QT_CONFIG(shortcut)
        self.res.setShortcut(QCoreApplication.translate("MainWindow", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.n7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.n7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.min.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.n9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.n9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

