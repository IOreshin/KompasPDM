# -*- coding: utf-8 -*-

import sqlite3
from NerpaPDMUtility import get_error_msg, get_info_msg

class ProjectDB():
    def __init__(self, db_path, project_name):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.project_name = project_name
        self.history_project_name = project_name+' history'
        
    def create_project(self):
        self.cursor.execute(
            f"""CREATE TABLE {self.project_name}
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            parent_id INTEGER,
            PN TEXT,
            DESCRIPTION TEXT,
            QTY INTEGER,
            VERSION INTEGER NOT NULL DEFAULT 1,
            TIMESTAMP TEXT,
            ACTIVE BOOLEAN NOT NULL DEFAULT 1,
            FOREIGN KEY (parent_id) REFERENCES items (id))"""
            )
        
        self.cursor.execute(
            f"""CREATE TABLE {self.history_project_name}
            (id INTEGER,
            parent_id INTEGER,
            PN TEXT,
            DESCRIPTION TEXT,
            QTY INTEGER,
            VERSION INTEGER NOT NULL,
            TIMESTAMP TEXT,
            ACTIVE BOOLEAN,
            CHANGE_TIMESTAMP TEXT,
            FOREIGN KEY (parent_id) REFERENCES items (id))""")

        self.conn.commit()
        self.conn.close()



class UsersDB():
    def __init__(self):
        self.conn = sqlite3.connect('databases\\users.db')
        self.cursor = self.conn.cursor()
        self.table_name = 'USERS'

    def create_user_db(self):
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS 
                            {self.table_name}
                            (LOGIN TEXT,
                            PASSWORD TEXT)""")
        
    def add_user(self, login, password):
        created_users = self.get_column_info('LOGIN')
        if login == '' or password == '':
            get_error_msg('Введите данные в поля логина и пароля')
            return
        if login not in created_users:
            self.cursor.execute(f"""INSERT INTO {self.table_name}
                                VALUES (?,?)"""
                                ,(login,password))
            self.conn.commit()
            self.conn.close()
            get_info_msg('Пользователь добавлен в PDM систему')
            return True
        else:
            get_error_msg('Пользователь с таким именем уже существует')
            
    
    def get_column_info(self, column_name):
        self.cursor.execute(f"""SELECT {column_name}
                            FROM {self.table_name}""")
        column_info = self.cursor.fetchall()
        info_list = [info[0] for info in column_info]

        return info_list
    
    def get_full_info(self):
        self.cursor.execute(f"""SELECT *
                            FROM {self.table_name}""")
        full_info = self.cursor.fetchall()
        print(full_info)
        return full_info


#test_db = UsersDB()
#test_db.get_full_info()


#test_db.get_users_login()