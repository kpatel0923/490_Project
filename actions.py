import sys
import subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3

#files
from quiz import *
from login import *
from signup import *
from forgot_password import *
from chart import *
from indices import *
from user import *
import testgraph


def DATABASE(query):

    with sqlite3.connect("490_database.db") as file:
        C = file.cursor()
        C.execute(query)
        file.commit()
        result = C.fetchall()
        return result


class common_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def home_screen(self):
        # PAGE home
        self.btn_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home_page))

    def login_screen(self):
        # PAGE login
        self.btn_login_signup.clicked.connect(lambda: Login.loginPage(self))

    def signup_screen(self):
        # PAGE signup
        self.btn_signup.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.signup_page))

    def test(self):
        # Testing the chart

        self.btn_submit.clicked.connect(lambda: MatplotlibWidget.update_graph(self, '1y'))
        self.btn_1D.clicked.connect(lambda: MatplotlibWidget.update_graph(self, '1d'))
        self.btn_1W.clicked.connect(lambda: MatplotlibWidget.update_graph(self, '1wk'))
        self.btn_1M.clicked.connect(lambda: MatplotlibWidget.update_graph(self, '1mo'))
        self.btn_3M.clicked.connect(lambda: MatplotlibWidget.update_graph(self, '3mo'))
        self.btn_1Y.clicked.connect(lambda: MatplotlibWidget.update_graph(self, '1y'))
        self.btn_5Y.clicked.connect(lambda: MatplotlibWidget.update_graph(self, '5y'))

        # indices buttons

        self.btn_DOW.clicked.connect(lambda: MatplotlibWidget.update_graph_index(self, '1y', 'DJI'))
        self.btn_SP.clicked.connect(lambda: MatplotlibWidget.update_graph_index(self, '1y', '^GSPC'))
        self.btn_NAS.clicked.connect(lambda: MatplotlibWidget.update_graph_index(self, '1y', '^IXIC'))
        self.btn_RUSS.clicked.connect(lambda: MatplotlibWidget.update_graph_index(self, '1y', '^RUT'))


    def refresh(self):
        # Refreshes the indices quotes
        self.btn_refresh.clicked.connect(lambda: RealTimeLabel.update_indices(self))



class login_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def login(self):
        # PAGE home
        self.btn_login.clicked.connect(lambda: Login.handleLogin(self))

    def reset_pass(self):
        # PAGE home
        self.btn_password.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.password_page))
        self.btn_send.clicked.connect(lambda: Password.handleSend(self))
        self.btn_continue.clicked.connect(lambda: Password.code(self))


        self.btn_back.clicked.connect(lambda: Password.screen(self))
        self.btn_back_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.password_page))
        self.btn_reset.clicked.connect(lambda: Password.handleReset(self))


class sign_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def signup(self):
        # PAGE home
        self.btn_signup_add.clicked.connect(lambda: Signup.addNewUser(self))




class quiz_Buttons_actions(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def navigate(self):
        # PAGE home
        quiz_Buttons.quiz_next_screen(self)
        quiz_Buttons.quiz_back_screen(self)


class user_Buttons_actions(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def navigate(self):
        # PAGE navigate
        self.btn_acct_settings.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.user_settings))
        self.btn_budget.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.budget))
        self.btn_back_3.clicked.connect(lambda: user_Buttons.back_screen(self))
        self.btn_back_4.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.chart_page))

        self.btn_personal.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.info_page))

        self.btn_change_password.clicked.connect(lambda: user_Buttons.pass_change(self))
        self.btn_retake.clicked.connect(lambda: user_Buttons.quiz(self))



