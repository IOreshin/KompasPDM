# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton,QLineEdit, QComboBox, QWidget, QGridLayout

from PyQt5.QtWidgets import QMenu, QAction, QTreeView


from NerpaPDMUtility import get_error_msg
from DBMngModule import ProjectDB, UsersDB
import sys


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NerpaPDM. Авторизация')
        self.setFixedSize(250,150)
        self.users_db = UsersDB()
        self.users_list = self.users_db.get_column_info('LOGIN')
        self.users_passwords = self.users_db.get_column_info('PASSWORD')
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        #LOGIN BLOCK
        self.login_label = QLabel('Логин: ', self)
        self.login_name_box = QComboBox(self)
        for user in self.users_list:
            self.login_name_box.addItem(user)
        grid.addWidget(self.login_label, 0, 0)
        grid.addWidget(self.login_name_box, 0, 1)

        #PASSWORD BLOCK
        self.pass_label = QLabel('Пароль: ', self)
        self.pass_text = QLineEdit(self)
        grid.addWidget(self.pass_label, 1,0)
        grid.addWidget(self.pass_text, 1,1)
            
        #BUTTONS BLOCK
        self.login_button = QPushButton('Войти', self)
        self.login_button.clicked.connect(self.login)
        self.create_login_button = QPushButton('Создать', self)
        self.create_login_button.clicked.connect(self.create_login)
        grid.addWidget(self.login_button, 2,0)
        grid.addWidget(self.create_login_button,2,1)

        self.setLayout(grid)

    def login(self):
        login = self.login_name_box.currentText()
        password = self.pass_text.text()
        if password == self.users_passwords[self.users_list.index(login)]:
            self.hide()
            self.pdm_window = PDMWindow()
            self.pdm_window.show()
        else:
            get_error_msg('Введенный пароль неверный')
            return

    def create_login(self):
        self.hide()
        self.create_login_window = CreateUserWindow()
        self.create_login_window.show()

class CreateUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(250,150)
        self.setWindowTitle('Создать')
        self.init_ui()
    
    def init_ui(self):
        grid = QGridLayout()
        self.intro_label = QLabel("""Введите логин и пароль,\nа затем нажмите кнопку создать""",self)
        self.intro_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.intro_label, 0, 0,1,0, Qt.AlignmentFlag.AlignCenter)

        #LOGIN BLOCK
        self.login_label = QLabel('Логин: ', self)
        self.login_text = QLineEdit(self)
        grid.addWidget(self.login_label, 1, 0)
        grid.addWidget(self.login_text, 1, 1)

        #PASSWORD BLOCK
        self.pass_label = QLabel('Пароль: ', self)
        self.pass_text = QLineEdit(self)
        grid.addWidget(self.pass_label, 2,0)
        grid.addWidget(self.pass_text, 2,1)

        self.create_button = QPushButton('Создать', self)
        self.create_button.clicked.connect(self.create_login)
        grid.addWidget(self.create_button, 3, 0,1,0)

        self.setLayout(grid)

    def create_login(self):
        db_mng = UsersDB()
        add_user = False
        while add_user is False:
            add_user = db_mng.add_user(self.login_text.text(), self.pass_text.text())
        self.login_window = LoginWindow()
        self.login_window.show()
        self.hide()

class PDMWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NerpaPDM')
        self.setFixedSize(1000,1000)
        self.init_ui()

    def init_ui(self):
        self.create_menubar()

        self.full_treeview = QTreeView()
        self.setCentralWidget(self.full_treeview)


        

    def create_menubar(self):
        menuBar = self.menuBar()
        self._create_actions()
        self._connect_actions()
        #FILE MENU
        file_menu = QMenu('Проект', self)
        menuBar.addMenu(file_menu)
        file_menu.addAction(self.newAction)
        file_menu.addAction(self.openAction)
        file_menu.addAction(self.updateAction)
        file_menu.addAction(self.saveAction)
        #EDIT MENU
        edit_menu = QMenu('Изменить', self)
        menuBar.addMenu(edit_menu)
        edit_menu.addAction(self.copyAction)
        #HELP MENU
        help_menu = QMenu('Помощь', self)
        menuBar.addMenu(help_menu)
        help_menu.addAction(self.aboutAction)

    def _create_actions(self):
        self.newAction = QAction("Создать", self)
        self.openAction = QAction("Открыть", self)
        self.updateAction = QAction('Обновить', self)
        self.saveAction = QAction('Сохранить', self)
        self.copyAction = QAction('Копировать', self)
        self.aboutAction = QAction('О программе', self)

    def _connect_actions(self):
        self.newAction.triggered.connect(self.new_project)
        self.openAction.triggered.connect(self.open_project)

    def new_project(self):
        pass

    def open_project(self):
        pass

    def update_project(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

