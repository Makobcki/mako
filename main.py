import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QFontDatabase

from design import Ui_MainWindow


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QFontDatabase.addApplicationFont("fonts/Rubik-Regular.ttf")

    def add_digit(self, btn_text: str) -> None:
        if self.ui.le_entry.text() == '0':
            self.ui.le_entry.setText(btn_text)
        else:
            self.ui.le_entry.setText(self.ui.le_entry.text() + btn_text)

        self.ui.n0.clicked.connect(lambda: self.add_digit("0"))
        self.ui.n1.clicked.connect(lambda: self.add_digit("1"))
        self.ui.n2.clicked.connect(lambda: self.add_digit("2"))
        self.ui.n3.clicked.connect(lambda: self.add_digit("3"))
        self.ui.n4.clicked.connect(lambda: self.add_digit("4"))
        self.ui.n5.clicked.connect(lambda: self.add_digit("5"))
        self.ui.n6.clicked.connect(lambda: self.add_digit("6"))
        self.ui.n7.clicked.connect(lambda: self.add_digit("7"))
        self.ui.n8.clicked.connect(lambda: self.add_digit("8"))
        self.ui.n9.clicked.connect(lambda: self.add_digit('9'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windoow = Calculator()
    windoow.show()
    sys.exit(app.exec())
