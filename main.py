import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sqlite3

#files
from actions import *

ui,_ = loadUiType('test_ui.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        title = "Trading with a budget"
        self.setWindowTitle(title)

        #This is called to install any packages that a new user might be missing


        #The common buttons to navigate the pages
        common_Buttons.home_screen(self)
        common_Buttons.login_screen(self)
        common_Buttons.signup_screen(self)



        file = sqlite3.connect("490_database.db")
        C = file.cursor()
        C.execute("SELECT * FROM users")

        x = C.fetchall()
        print(x)






def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
