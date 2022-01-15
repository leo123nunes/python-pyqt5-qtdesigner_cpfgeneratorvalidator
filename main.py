from PyQt5.QtWidgets import QApplication
from app import App
import sys

q_app = QApplication(sys.argv)
app = App()

app.show()
q_app.exec_()