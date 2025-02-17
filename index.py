from PyQt6.QtCore import * 
from PyQt6.QtGui import *
from PyQt6.QtWidgets import * 
import sys

from PyQt6.uic import loadUiType

ui,_ = loadUiType('untitled.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    
    def Handle_UI_Changes(self):
        pass

    def Handle_Buttons(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

