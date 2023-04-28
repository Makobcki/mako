import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv
from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv,
}
zero = "дулить на ноль нельзя"
zerodiv = "дулить на ноль нельзя"

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.entry_max = self.ui.le_entry.maxLength()

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
        self.ui.ce.clicked.connect(self.clear_all)
        self.ui.c.clicked.connect(self.clear_entry)
        self.ui.point.clicked.connect(lambda: self.add_point())
        self.ui.plus.clicked.connect(lambda: self.math_op(" + "))
        self.ui.min.clicked.connect(lambda: self.math_op(" - "))
        self.ui.x.clicked.connect(lambda: self.math_op(" * "))
        self.ui.dev.clicked.connect(lambda: self.math_op(" / "))
        self.ui.res.clicked.connect(self.calculate)
        self.ui.pls.clicked.connect(self.min)
        self.ui.bak.clicked.connect(self.bac)

    def add_digit(self, btn_text: str) -> None:
        if self.ui.le_entry.text() == '0':
            self.ui.le_entry.setText(btn_text)
        else:
            self.ui.le_entry.setText(self.ui.le_entry.text() + btn_text)

    def clear_all(self) -> None:
        self.ui.le_entry.setText('0')
        self.ui.lb.clear()

    def clear_entry(self) -> None:
        self.ui.le_entry.setText('0')

    def bac(self) -> None:
        entry = self.ui.le_entry.text()

        if len(entry) != 1:
            if len(entry) == 2 and "-" in entry:
                entry = "0"
            else:
                entry = entry[:-1]
        else:
            entry = "0"

        self.ui.le_entry.setText(entry)

    def add_point(self) -> None:
        if "." not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + ".")
        else:
            self.ui.le_entry.setText(self.ui.le_entry.text())

    @staticmethod
    def remove_ziro(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == ".0" else n

    def add_temp(self, math_sign: str):
        if not self.ui.lb.text() or self.get_math() == "=":
            self.ui.lb.setText(self.remove_ziro(self.ui.le_entry.text()) + f"{math_sign}")
            self.ui.le_entry.setText("0")

    def num(self) -> Union[int, float]:
        entry = self.ui.le_entry.text().strip(".")
        return float(entry) if "." in entry else int(entry)

    def lb_num(self) -> Union[int, float, None]:
        if self.ui.lb.text():
            temp = self.ui.lb.text().strip(".").split()[0]
            return float(temp) if "." in temp else int(temp)

    def get_math(self) -> Optional[str]:
        if self.ui.lb.text():
            return self.ui.lb.text().strip(".").split()[-1]

    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entry.text()
        temp = self.ui.lb.text()

        if temp:
            result = self.remove_ziro(
                str(operations[self.get_math()](self.lb_num(), self.num()))
            )
            self.ui.lb.setText(temp + self.remove_ziro(entry) + " =")
            self.ui.le_entry.setText(result)
            return result



    def math_op(self, math_sign: str):
        temp = self.ui.lb.text()

        if not temp:
            self.add_temp(math_sign)
        else:
            if self.get_math() != math_sign:
                if self.get_math() == "=":
                    self.add_temp(math_sign)
                else:
                    self.ui.lb.setText(temp[:-2] + f'{math_sign}')
            else:
                self.ui.lb.setText(self.calculate() + f" {math_sign} ")

    def min(self):
        entry = self.ui.le_entry.text()

        if "-" not in entry:
            if entry != "0":
                entry = "-" + entry
        else:
            entry = entry[1:]

        if len(entry) == self.entry_max + 1 and "-" in entry:
            self.ui.le_entry.setMaxLength(self.entry_max + 1)
        else:
            self.ui.le_entry.setMaxLength(16)

        self.ui.le_entry.setText(entry)


    def error(self, text: str) -> None:
        self.ui.le_entry.setMaxLength(len(text))
        self.ui.le_entry.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windoow = Calculator()
    windoow.show()
    sys.exit(app.exec())
