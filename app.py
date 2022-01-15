from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from qt_designer.visual_interface import Ui_MainWindow
from cpf_app import CpfApp

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.cpf_app = CpfApp('')

        self.linedit_display.setReadOnly(True)

        self.btn_generate_cpf.clicked.connect(self.generate_cpf)

        self.btn_validate_cpf.clicked.connect(self.validate_cpf)

        self.btn_reset.clicked.connect(self.reset_app)

        self.linedit_display.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.linedit_cpf.setInputMask('999.999.999-99')

        self.DISPLAY_COLOR_NORMAL = '#888888'
        self.DISPLAY_COLOR_VALID_CPF = '#5bff5d'
        self.DISPLAY_COLOR_INVALID_CPF = '#ff5f5b'

        self.DISPLAY_TEXT_NORMAL = 'Enter the cpf...'
        self.DISPLAY_TEXT_VALID_CPF = 'Valid cpf.'
        self.DISPLAY_TEXT_INVALID_CPF = 'Invalid cpf.'

        self.reset_app()

    def generate_cpf(self):
        self.cpf_app.generate_cpf()
        self.linedit_cpf.setText(self.cpf_app.cpf)

    def validate_cpf(self):

        if len(self.linedit_cpf.text()) < 11:
            self.display_show('invalid', msg = 'Cpf must have 11 digits.')
            return 

        validation = CpfApp.validate_cpf(self.linedit_cpf.text())

        if validation:
            self.display_show('valid')
        else:
            self.display_show('invalid')

    def display_show(self, result, msg = None):

        if result == 'valid':
            self.linedit_display.setStyleSheet(f'background-color: {self.DISPLAY_COLOR_VALID_CPF}')
            self.linedit_display.setText(self.DISPLAY_TEXT_VALID_CPF)
        elif result == 'invalid':
            self.linedit_display.setStyleSheet(f'background-color: {self.DISPLAY_COLOR_INVALID_CPF}')

            if msg:
                self.linedit_display.setText(msg)
            else:
                self.linedit_display.setText(self.DISPLAY_TEXT_INVALID_CPF)

        else:
            self.linedit_display.setStyleSheet(f'background-color: {self.DISPLAY_COLOR_NORMAL}')
            self.linedit_display.setText(self.DISPLAY_TEXT_NORMAL)

    def reset_app(self):
        self.linedit_cpf.setText('')
        self.display_show('normal')