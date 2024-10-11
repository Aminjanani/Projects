# AP_Project : Personal Accounting
# Group members : Mohammad Reza Eghbali, Amin Janani

import base64
from datetime import datetime
import re, sys, time, pandas as pd, numpy as np
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (QPushButton, QWidget, QMainWindow, QFileDialog, 
                             QApplication, QLabel, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QComboBox, QCompleter, QListView, 
                             QRadioButton, QButtonGroup, QTextBrowser, QCheckBox)
from PyQt6.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt6.QtCore import Qt, QStringListModel, QTimer, QTime, QDateTime, QDate

#check_validation checks if the user's attributes are valid
class check_validation:    
    valid_years = [year for year in range(1920, 2005)]
    valid_mounths = {"january": '31', "february": '29', "march": '31',
                     "april": '30', "may": '31', "june": '30',
                     "july": '31', "august": '31', "september": '30',
                     "october": '31', "november": '30', "december": '31'}
    
    def __init__(self):
        self.name_pattern = r"^[A-Za-z]{1,}$"
        self.phone_number_pattern = r"^09[0-9]{9}$"
        self.password_pattern = r"(?=(.*[a-z]){1,})(?=(.*[A-Z]){1,})(?=(.*\d){1,})(?=(.*[!@#$%^&+*()_\-<>/?;]){1,}){6,}"
        self.email_pattern = r"^[A-Za-z0-9]{5,}@(gmail|yahoo).com$"
        self.digit_pattern = r"^\d{1,14}$"
        self.decriptiion_pattern = r"^.{1,14}$"
        self.category_pattern = r"^[A-Za-z0-9]{1,15}$"
        self.mounth_pattern = r"^([1-9]|1[0-2])$"
        self.year_pattern = r"(19[2-9][0-9]|200[0-5])"
        self.revexp_year_pattern = r"(19[3-9][0-9]|20[0-5][0-9]|)"
        
    #checking the first name, last name and user name validation    
    def name_val(self, name):
        if re.match(self.name_pattern, name):
            return True
        else:
            return False
        
    #checking the phone number validation
    def phone_number_val(self, phone_number):
        if re.match(self.phone_number_pattern, phone_number) :
            return True
        else:
            return False
        
    #checking the password validation
    def password_val(self, password):
        if re.match(self.password_pattern, password):
            return True
        else:
            return False
        
    #checking the email adress validation
    def email_val(self, email):
        if re.match(self.email_pattern, email):
            return True
        else:
            return False
        
    #checking the year, mounth and day validation   
    def year_val(self, year):
        year_val_resault = False
        if re.match(self.year_pattern, year):
            year_val_resault = True  
        return year_val_resault
    
    #checking the year, mounth and day validation for revenue and expense date
    def revexp_year_val(self, year):
        revexp_year_val_resault = False
        if re.match(self.revexp_year_pattern, year):
            revexp_year_val_resault = True
        return revexp_year_val_resault    
        
    def mounth_val(self, mounth):  
        mounth_val_resault = False      
        if mounth.lower() in self.valid_mounths.keys():
            mounth_val_resault = True 
        return mounth_val_resault    
              
    def day_val(self, day, mounth):   
        day_val_resault = None    
        try:
            if int(day) <= int(self.valid_mounths[mounth.lower()]) and int(day) >= 1:
                day_val_resault = True
            else:
                raise Exception    
        except Exception as e:
            day_val_resault = False 
        return day_val_resault    
                   
    def digit_val(self, digit):
        if re.match(self.digit_pattern, digit):
            return True
        else:
            return False   