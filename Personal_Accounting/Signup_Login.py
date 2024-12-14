import base64
import sqlite3
import re, os, sys, time, pandas as pd, numpy as np
from datetime import datetime
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (QPushButton, QWidget, QMainWindow, QFileDialog, 
                             QApplication, QLabel, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QComboBox, QCompleter, QListView, 
                             QRadioButton, QButtonGroup, QTextBrowser, QCheckBox)
from PyQt6.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt6.QtCore import Qt, QStringListModel, QTimer, QTime, QDateTime, QDate
from Main_UI import MainUI
from User import user
from Validation import check_validation



# ***********  START SIGNUP_LOGIN CLASS   ************
class signup_login(MainUI):
    
    mounths = {"January": '31', "February": '29', "March": '31',
               "April": '30', "May": '31', "June": '30',
               "July": '31', "August": '31', "September": '30',
               "October": '31', "November": '30', "December": '31'}
    
    def __init__(self):
        #user.__init__(self)
        check_validation.__init__(self)
        MainUI.__init__(self)
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users_file.db')
        self.max_error = 0
        self.countdown = 15
    
    # ***********  START SIGN UP WINDOW   ************

    def sign_up_window(self):
        self.signup_window = QMainWindow(self)
        self.signup_window.setGeometry(300, 100, 500, 400)
        self.signup_window.setStyleSheet("background-color: #33CC99")
        self.background_signup = QLabel(self.window)

        self.security_question_line_edit = QLineEdit(self.signup_window)
        self.security_question_line_edit.setPlaceholderText("WHAT IS YOUR FAVORITE WORD ?")

        self.first_name_line_edit = QLineEdit(self.signup_window)
        self.first_name_line_edit.setPlaceholderText('first_name')
        self.last_name_line_edit = QLineEdit(self.signup_window)
        self.last_name_line_edit.setPlaceholderText('last_name')
        self.user_name_line_edit = QLineEdit(self.signup_window)
        self.user_name_line_edit.setPlaceholderText('user_name')
        self.password_line_edit = QLineEdit(self.signup_window)
        self.password_line_edit.setPlaceholderText('password')
        self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.repeat_password_line_edit = QLineEdit(self.signup_window)
        self.repeat_password_line_edit.setPlaceholderText('repeat_password')
        self.repeat_password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.email_line_edit = QLineEdit(self.signup_window)
        self.email_line_edit.setPlaceholderText('email_address')
        self.phone_number_line_edit = QLineEdit(self.signup_window)
        self.phone_number_line_edit.setPlaceholderText('phone_number')
        self.city_line_edit = QLineEdit(self.signup_window)
        self.city_line_edit.setPlaceholderText('city')
        self.day_line_edit = QLineEdit(self.signup_window)
        self.day_line_edit.setPlaceholderText('day')
        self.mounth_line_edit = QLineEdit(self.signup_window)
        self.mounth_line_edit.setPlaceholderText('month')
        self.year_line_edit = QLineEdit(self.signup_window)
        self.year_line_edit.setPlaceholderText('year')
        
        self.close_user_db_label = QLabel("please close the user's_file first!", self.signup_window)
        self.close_user_db_label.setVisible(False)
        self.close_user_db_label.setStyleSheet('color: red')
        self.first_name_label = QLabel("first_name is not valid!", self.signup_window)
        self.first_name_label.setVisible(False)
        self.first_name_label.setStyleSheet('color: red')
        self.last_name_label = QLabel("last_name is not valid!", self.signup_window)
        self.last_name_label.setVisible(False)
        self.last_name_label.setStyleSheet('color: red')
        self.password_label = QLabel("password is not valid!", self.signup_window)
        self.password_label.setVisible(False)
        self.password_label.setStyleSheet('color: red')
        self.repeat_password_label = QLabel("repeated_password is not valid!", self.signup_window)
        self.repeat_password_label.setVisible(False)
        self.repeat_password_label.setStyleSheet('color: red')
        self.security_question_label = QLabel("please answer the question", self.signup_window)
        self.security_question_label.setVisible(False)
        self.security_question_label.setStyleSheet('color: red')
        self.email_label = QLabel("email address is not valid!", self.signup_window)
        self.email_label.setVisible(False)
        self.email_label.setStyleSheet('color: red')
        self.phone_number_label = QLabel("phone_number is not valid!", self.signup_window)
        self.phone_number_label.setVisible(False)
        self.phone_number_label.setStyleSheet('color: red')
        self.city_label = QLabel("plese fill the gap", self.signup_window)
        self.city_label.setVisible(False)
        self.city_label.setStyleSheet('color: red')
        self.day_label = QLabel("birth_day is not valid!", self.signup_window)
        self.day_label.setVisible(False)
        self.day_label.setStyleSheet('color: red')
        self.mounth_label = QLabel("birth_month is not valid!", self.signup_window)
        self.mounth_label.setVisible(False)
        self.mounth_label.setStyleSheet('color: red')
        self.year_label = QLabel("birth_year is not valid!", self.signup_window)
        self.year_label.setVisible(False)
        self.year_label.setStyleSheet('color: red')

        self.line_style ="""
        QLineEdit {
           background-color: #2E5894;  
           color: #FFFFFF;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QLineEdit:hover {
            background-color: #0081AB;  
        }
        """

        self.day_line_edit.setStyleSheet(self.line_style)
        self.city_line_edit.setStyleSheet(self.line_style)
        self.email_line_edit.setStyleSheet(self.line_style)
        self.year_line_edit.setStyleSheet(self.line_style)
        self.first_name_line_edit.setStyleSheet(self.line_style)
        self.last_name_line_edit.setStyleSheet(self.line_style)
        self.mounth_line_edit.setStyleSheet(self.line_style)
        self.password_line_edit.setStyleSheet(self.line_style)
        self.repeat_password_line_edit.setStyleSheet(self.line_style)
        self.security_question_line_edit.setStyleSheet(self.line_style)
        self.user_name_line_edit.setStyleSheet(self.line_style)
        self.phone_number_line_edit.setStyleSheet(self.line_style)

        self.central = QWidget(self)
        self.layout = QVBoxLayout(self.central)
        self.hlayout = QHBoxLayout(self.central)
        self.hlayout1 = QHBoxLayout(self.central)
        self.hlayout2 = QHBoxLayout(self.central)
    
        self.day_combo_box = QComboBox(self.signup_window)
        self.day_combo_box.setStyleSheet("""
        QComboBox {
          background-color: #FF4681;  
          color: #76D7EA;
          border: 3px solid #0081AB;     
          border-radius: 10px;         
          padding: 4px;
                    
        }
        QComboBox QAbstractItemView {
            background-color: skyblue;
            color: red  
        }
        """)

        self.mounth_combo_box = QComboBox(self.signup_window)
        self.mounth_combo_box.setStyleSheet("""
        QComboBox {
          background-color: #FF4681;  
          color: #76D7EA;
          border: 3px solid #0081AB;     
          border-radius: 10px;         
          padding: 4px;
                    
        }
        QComboBox QAbstractItemView {
            background-color: skyblue;
            color: red  
        }
        """)

        self.year_combo_box = QComboBox(self.signup_window)
        self.year_combo_box.setStyleSheet("""
        QComboBox {
          background-color: #FF4681;  
          color: #76D7EA;
          border: 3px solid #0081AB;     
          border-radius: 10px;         
          padding: 4px;
                    
        }
        QComboBox QAbstractItemView {
            background-color: skyblue;
            color: red  
        }
        """)

        self.year_combo_box.activated[int].connect(self.set_year_line_edit)
        self.mounth_combo_box.activated[int].connect(self.set_mounth_line_edit)
        self.day_combo_box.activated[int].connect(self.set_day_line_edit)

        self.day_list = QListView(self.signup_window)
        self.mounth_list = QListView(self.signup_window)
        self.year_list = QListView(self.signup_window)

        for i in range(1, 32) :
            self.day_combo_box.addItem(f"{i}")

        for mounth in self.mounths.keys() :
            self.mounth_combo_box.addItem(mounth)

        for i in range(1920, 2006) :
            self.year_combo_box.addItem(f"{i}")
            
        self.hlayout1.addWidget(self.year_label)
        self.hlayout1.addWidget(self.mounth_label)
        self.hlayout1.addWidget(self.day_label)    

        self.hlayout.addWidget(self.year_line_edit)
        self.hlayout.addWidget(self.mounth_line_edit)
        self.hlayout.addWidget(self.day_line_edit)

        self.hlayout2.addWidget(self.year_combo_box)
        self.hlayout2.addWidget(self.mounth_combo_box)
        self.hlayout2.addWidget(self.day_combo_box)
        
        self.layout.addWidget(self.close_user_db_label)
        self.layout.addWidget(self.first_name_label)
        self.layout.addWidget(self.first_name_line_edit)
        self.layout.addWidget(self.last_name_label)
        self.layout.addWidget(self.last_name_line_edit)
        self.layout.addWidget(self.user_name_line_edit)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_line_edit)
        self.layout.addWidget(self.repeat_password_label)
        self.layout.addWidget(self.repeat_password_line_edit)
        self.layout.addWidget(self.security_question_label)
        self.layout.addWidget(self.security_question_line_edit)
        self.layout.addWidget(self.email_label)
        self.layout.addWidget(self.email_line_edit)
        self.layout.addWidget(self.phone_number_label)
        self.layout.addWidget(self.phone_number_line_edit)
        self.layout.addWidget(self.city_label)
        self.layout.addWidget(self.city_line_edit)
        
        self.city_combo_box = QComboBox(self.signup_window)
        self.city_combo_box.setStyleSheet("""
        QComboBox {
          background-color: #FF4681;  
          color: #76D7EA;
          border: 3px solid #0081AB;     
          border-radius: 10px;         
          padding: 4px;          
        }
        QComboBox QAbstractItemView {
            background-color: skyblue;
            color: red  
        }
        """)
        self.city_combo_box.addItems(self.default_cities)
    
        self.city_line_edit.textChanged.connect(self.update_combo_box)
        self.city_combo_box.activated[int].connect(self.set_city_line_edit)
        self.layout.addWidget(self.city_combo_box)
        
        self.layout.addLayout(self.hlayout1)
        self.layout.addLayout(self.hlayout)
        self.layout.addLayout(self.hlayout2)
        self.central.setLayout(self.layout)
        self.layout.setContentsMargins(200, 100, 200, 100)
        
        self.submit_btn = QPushButton("submit")
        self.submit_btn.setStyleSheet("""
       QPushButton {
          background-color: #C53151;  
          color: #76D7EA;
          border: 3px solid #0081AB;     
          border-radius: 10px;         
          padding: 4px;
                    
        }
        QPushButton:hover {
            background-color: #B768A2;  
        }
        """)
      
        self.layout.addWidget(self.submit_btn)
        self.submit_btn.clicked.connect(self.close_signup_open_login)
        
        self.signup_window.setCentralWidget(self.central)
        self.signup_window.setWindowTitle('Signup_Login')
        self.signup_window.show()

        # ***********  END SIGN UP WINDOW   ************
        
        # ***********  START LOGIN WINDOW   ************  

    def Login_window(self):
        self.login_window = QMainWindow(self)
        self.login_window.setGeometry(300, 100, 500, 400)
        self.login_window.setStyleSheet("background-color: #33CC99")
        
        self.timer_label = QLabel("remaining time : 00:15", self.login_window)
        self.timer_label.setVisible(False)
        self.timer_label.setStyleSheet('color: red')

        self.log_user_line_edit = QLineEdit(self.login_window)
        self.log_user_line_edit.setPlaceholderText("user_name")
        self.log_user_line_edit.setStyleSheet("""
        QLineEdit {
           background-color: #2E5894;  
           color: #FFFFFF;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QLineEdit:hover {
            background-color: #0081AB;  
        }
        """)
        
        self.login_label = QLabel("not found!", self.login_window)
        self.login_label.setVisible(False)
        self.login_label.setStyleSheet("color: red")
        self.log_password_label = QLabel("not found!", self.login_window)
        self.log_password_label.setVisible(False)
        self.log_password_label.setStyleSheet("color: red")
        self.show_user_label = QLabel("not found!", self.login_window)
        self.show_user_label.setVisible(False)
        self.show_user_label.setStyleSheet("color: red")
        self.show_password_label = QLabel("not found!", self.login_window)
        self.show_password_label.setVisible(False)
        self.show_password_label.setStyleSheet("color: red")

        self.log_password_line_edit = QLineEdit(self.login_window)
        self.log_password_line_edit.setPlaceholderText("password")
        self.log_password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.log_password_line_edit.setStyleSheet("""
        QLineEdit {
           background-color: #2E5894;  
           color: #FFFFFF;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QLineEdit:hover {
            background-color: #0081AB;  
        }
        """)

        self.go_to_signup_window_btn = QPushButton(self.login_window)
        self.go_to_signup_window_btn.setText("Go To Sign Up")
        self.go_to_signup_window_btn.setStyleSheet("""
       QPushButton {
          background-color: #C53151;  
          color: #76D7EA;
          border: 3px solid #0081AB;     
          border-radius: 10px;         
          padding: 4px;
                    
        }
        QPushButton:hover {
            background-color: #B768A2;  
        }
        """)

        self.log_sub_btn = QPushButton(self.login_window)
        self.log_sub_btn.setText("Submit")
        self.log_sub_btn.setStyleSheet("""
       QPushButton {
          background-color: #C53151;  
          color: #76D7EA;
          border: 3px solid #0081AB;     
          border-radius: 10px;         
          padding: 4px;
                    
        }
        QPushButton:hover {
            background-color: #B768A2;  
        }
        """)

        self.forgot_password_radio = QRadioButton(self.login_window)
        self.forgot_password_radio.setText("Forgot Password ?")
        self.forgot_password_radio.setStyleSheet("""
        QRadioButton {
           background-color: #2E5894;  
           color: #FFFFFF;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QRadioButton:hover {
            background-color: #0081AB;  
        }
        """)

        self.log_forgot_password_line_edit = QLineEdit(self.login_window)
        self.log_forgot_password_line_edit.setPlaceholderText("WHAT IS YOUR FAVORITE WORD ?")

        self.log_user2_line_edit = QLineEdit(self.login_window)
        self.log_user2_line_edit.setPlaceholderText("user_name")
        self.log_user2_line_edit.setStyleSheet("""
        QLineEdit {
           background-color: #2E5894;  
           color: #FFFFFF;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QLineEdit:hover {
            background-color: #0081AB;  
        }
        """)

        self.log_password2_line_edit = QLineEdit(self.login_window)
        self.log_password2_line_edit.setPlaceholderText("WHAT IS YOUR FAVORITE WORD ?")
        self.log_password2_line_edit.setStyleSheet("""
        QLineEdit {
           background-color: #2E5894;  
           color: #FFFFFF;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QLineEdit:hover {
            background-color: #0081AB;  
        }
        """)

        self.log_sub2_btn = QPushButton(self.login_window)
        self.log_sub2_btn.setText("Submit")
        self.log_sub2_btn.setStyleSheet("""
       QPushButton {
          background-color: #C53151;  
          color: #76D7EA;
          border: 3px solid #0081AB;     
          border-radius: 10px;         
          padding: 4px;
                    
        }
        QPushButton:hover {
            background-color: #B768A2;  
        }
        """)

        self.log_central = QWidget(self)
        self.log_layout = QVBoxLayout(self.log_central)
        self.log_layout.setContentsMargins(200, 100, 200, 100)
        self.log_hlayout = QHBoxLayout(self.log_central)
        self.log_layout2 = QVBoxLayout(self.log_central)
        
        self.log_layout.addWidget(self.timer_label)
        self.log_layout.addWidget(self.login_label)
        self.log_layout.addWidget(self.log_user_line_edit)
        self.log_layout.addWidget(self.log_password_label)
        self.log_layout.addWidget(self.log_password_line_edit)
        self.log_layout.addLayout(self.log_hlayout)
        self.log_hlayout.addWidget(self.go_to_signup_window_btn)
        self.log_hlayout.addWidget(self.log_sub_btn)
        
        self.log_layout.addLayout(self.log_layout2)
        self.log_layout2.addWidget(self.show_user_label)
        self.log_layout2.addWidget(self.log_user2_line_edit)
        self.log_layout2.addWidget(self.show_password_label)
        self.log_layout2.addWidget(self.log_password2_line_edit)
        self.log_layout2.addWidget(self.log_sub2_btn)
        self.log_user2_line_edit.hide()
        self.log_password2_line_edit.hide()
        self.log_sub2_btn.hide()

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(False)
        self.button_group.addButton(self.forgot_password_radio)
        self.forgot_password_radio.toggled.connect(self.radio_toggled)
        self.log_hlayout.addWidget(self.forgot_password_radio)
        self.show_password = QLineEdit(self.login_window)
        self.show_password.setReadOnly(True)
        self.show_password.setStyleSheet("""
        QLineEdit {
           background-color: #2E5894;  
           color: #FFFFFF;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QLineEdit:hover {
            background-color: #0081AB;  
        }
        """)
        self.log_layout2.addWidget(self.show_password)
        self.show_password.hide()

        self.go_to_signup_window_btn.clicked.connect(self.go_to_sign_up)
        self.log_sub_btn.clicked.connect(self.check_login_inputs_val)
        self.log_sub2_btn.clicked.connect(self.show_pass)

        self.login_window.setCentralWidget(self.log_central)
        self.login_window.setWindowTitle('Signup_Login')
        self.login_window.show()
        
    #***********  END LOGIN WINDOW   ************

    def start_timer(self):
        self.end_time = QDateTime.currentDateTime().addSecs(self.countdown)  
        self.timer = QTimer(self.login_window)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        self.timer_label.setVisible(True)
        self.log_user_line_edit.setReadOnly(True)
        self.log_password_line_edit.setReadOnly(True)
        self.log_user2_line_edit.setReadOnly(True)
        self.log_password2_line_edit .setReadOnly(True)
        self.log_forgot_password_line_edit.setReadOnly(True)
        self.log_sub_btn.setEnabled(False)
        self.log_sub2_btn.setEnabled(False)
        self.go_to_signup_window_btn.setEnabled(False)
        self.forgot_password_radio.setEnabled(False)
        
    # updating time     
    def update_time(self):
        current_time = QDateTime.currentDateTime()
        remaining_time = self.end_time.toSecsSinceEpoch() - current_time.toSecsSinceEpoch()
        
        if remaining_time <= 0:
            self.timer.stop()
            self.timer_label.setText("remaining time : 00:00")
            self.max_error = 0
            self.timer_label.setVisible(False)
            self.log_user_line_edit.setReadOnly(False)
            self.log_password_line_edit.setReadOnly(False)
            self.log_user2_line_edit.setReadOnly(False)
            self.log_password2_line_edit .setReadOnly(False)
            self.log_forgot_password_line_edit.setReadOnly(False)
            self.log_sub_btn.setEnabled(True)
            self.log_sub2_btn.setEnabled(True)
            self.go_to_signup_window_btn.setEnabled(True)
            self.forgot_password_radio.setEnabled(True)
            
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        self.timer_label.setText(f"remaining time : {minutes:02d}:{seconds:02d}")
                
    def go_to_sign_up(self):
        self.login_window.close()
        self.sign_up_window()

    def radio_toggled(self, checked):
        if checked :
            self.log_user2_line_edit.show()
            self.log_password2_line_edit.show()
            self.log_sub2_btn.show()
                
        else:
            self.log_user2_line_edit.hide()
            self.log_password2_line_edit.hide()
            self.log_sub2_btn.hide()
            
    def find_user_pass(self, user_name, security_answer):
        try:
            db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users_file.db')
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            cursor.execute('''
                SELECT password FROM Users WHERE user_name = ? AND security_answer = ?
            ''', (user_name, security_answer))

            result = cursor.fetchone()
            return result[0] if result else None
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            if conn:
                conn.close()
                
    def show_pass(self):
        if not self.show_password.isVisible():
            self.show_password.setVisible(True)
        log_text = self.log_user2_line_edit.text() 
        pass_text = self.log_password2_line_edit.text()  
        resault = self.find_user_pass(log_text, pass_text)     
        if resault is not None:
            self.show_password.setText(f"{resault}")
        else :
            self.show_password.setText(f"password does not exist")       
            
    def update_combo_box(self, text):
        self.city_combo_box.clear()
        for word in self.default_cities:
            if text.lower() in word.lower():
                self.city_combo_box.addItem(word) 
                
    def set_city_line_edit(self, index):
        text = self.city_combo_box.itemText(index)
        self.city_line_edit.setText(text) 

    def set_year_line_edit(self, index):
        text = self.year_combo_box.itemText(index)
        self.year_line_edit.setText(text)

    def set_mounth_line_edit(self, index):
        text = self.mounth_combo_box.itemText(index)
        self.mounth_line_edit.setText(text)

    def set_day_line_edit(self, index):
        text = self.day_combo_box.itemText(index)
        self.day_line_edit.setText(text)                 
      
    def open_login_window(self):
        self.signup_window.close()
        self.login_window = QMainWindow() 
        self.central_widget = QWidget()
        self.login_window.setGeometry(100, 100, 500, 500)
        self.layout = QVBoxLayout(self.central_widget)
        self.line_edit3 = QPushButton("btn_login", self.central_widget)
        self.layout.addWidget(self.line_edit3) 
        self.central_widget.setLayout(self.layout)
        self.layout.setContentsMargins(390, 40, 390, 40)
        self.login_window.setCentralWidget(self.central_widget)
        
        self.login_window.setWindowTitle('QLineEdit')
        self.login_window.show()
        
    def create_user_file(self):
        try:
            db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users_file.db')
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # Create table if not exists
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    first_name TEXT,
                    last_name TEXT,
                    user_name TEXT PRIMARY KEY,
                    password TEXT,
                    security_answer TEXT,
                    email TEXT,
                    phone_number TEXT,
                    city TEXT,
                    birth_year TEXT,
                    birth_month TEXT,
                    birth_day TEXT
                )
            ''')

            user_info = (
                self.first_name, self.last_name, self.user_name, self.password,
                self.security_question, self.email, self.phone_number, self.city,
                self.birth_year, self.birth_mounth, self.birth_day
            )

            cursor.execute('SELECT * FROM Users WHERE user_name = ?', (self.user_name,))
            existing_user = cursor.fetchone()

            if not existing_user:
                cursor.execute('''
                    INSERT INTO Users (first_name, last_name, user_name, password, security_answer, email, phone_number, city, birth_year, birth_month, birth_day)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', user_info)
                conn.commit()

                if self.close_user_db_label.isVisible():
                    self.close_user_db_label.setVisible(False)
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            if not self.close_user_db_label.isVisible():
                self.close_user_db_label.setVisible(True)
        finally:
            if conn:
                conn.close()

        
    def set_user_info(self):
        self.first_name = self.first_name_line_edit.text()
        self.last_name = self.last_name_line_edit.text() 
        self.user_name = self.user_name_line_edit.text()
        self.password = self.password_line_edit.text()
        self.repeat_password = self.repeat_password_line_edit.text()
        self.security_question = self.security_question_line_edit.text()
        self.email = self.email_line_edit.text()
        self.phone_number = self.phone_number_line_edit.text()
        self.city = self.city_line_edit.text()
        self.birth_day = self.day_line_edit.text()
        self.birth_mounth = self.mounth_line_edit.text()
        self.birth_year = self.year_line_edit.text()

    def close_signup_open_login(self):
        self.set_user_info()
        
        first_name_val = self.name_val(self.first_name)  
        last_name_val = self.name_val(self.last_name)
        password_val = self.password_val(self.password)
        repeat_password_val = self.password_val(self.repeat_password)
        
        passwords_eq = (self.password == self.repeat_password)
        
        security_val = (self.security_question != "")
        email_val = self.email_val(self.email)
        phone_number_val = self.phone_number_val(self.phone_number)
        birth_date = f"{self.birth_year}-{self.birth_mounth}"
        day_val = self.day_val(self.birth_day, self.birth_mounth)
        mounth_val = self.mounth_val(self.birth_mounth)
        year_val = self.year_val(self.birth_year)
        val_list = [first_name_val, last_name_val, password_val, repeat_password_val,
                    passwords_eq, email_val, phone_number_val, year_val, mounth_val, day_val, security_val]
        
        if False in val_list:
            if not val_list[0]:
                if self.first_name == "":
                    self.first_name_label.setText("please fill the gap")
                if not self.first_name_label.isVisible() :    
                    self.first_name_label.setVisible(True)
            else:
                self.first_name_label.setVisible(False)
                self.first_name_label.setText("first_name is not valid!")
                
            if not val_list[1]:
                if self.last_name == "":
                    self.last_name_label.setText("please fill the gap")
                elif self.last_name != "":
                    self.last_name_label.setText("last_name is not valid!")   
                if not self.last_name_label.isVisible():     
                    self.last_name_label.setVisible(True)
            else:
                self.last_name_label.setText("last_name is not valid!")
                self.last_name_label.setVisible(False)   
                
            
            if not val_list[2]:
                if self.password == "":
                    self.password_label.setText("please fill the gap")
                elif self.password != "":
                    self.password_label.setText("password is not valid!")    
                if not self.password_label.isVisible():
                    self.password_label.setVisible(True)
            else : 
                self.password_label.setVisible(False)       
                self.password_label.setText("password is not valid!")
            
                    
            if not val_list[3]:
                if self.repeat_password == "":
                    self.repeat_password_label.setText("please fill the gap")
                    
                elif self.repeat_password != "":
                    self.repeat_password_label.setText("repeated_password is not valid!")
                    #self.repeat_password_label.setVisible(True)    
                    if self.password != "" and self.repeat_password != self.password:
                        self.repeat_password_label.setText("not match!") 
                    elif self.password == "":
                        self.repeat_password_label.setText("not match!")  
                    self.repeat_password_label.setVisible(True)              
                if not self.repeat_password_label.isVisible():
                    self.repeat_password_label.setVisible(True)
            elif val_list[3] and self.repeat_password != self.password:
                        self.repeat_password_label.setText("not match!")    
                        if not self.repeat_password_label.isVisible():
                            self.repeat_password_label.setVisible(True)    
            else:
                self.repeat_password_label.setVisible(False)
                self.repeat_password_label.setText("repeated_password is not valid!") 
            
            if not val_list[5]:
                if self.email == "":
                    self.email_label.setText("please fill the gap")
                elif self.email != "":
                    self.email_label.setText("email address is not valid!")    
                if not self.email_label.isVisible():
                    self.email_label.setVisible(True)    
            else:
                self.email_label.setVisible(False)
                self.email_label.setText("email address is not valid!")    
                
            if not val_list[6]:
                if self.phone_number == "":
                    self.phone_number_label.setText("please fill the gap")
                elif self.phone_number != "":
                    self.phone_number_label.setText("phone_number is not valid!")     
                if not self.phone_number_label.isVisible():
                    self.phone_number_label.setVisible(True)    
            else:
                self.phone_number_label.setVisible(False)
                self.phone_number_label.setText("phone_number is not valid!") 
                
            if not val_list[7]:
                if self.birth_year == "":
                    self.year_label.setText("please fill the gap")
                elif self.birth_year != "":
                    self.year_label.setText("birth_year is not valid!")     
                if not self.year_label.isVisible():
                    self.year_label.setVisible(True)    
            else:
                self.year_label.setVisible(False)
                self.year_label.setText("birth_year is not valid!")
                
            if not val_list[8]:
                if self.birth_mounth == "":
                    self.mounth_label.setText("please fill the gap")
                elif self.birth_mounth != "":
                    self.mounth_label.setText("birth_mounth is not valid!")     
                if not self.mounth_label.isVisible():
                    self.mounth_label.setVisible(True)    
            else:
                self.mounth_label.setVisible(False)
                self.mounth_label.setText("birth_mounth is not valid!")
                
            if not val_list[9]:
                if self.birth_day == "":
                    self.day_label.setText("please fill the gap")
                elif self.birth_day != "":
                    self.day_label.setText("birth_day is not valid!")     
                if not self.day_label.isVisible():
                    self.day_label.setVisible(True)    
            else:
                self.day_label.setVisible(False)
                self.day_label.setText("birth_day is not valid!")  
                
            if not val_list[10]:
                if not self.security_question_label.isVisible():
                    self.security_question_label.setVisible(True)
            else:
                if self.security_question_label.isVisible():
                    self.security_question_label.setVisible(False)                 
                
            if self.city == "":
                if not self.city_label.isVisible():
                    self.city_label.setVisible(True) 
            else:
                if self.city_label.isVisible():
                    self.city_label.setVisible(False)                
        else:
            self.create_user_file()
            if not self.close_user_db_label.isVisible():
                self.signup_window.close()
                self.Login_window()
                
    def search_user(self, user_name, password):
        try:
            db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users_file.db')
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            cursor.execute('''
                SELECT first_name, last_name, user_name, password, security_answer, email, phone_number, city, birth_year, birth_month, birth_day
                FROM Users
                WHERE user_name = ? AND password = ?
            ''', (user_name, password))

            result = cursor.fetchone()
            if result:
                (self.first_name, self.last_name, self.user_name, self.password,
                 self.security_question, self.email, self.phone_number, self.city,
                 self.birth_year, self.birth_mounth, self.birth_day) = result
                return True
            else:
                return False
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return False
        finally:
            if conn:
                conn.close()
            
    def check_login_inputs_val(self):
        user_text = self.log_user_line_edit.text()
        pass_text = self.log_password_line_edit.text()
        if user_text and pass_text:
            if self.search_user(user_text, pass_text):
                self.set_visibility(False)
                self.login_window.close()
                
                user_info = [self.first_name, self.last_name, self.user_name, self.password,
                        self.security_question, self.email, self.phone_number, self.city,
                        self.birth_year, self.birth_mounth, self.birth_day]
                
                self.set_user_attr(user_info)
                self.Main_window()
            else :
                self.check_error()
        else :
            self.check_error()      
    
    def set_visibility(self, isvisible):
        self.login_label.setVisible(isvisible)
        self.log_password_label.setVisible(isvisible) 
        
    def check_error(self):
        if self.max_error < 2:
            self.max_error += 1
            if not self.login_label.isVisible():
                self.set_visibility(True)
        elif self.max_error == 2:
            if self.login_label.isVisible():
                self.set_visibility(False)
            self.start_timer()

    def new_sign_up(self):
        self.sign_up_window() 

# ***********  END SIGNUP_LOGIN CLASS   ************ 