# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMessageBox

def get_error_msg(error_text):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle('Ошибка')
    msg_box.setText(error_text)
    msg_box.exec()

def get_info_msg(info_text):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setWindowTitle('Успех')
    msg_box.setText(info_text)
    msg_box.exec()

