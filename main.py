import sys
from typing import Union, Optional
from operator import add, sub, mul, truediv
from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_Calkulater
operations = {
    "+": add,
    "-": sub,
    "x": mul,
    "/": truediv,
}
zero = "делить на 0 нельзя"

d_f_s = 16
d_e_f_s = 40


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_Calkulater()
        self.ui.setupUi(self)
        self.entry_max = self.ui.le_entry.maxLength()

        self.ui.n0.clicked.connect(self.add_digit)
        self.ui.n1.clicked.connect(self.add_digit)
        self.ui.n2.clicked.connect(self.add_digit)
        self.ui.n3.clicked.connect(self.add_digit)
        self.ui.n4.clicked.connect(self.add_digit)
        self.ui.n5.clicked.connect(self.add_digit)
        self.ui.n6.clicked.connect(self.add_digit)
        self.ui.n7.clicked.connect(self.add_digit)
        self.ui.n8.clicked.connect(self.add_digit)
        self.ui.n9.clicked.connect(self.add_digit)
        self.ui.ce.clicked.connect(self.clear_all)
        self.ui.c.clicked.connect(self.clear_entry)
        self.ui.point.clicked.connect(self.add_point)
        self.ui.plus.clicked.connect(self.math_op)
        self.ui.min.clicked.connect(self.math_op)
        self.ui.x.clicked.connect(self.math_op)
        self.ui.dev.clicked.connect(self.math_op)
        self.ui.res.clicked.connect(self.calculate)
        self.ui.pls.clicked.connect(self.min)
        self.ui.bak.clicked.connect(self.bac)

    def add_digit(self):
        btn = self.sender()
        digit_button = ("n0", "n1", "n2", "n3", "n4",
                        "n5", "n6", "n7", "n8", "n9")

        if btn.objectName() in digit_button:
            if self.ui.le_entry.text() == '0':
                self.ui.le_entry.setText(btn.text())
            else:
                self.ui.le_entry.setText(self.ui.le_entry.text() + btn.text())
        self.ad_fnt_size()
        self.new_op()

    def clear_all(self) -> None:
        self.ui.le_entry.setText('0')
        self.ui.lb.clear()
        self.ad_fnt_size()

    def clear_entry(self) -> None:
        self.ui.le_entry.setText('0')
        self.ad_fnt_size()

    def get_txt_width(self) -> int:
        return self.ui.le_entry.fontMetrics().boundingRect(self.ui.le_entry.text()).width()

    def get_lb_txt_width(self) -> int:
        return self.ui.lb.fontMetrics().boundingRect(self.ui.lb.text()).width()

    def ad_fnt_size(self) -> None:
        font_size = d_e_f_s
        while self.get_txt_width() > self.ui.le_entry.width():
            font_size -= 1
            self.ui.le_entry.setStyleSheet('font-size: ' + str(font_size) + 'pt; border: none;')

    def bac(self) -> None:
        entry = self.ui.le_entry.text()

        if entry == zero:
            entry = '0'
        else:
            if len(entry) != 1:
                if len(entry) == 2 and "-" in entry:
                    entry = "0"
                else:
                    entry = entry[:-1]
            else:
                entry = "0"
        self.ui.le_entry.setText(entry)
        self.ad_fnt_size()

    def add_point(self) -> None:
        if "." not in self.ui.le_entry.text():
            self.ui.le_entry.setText(self.ui.le_entry.text() + ".")
        else:
            self.ui.le_entry.setText(self.ui.le_entry.text())
        self.ad_fnt_size()

    @staticmethod
    def remove_ziro(num: str) -> str:
        n = str(float(num))
        return n[:-2] if n[-2:] == ".0" else n

    def add_temp(self):
        btn = self.sender()
        entry = self.remove_ziro(self.ui.le_entry.text())

        if '=' in self.ui.lb.text():
            self.ui.lb.setText()
            self.ui.lb.setText(entry + f' {btn.text} ')
        else:
            if not self.ui.lb.text() or self.get_math() == "=":
                self.ui.lb.setText(entry + f" {btn.text()} ")
                self.ui.le_entry.setText('0')
            self.ad_fnt_size()

    def new_op(self):
        btn = self.sender()
        entry = self.remove_ziro(self.ui.le_entry.text())
        if '=' in self.ui.lb.text():
            self.ui.lb.setText(entry + f' {btn.text()} ')
            entry = '0'
        self.ui.le_entry.setText(entry)

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
        self.ad_fnt_size()

    def calculate(self) -> Optional[str]:
        entry = self.ui.le_entry.text()
        temp = self.ui.lb.text()

        try:
            if temp:
                result = self.remove_ziro(
                    str(operations[self.get_math()](self.lb_num(), self.num()))
                )
                self.ui.lb.setText(temp + self.remove_ziro(entry) + "=")
                self.ui.le_entry.setText(result)
                self.ad_fnt_size()
                return result
        except KeyError:
            pass

        except ZeroDivisionError:
            self.ui.le_entry.setText(zero)
        self.ad_fnt_size()
        self.new_op()

    def math_op(self) -> None:
        temp = self.ui.lb.text()
        btn = self.sender()

        if not temp:
            self.add_temp()
        else:
            if self.get_math() != btn.text():
                if self.get_math() == "=":
                    self.add_temp()
                else:
                    self.ui.lb.setText(temp[:-3] + f' {btn.text( )} ')
            else:
                self.ui.lb.setText(self.calculate() + f" {btn.text( )} ")
        self.ad_fnt_size()
        self.new_op()

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
            self.ui.le_entry.setMaxLength(20)

        self.ui.le_entry.setText(entry)
        self.ad_fnt_size()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windoow = Calculator()
    windoow.show()
    sys.exit(app.exec())
