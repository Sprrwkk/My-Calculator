import sys
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QLabel, QWidget, QApplication


my_app = QApplication(sys.argv)

window_object = QWidget()
window_object.setWindowTitle("My Calculator")
window_object.setGeometry(100, 110, 280, 120)
window_object.move(100, 100)
bg_text = QLabel("<h1>To jest przykładowy tekst", parent=window_object)
bg_text.move(60, 100)

window_object.show()

sys.exit(my_app.exec_())