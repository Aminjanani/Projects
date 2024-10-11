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
from Signup_Login import signup_login

# ***********   START WELCOME CLASS    **************            
class welcome(signup_login):  
    default_cities = ['Tehran', 'Isfahan', 'Shiraz', 'Yazd', 'Mashhad', 'Sari', 'Ardebil', 'Bushehr', 'Ahvaz', 'Hamedan']
                  
    def __init__(self) :
        super().__init__()           
        signup_login.__init__(self)
        #self.welcome_page()

    def welcome_page(self):
       self.window = QMainWindow()
       self.window.setGeometry(100, 100, 700, 480)
       self.btn_sign_up = QPushButton("SIGN UP")
       self.btn_login = QPushButton("LOGIN")
       self.welcome_pic = QLabel(self.window)
       self.pixmap = QPixmap("C:/Users/Asa/Desktop/Pr_Ap/Polish_mr_k.jpg")
       self.welcome_pic.setPixmap(self.pixmap)

       self.btn_style ="""
       QPushButton {
          background-color: #1f3057;  
          color: #fdd906;                
          border: 3px solid #a7c6eb;     
          border-radius: 5px;         
          padding: 10px;
                    
       }
       QPushButton:hover {
           background-color: #228B22;  
       }
       """

       self.btn_sign_up.setStyleSheet(self.btn_style)
       self.btn_login.setStyleSheet(self.btn_style)

       self.background = QLabel(self.window)
       self.background.setPixmap(QPixmap('C:/Users/Asa/Desktop/Pr_Ap/sport-of-tycoons-carl-barks.jpg'))
       self.background.setScaledContents(True)
       self.welcome_pic.setScaledContents(True)
       self.window.resizeEvent = self.on_resize
       self.welcome_pic.resizeEvent = self.on_resize
       self.central_widget = QWidget()
       self.window.setCentralWidget(self.central_widget)
       self.layout = QVBoxLayout(self.central_widget)
       self.layout.setContentsMargins(190, 30, 190, 30)
       self.layout.addWidget(self.btn_sign_up)
       self.layout.addWidget(self.btn_login)
       self.layout.addChildWidget(self.welcome_pic)
       self.timer = QTimer(self)
       self.timer.timeout.connect(self.hide_welcome_pic)
       self.timer.setSingleShot(True)  
       self.timer.start(4000)

       self.btn_sign_up.clicked.connect(self.btn_clicked_sign_up)
       self.btn_login.clicked.connect(self.btn_clicked_login)
       
       self.window.setCentralWidget(self.central_widget)
       self.window.show()

    def on_resize(self, event):
        self.welcome_pic.setGeometry(self.window.rect())
        self.background.setGeometry(self.window.rect())
            
    def hide_welcome_pic(self):
        self.welcome_pic.hide()

    def btn_clicked_sign_up(self):
        self.window.close()
        self.sign_up_window()

    def btn_clicked_login(self):
        self.window.close()
        self.Login_window()
# ***********  END WELCOME CLASS  ************ 
