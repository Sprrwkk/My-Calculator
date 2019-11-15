import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QPushButton, QGridLayout
from my_calc_view import my_calc_view
from PyQt5.QtCore import Qt


__version__ = 1.0
__author__ = 'Łukasz Wróbel'

class CalculatorInterface(QMainWindow):
    """Calculator main interface class"""
    def __init__(self):
        # View initialization
        self.generalLayout = my_calc_view()
        super().__init__()
        self.setWindowTitle(f"My Calc  v{__version__}")
        #self.setFixedHeight(350)
        #self.setFixedWidth(250)
        self.setFixedSize(350, 250)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()



    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'7': (0, 0),
                         '8': (0, 1),
                         '9': (0, 2),
                         '/': (0, 3),
                         'C': (0, 4),
                         '4': (1, 0),
                         '5': (1, 1),
                         '6': (1, 2),
                         '*': (1, 3),
                         '(': (1, 4),
                         '1': (2, 0),
                         '2': (2, 1),
                         '3': (2, 2),
                         '-': (2, 3),
                         ')': (2, 4),
                         '0': (3, 0),
                         '00': (3, 1),
                         '.': (3, 2),
                         '+': (3, 3),
                         '=': (3, 4),
                         }

        for buttonText, position in buttons.items():
            self.buttons[buttonText] = QPushButton(buttonText)
            self.buttons[buttonText].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[buttonText], position[0], position[1])
            self.generalLayout.addLayout(buttonsLayout)




# Client code
def main_function():
    """Main Calculator function """
    my_calculator = QApplication(sys.argv)
    calculator_view = CalculatorInterface()
    calculator_view.show()
    sys.exit(my_calculator.exec())


if __name__ == '__main__':
    main_function()