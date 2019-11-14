import sys
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QLabel, QWidget, QApplication, QLineEdit, QGridLayout


my_app = QApplication(sys.argv)

window_object = QWidget()

window_object.setWindowTitle("My Calculator")
# window_object.setGeometry(100, 110, 280, 120)
# window_object.move(100, 100)
# bg_text = QLabel("<h1>To jest przykładowy tekst", parent=window_object)
# bg_text.move(60, 100)

layout = QGridLayout()
layout.addWidget(QPushButton('1'), 0, 0)
layout.addWidget(QPushButton('2'), 0, 1)
layout.addWidget(QPushButton('3'), 0, 2)
layout.addWidget(QPushButton('4'), 1, 0)
layout.addWidget(QPushButton('5'), 1, 1)
layout.addWidget(QPushButton('6'), 1, 2)
layout.addWidget(QPushButton('7'), 2, 0)
layout.addWidget(QPushButton('8'), 2, 1)
layout.addWidget(QPushButton('9'), 2, 2)
layout.addWidget(QPushButton('0'), 3, 1)
window_object.setLayout(layout)


window_object.show()

sys.exit(my_app.exec_())
