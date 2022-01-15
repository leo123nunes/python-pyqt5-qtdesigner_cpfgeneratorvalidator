from PyQt5.QtWidgets import QMainWindow
from qt_designer.visual_interface import Ui_MainWindow
from cpf import CpfGeneratorValidator

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.linedit_display.setReadOnly(True)