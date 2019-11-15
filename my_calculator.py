import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

__version__ = 1.0
__author__ = 'Łukasz Wróbel'

class CalculatorInterface(QMainWindow):
    """Calculator main interface class"""
    def __init__(self):
        # View initialization
        super().__init__()
        self.setWindowTitle(f"My Calc  v{__version__}")
        self.setFixedHeight(350)
        self.setFixedWidth(250)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)



# Client code
def main_function():
    """Main Calculator function """
    my_calculator = QApplication(sys.argv)
    calculator_view = CalculatorInterface()
    calculator_view.show()
    sys.exit(my_calculator.exec())


if __name__ == '__main__':
    main_function()