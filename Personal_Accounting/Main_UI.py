from User import user
import Validation
import sqlite3 as sql
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# This class contains the main menu of the app, including the revenue, expence, category, search, report and setting pages as well as exit button.
class MainUI(Validation.QMainWindow, user, Validation.check_validation):
    default_type_combo = ['Cash', 'Cheque', 'Digital currency']
    months = {"January": '31', "February": '29', "March": '31',
              "April": '30', "May": '31', "June": '30',
              "July": '31', "August": '31', "September": '30',
              "October": '31', "November": '30', "December": '31'}
    category_combo = ['wage', 'saving', 'allowance']
    dark_mode = ["Lite", "Dark"]
    delete_information =["user", "transaction", "just revenue", "just expense"]
    
    def __init__(self):
        super().__init__()  
        #user.__init__(self)
        Validation.check_validation.__init__(self)
        self.window_title = 'Main Menu'
        self.rev_amount = ""
        self.rev_day = ""
        self.rev_month = ""
        self.rev_year = ""
        self.rev_source = ""
        self.rev_desc = ""
        self.rev_type = ""
        self.exp_amount = ""
        self.exp_day = ""
        self.exp_month = ""
        self.exp_year = ""
        self.exp_source = ""
        self.exp_desc = ""
        self.exp_type = ""
        self.searched_word = ""
        self.curr_dir = os.path.dirname(os.path.abspath(__file__))
        self.curr_info = [self.first_name, self.last_name, self.user_name,
                          self.password, self.security_question, self.email, self.phone_number, self.city,
                          self.birth_year, self.birth_mounth, self.birth_day]
        #self.Main_window()

    def Main_window(self):
        self.revenue_file = self.user_name + f"_revenue.db"
        self.expense_file = self.user_name + f"_expense.db"
        self.category_file = self.user_name + f"_category.db"
        
        img_db_path = os.path.join(self.curr_dir, 'images.db')
        self.conn = sql.connect(img_db_path)
        self.cursor = self.conn.cursor()
        
        self.setWindowTitle(self.window_title)
        self.setGeometry(400, 100, 600, 300)
        self.mainWidget = Validation.QWidget(self)
        self.mainLayout = Validation.QHBoxLayout(self.mainWidget)
        
        rev_db = os.path.join(self.curr_dir, self.revenue_file)
        rev_conn = sql.connect(rev_db)
        rev_cur = rev_conn.cursor()
        rev_create_table_query = '''CREATE TABLE IF NOT EXISTS REVENUE (
                                    amount INT NOT NULL,
                                    source TEXT NOT NULL,
                                    description TEXT,
                                    type TEXT NOT NULL,
                                    year INT NOT NULL,
                                    month TEXT NOT NULL,
                                    day INT NULL, 
                                    UNIQUE(amount, source, 
                                    description, type, year, month, day))'''
        rev_cur.execute(rev_create_table_query)
        rev_cur.close() 
        rev_conn.close()                            
        
        exp_db = os.path.join(self.curr_dir, self.expense_file)
        exp_conn = sql.connect(exp_db)
        exp_cur = exp_conn.cursor()
        exp_create_table_query = '''CREATE TABLE IF NOT EXISTS EXPENSE (
                                    amount INT NOT NULL,
                                    source TEXT NOT NULL,
                                    description TEXT,
                                    type TEXT NOT NULL,
                                    year INT NOT NULL,
                                    month TEXT NOT NULL,
                                    day INT NULL, 
                                    UNIQUE(amount, source, 
                                    description, type, year, month, day))'''
        
        exp_cur.execute(exp_create_table_query)
        exp_cur.close() 
        exp_conn.close()
        
        cat_db = os.path.join(self.curr_dir, self.category_file)
        cat_conn = sql.connect(cat_db)
        cat_cur = cat_conn.cursor()
        cat_create_table_query = '''CREATE TABLE IF NOT EXISTS CATEGORY 
                                (
                                    category TEXT, 
                                    UNIQUE (category)
                                )'''
        cat_cur.execute(cat_create_table_query)
        cat_cur.close() 
        cat_conn.close()                       

        self.leftWidget = Validation.QWidget(self)
        self.leftWidget.setStyleSheet("background-color: #FBE870;")
        self.leftLayout = Validation.QVBoxLayout(self.leftWidget)
        self.hlayout = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout1 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout2 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout3 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout4 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout5 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout6 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout7 = Validation.QHBoxLayout(self.leftWidget)
        self.hlayout8 = Validation.QHBoxLayout(self.leftWidget)

        self.leftLayout.addLayout(self.hlayout)
        self.leftLayout.addLayout(self.hlayout2)
        self.leftLayout.addLayout(self.hlayout3)
        self.leftLayout.addLayout(self.hlayout4)
        self.leftLayout.setContentsMargins(0, 60, 90, 250)
        self.line_main_style = """
        QLineEdit {
           background-color: #c9a8ce; 
           color: #0A0A0A;               
           border: 3px solid #34568B;    
           border-radius: 10px;        
           padding: 4px;
        }
        QLineEdit:hover {
            background-color: #0081AB; 
        }
        """
        self.mainLayout.addWidget(self.leftWidget, 80)  

        self.rightWidget = Validation.QWidget(self)
        self.rightWidget.setStyleSheet("background-color: #52afb6;")
        self.rightLayout = Validation.QVBoxLayout(self.rightWidget)
        self.btn_main_style ="""
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
        """
        self.combo_main_style ="""
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
        """
        self.check_box_style ="""
        QCheckBox {
           background-color: #2E5894;  
           color: #FFFFFF;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QCheckBox:hover {
            background-color: #0081AB;  
        }
        """
        
        self.view_style ="""
        QTextBrowser {
           background-color: #93CCEA;  
           color: red;                
           border: 1px solid #ED0A3F;     
           border-radius: 10px;         
           padding: 4px;
                    
        }
        QTableView:hover {
            background-color: #0081AB;  
        }
        """
        
        self.timer_label = Validation.QLabel("Elapsed Time: 00:00:00", self)
        self.timer_label.setStyleSheet("background-color:#FBE870 ;  color : #ED0A3F ")
        self.timer_label.setFixedSize(200, 40)
        self.timer_label.setAlignment(Validation.Qt.AlignmentFlag.AlignCenter)
        self.start_time = Validation.QTime.currentTime()
        self.timer = Validation.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        self.rightLayout.addWidget(self.timer_label)

        self.btn_revenue = Validation.QPushButton("Revenue")
        self.btn_revenue.setStyleSheet(self.btn_main_style)
        self.btn_expense = Validation.QPushButton("Expense")
        self.btn_expense.setStyleSheet(self.btn_main_style)
        self.btn_category = Validation.QPushButton("Category")
        self.btn_category.setStyleSheet(self.btn_main_style)
        self.btn_search = Validation.QPushButton("Search")
        self.btn_search.setStyleSheet(self.btn_main_style)
        self.btn_report = Validation.QPushButton("Report")
        self.btn_report.setStyleSheet(self.btn_main_style)
        self.btn_settings = Validation.QPushButton("Setting")
        self.btn_settings.setStyleSheet(self.btn_main_style)
        self.btn_exit = Validation.QPushButton("Exit")
        self.btn_exit.setStyleSheet(self.btn_main_style)

        self.rightLayout.addWidget(self.btn_revenue)
        self.rightLayout.addWidget(self.btn_expense)
        self.rightLayout.addWidget(self.btn_category)
        self.rightLayout.addWidget(self.btn_search)
        self.rightLayout.addWidget(self.btn_report)
        self.rightLayout.addWidget(self.btn_settings)
        self.rightLayout.addWidget(self.btn_exit)
        self.mainLayout.addWidget(self.rightWidget, 20)  

        self.btn_revenue.clicked.connect(self.revenue)
        self.btn_expense.clicked.connect(self.expense)
        self.btn_category.clicked.connect(self.category)
        self.btn_search.clicked.connect(self.search)
        self.btn_report.clicked.connect(self.report)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_exit.clicked.connect(self.exit)

        self.setCentralWidget(self.mainWidget)
        self.show()

        self.current_layout = None
        
    def update_timer(self):
        elapsed_time = Validation.QTime(0, 0).addSecs(self.start_time.secsTo(Validation.QTime.currentTime()))
        self.timer_label.setText(f"Elapsed Time: {elapsed_time.toString('hh:mm:ss')}")    

    def revenue(self):
        if self.current_layout == 'revenue':
            return
        self.current_layout = 'revenue'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)
        self.clear_layout(self.hlayout8)

        self.amount_of_revenue_line = Validation.QLineEdit()
        self.amount_of_revenue_label = Validation.QLabel()
        self.amount_of_revenue_label.setVisible(False)
        self.amount_of_revenue_label.setText("please enter a valid amount(just digits)!")
        self.amount_of_revenue_label.setStyleSheet('color: red')
        self.amount_of_revenue_line.setPlaceholderText("Amount Of Revenue")
        self.amount_of_revenue_line.setStyleSheet(self.line_main_style)
        self.day_of_revenue_line = Validation.QLineEdit()
        self.day_of_revenue_line.setPlaceholderText("Day")
        self.day_of_revenue_line.setStyleSheet(self.line_main_style)
        self.day_of_revenue_label = Validation.QLabel()
        self.day_of_revenue_label.setVisible(False)
        self.day_of_revenue_label.setText("please enter a valid day")
        self.day_of_revenue_label.setStyleSheet('color: red')
        self.month_of_revenue_line = Validation.QLineEdit()
        self.month_of_revenue_line.setPlaceholderText("Month")
        self.month_of_revenue_line.setStyleSheet(self.line_main_style)
        self.month_of_revenue_label = Validation.QLabel()
        self.month_of_revenue_label.setVisible(False)
        self.month_of_revenue_label.setText("please enter a valid mont(just letters)!")
        self.month_of_revenue_label.setStyleSheet('color: red')
        self.year_of_revenue_line = Validation.QLineEdit()
        self.year_of_revenue_line.setPlaceholderText("Year")
        self.year_of_revenue_line.setStyleSheet(self.line_main_style)
        self.year_of_revenue_label = Validation.QLabel()
        self.year_of_revenue_label.setVisible(False)
        self.year_of_revenue_label.setText("please enter a valid year")
        self.year_of_revenue_label.setStyleSheet('color: red')
        self.source_of_revenue_line = Validation.QLineEdit()
        self.source_of_revenue_line.setPlaceholderText("Source Of Revenue")
        self.source_of_revenue_line.setStyleSheet(self.line_main_style)
        self.source_of_revenue_label = Validation.QLabel()
        self.source_of_revenue_label.setVisible(False)
        self.source_of_revenue_label.setText("please fill the gap!")
        self.source_of_revenue_label.setStyleSheet('color: red')
        self.close_rev_file_label = Validation.QLabel()
        self.close_rev_file_label.setText("please close the revenue file first!")
        self.close_rev_file_label.setStyleSheet('color: red')
        self.close_rev_file_label.setVisible(False)
        self.source_of_revenue_combo_box = Validation.QComboBox()
        self.source_of_revenue_combo_box.setStyleSheet(self.combo_main_style)
        
        self.create_user_category_database()
        self.add_item_category_combo()

        self.description_revenue_line = Validation.QLineEdit()
        self.description_revenue_line.setPlaceholderText("Description Of Revenue")
        self.description_revenue_line.setStyleSheet(self.line_main_style)
        self.desc_of_revenue_label = Validation.QLabel()
        self.desc_of_revenue_label.setText('please enter a sentence with less than equal 100 characters!')
        self.desc_of_revenue_label.setStyleSheet('color: red')
        self.desc_of_revenue_label.setVisible(False)
        self.type_of_revenue_line = Validation.QLineEdit()
        self.type_of_revenue_line.setPlaceholderText("Type Of Revenue")
        self.type_of_revenue_line.setStyleSheet(self.line_main_style)
        self.type_of_revenue_line.setReadOnly(True)
        self.type_of_revenue_label = Validation.QLabel()
        self.type_of_revenue_label.setVisible(False)
        self.type_of_revenue_label.setText("please fill the gap!")
        self.type_of_revenue_label.setStyleSheet('color: red')

        self.type_of_revenue_combo_box = Validation.QComboBox()
        self.type_of_revenue_combo_box.setStyleSheet(self.combo_main_style)
        self.year_of_revenue_combo_box = Validation.QComboBox()
        self.year_of_revenue_combo_box.setStyleSheet(self.combo_main_style)
        self.month_of_revenue_combo_box = Validation.QComboBox()
        self.month_of_revenue_combo_box.setStyleSheet(self.combo_main_style)
        self.day_of_revenue_combo_box = Validation.QComboBox()
        self.day_of_revenue_combo_box.setStyleSheet(self.combo_main_style)
        self.btn_sub_revenue = Validation.QPushButton("Submit")
        self.btn_sub_revenue.setStyleSheet(self.btn_main_style)
        
        self.leftLayout.addWidget(self.amount_of_revenue_label)
        self.leftLayout.addWidget(self.amount_of_revenue_line)
        self.leftLayout.addLayout(self.hlayout1)
        self.hlayout1.addWidget(self.year_of_revenue_label)
        self.hlayout1.addWidget(self.month_of_revenue_label)
        self.hlayout1.addWidget(self.day_of_revenue_label)
        self.leftLayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.year_of_revenue_line)
        self.hlayout.addWidget(self.month_of_revenue_line)
        self.hlayout.addWidget(self.day_of_revenue_line)
        self.leftLayout.addLayout(self.hlayout2)
        self.hlayout2.addWidget(self.year_of_revenue_combo_box)
        self.hlayout2.addWidget(self.month_of_revenue_combo_box)
        self.hlayout2.addWidget(self.day_of_revenue_combo_box)

        for i in range(1, 32):
            self.day_of_revenue_combo_box.addItem(f"{i}")

        for month in self.months.keys():
            self.month_of_revenue_combo_box.addItem(month)

        for i in range(1930, 2051):
            self.year_of_revenue_combo_box.addItem(f"{i}")

        self.year_of_revenue_combo_box.activated[int].connect(self.set_year_revenue_line)
        self.month_of_revenue_combo_box.activated[int].connect(self.set_month_revenue_line)
        self.day_of_revenue_combo_box.activated[int].connect(self.set_day_revenue_line)

        self.source_of_revenue_combo_box.activated[int].connect(self.set_source_line)
        
        self.leftLayout.addWidget(self.source_of_revenue_label)
        self.leftLayout.addWidget(self.source_of_revenue_line)
        self.leftLayout.addWidget(self.source_of_revenue_combo_box)
        self.leftLayout.addWidget(self.desc_of_revenue_label)
        self.leftLayout.addWidget(self.description_revenue_line)
        self.leftLayout.addWidget(self.type_of_revenue_label)
        self.leftLayout.addWidget(self.type_of_revenue_line)
        self.leftLayout.addWidget(self.type_of_revenue_combo_box)
        self.leftLayout.addWidget(self.btn_sub_revenue)
        self.leftLayout.addWidget(self.close_rev_file_label)

        self.type_of_revenue_combo_box.addItems(self.default_type_combo)
        self.type_of_revenue_line.textChanged.connect(self.update_type_combo_box)
        #self.source_of_revenue_combo_box.addItems(self.category_combo)

        self.type_of_revenue_combo_box.activated[int].connect(self.set_revenue_line)
        
        self.btn_sub_revenue.clicked.connect(self.take_rev)
        
    def set_rev_attr(self):
        self.rev_amount = self.amount_of_revenue_line.text()
        self.rev_day = self.day_of_revenue_line.text()
        self.rev_month = self.month_of_revenue_line.text()
        self.rev_year = self.year_of_revenue_line.text()
        self.rev_source = self.source_of_revenue_line.text()
        self.rev_desc = self.description_revenue_line.text()
        self.rev_type = self.type_of_revenue_line.text()  
        
    def take_rev(self):
        rev_amount = self.amount_of_revenue_line.text()
        rev_day = self.day_of_revenue_line.text()
        rev_month = self.month_of_revenue_line.text()
        rev_year = self.year_of_revenue_line.text()
        rev_source = self.source_of_revenue_line.text()
        rev_desc = self.description_revenue_line.text()
        rev_type = self.type_of_revenue_line.text()
         
        rev_amount_val = self.digit_val(rev_amount)
        rev_day_val = self.day_val(rev_day, rev_month)
        rev_month_val = self.mounth_val(rev_month)
        rev_year_val = self.revexp_year_val(rev_year)
        if rev_source != "":
            rev_source_val = True
        else:
            rev_source_val = False
        if len(rev_desc) <= 100 :        
            rev_desc_val = True
        else :
            rev_desc_val = False 
        if rev_type != "":    
            rev_type_val = True
        else :
             rev_type_val = False   
         
        rev_val_list = [rev_amount_val, rev_day_val, rev_month_val, 
                        rev_year_val, rev_source_val, rev_desc_val, rev_type_val]
         
        if False in rev_val_list:
            if not rev_val_list[0]:
                if not self.amount_of_revenue_label.isVisible():
                    self.amount_of_revenue_label.setVisible(True)
            else:
                if self.amount_of_revenue_label.isVisible():
                    self.amount_of_revenue_label.setVisible(False)       
            if not rev_val_list[1]:
                if not self.day_of_revenue_label.isVisible():
                    self.day_of_revenue_label.setVisible(True)
            else:
                if self.day_of_revenue_label.isVisible():
                    self.day_of_revenue_label.setVisible(False) 
            if not rev_val_list[2]:
                if not self.month_of_revenue_label.isVisible():
                    self.month_of_revenue_label.setVisible(True)
            else:
                if self.month_of_revenue_label.isVisible():
                    self.month_of_revenue_label.setVisible(False) 
            if not rev_val_list[3]:
                if not self.year_of_revenue_label.isVisible():
                    self.year_of_revenue_label.setVisible(True)
            else:
                if self.year_of_revenue_label.isVisible():
                    self.year_of_revenue_label.setVisible(False) 
            if not rev_val_list[4]:
                if not self.source_of_revenue_label.isVisible():
                    self.source_of_revenue_label.setVisible(True)
            else:
                if self.source_of_revenue_label.isVisible():
                    self.source_of_revenue_label.setVisible(False) 
            if not rev_val_list[5]:
                if not self.desc_of_revenue_label.isVisible():
                    self.desc_of_revenue_label.setVisible(True)
            else:
                if self.desc_of_revenue_label.isVisible():
                    self.desc_of_revenue_label.setVisible(False) 
            if not rev_val_list[6]:
                if not self.type_of_revenue_label.isVisible():
                    self.type_of_revenue_label.setVisible(True)
            else:
                if self.type_of_revenue_label.isVisible():
                    self.type_of_revenue_label.setVisible(False)        
        else:
            if self.amount_of_revenue_label.isVisible():
                    self.amount_of_revenue_label.setVisible(False)
            if self.day_of_revenue_label.isVisible():
                    self.day_of_revenue_label.setVisible(False) 
            if self.month_of_revenue_label.isVisible():
                    self.month_of_revenue_label.setVisible(False)                 
            if self.year_of_revenue_label.isVisible():
                    self.year_of_revenue_label.setVisible(False)   
            if self.source_of_revenue_label.isVisible():
                    self.source_of_revenue_label.setVisible(False) 
            if self.desc_of_revenue_label.isVisible():
                    self.desc_of_revenue_label.setVisible(False)   
            if self.type_of_revenue_label.isVisible():
                    self.type_of_revenue_label.setVisible(False)
            self.set_rev_attr()
            self.create_user_revenue_databse()  
            
    def expense(self):
        if self.current_layout == 'expense':
            return
        self.current_layout = 'expense'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)
        self.clear_layout(self.hlayout8)

        self.amount_of_expense_line = Validation.QLineEdit()
        self.amount_of_expense_line.setPlaceholderText("Amount Of Expense")
        self.amount_of_expense_line.setStyleSheet(self.line_main_style)
        self.amount_of_expense_label = Validation.QLabel()
        self.amount_of_expense_label.setVisible(False)
        self.amount_of_expense_label.setText("please enter a valid amount(just digits)!")
        self.amount_of_expense_label.setStyleSheet('color: red')
        self.day_of_expense_line = Validation.QLineEdit()
        self.day_of_expense_line.setPlaceholderText("Day")
        self.day_of_expense_line.setStyleSheet(self.line_main_style)
        self.day_of_expense_label = Validation.QLabel()
        self.day_of_expense_label.setVisible(False)
        self.day_of_expense_label.setText("please enter a valid day!")
        self.day_of_expense_label.setStyleSheet('color: red')
        self.month_of_expense_line = Validation.QLineEdit()
        self.month_of_expense_line.setPlaceholderText("Month")
        self.month_of_expense_line.setStyleSheet(self.line_main_style)
        self.month_of_expense_label = Validation.QLabel()
        self.month_of_expense_label.setVisible(False)
        self.month_of_expense_label.setText("please enter a valid month(just letters)!")
        self.month_of_expense_label.setStyleSheet('color: red')
        self.year_of_expense_line = Validation.QLineEdit()
        self.year_of_expense_line.setPlaceholderText("Year")
        self.year_of_expense_line.setStyleSheet(self.line_main_style)
        self.year_of_expense_label = Validation.QLabel()
        self.year_of_expense_label.setVisible(False)
        self.year_of_expense_label.setText("please enter a valid year!")
        self.year_of_expense_label.setStyleSheet('color: red')
        self.source_of_expense_line = Validation.QLineEdit()
        self.source_of_expense_line.setPlaceholderText("Source Of Expense")
        self.source_of_expense_line.setStyleSheet(self.line_main_style)
        self.source_of_expense_label = Validation.QLabel()
        self.source_of_expense_label.setVisible(False)
        self.source_of_expense_label.setText("please fill the gap!")
        self.source_of_expense_label.setStyleSheet('color: red')
        self.description_expense_line = Validation.QLineEdit()
        self.description_expense_line.setPlaceholderText("Description Of Expense")
        self.description_expense_line.setStyleSheet(self.line_main_style)
        self.desc_of_expense_label = Validation.QLabel()
        self.desc_of_expense_label.setText('please enter a sentence with less than equal 100 characters!')
        self.desc_of_expense_label.setStyleSheet('color: red')
        self.desc_of_expense_label.setVisible(False)
        self.type_of_expense_line = Validation.QLineEdit()
        self.type_of_expense_line.setPlaceholderText("Type Of Expense")
        self.type_of_expense_line.setStyleSheet(self.line_main_style)
        self.type_of_expense_line.setReadOnly(True)
        self.type_of_expense_label = Validation.QLabel()
        self.type_of_expense_label.setVisible(False)
        self.type_of_expense_label.setText("please fill the gap!")
        self.type_of_expense_label.setStyleSheet('color: red')

        self.type_of_expense_combo_box = Validation.QComboBox()
        self.type_of_expense_combo_box.setStyleSheet(self.combo_main_style)
        self.year_of_expense_combo_box = Validation.QComboBox()
        self.year_of_expense_combo_box.setStyleSheet(self.combo_main_style)
        self.month_of_expense_combo_box = Validation.QComboBox()
        self.month_of_expense_combo_box.setStyleSheet(self.combo_main_style)
        self.day_of_expense_combo_box = Validation.QComboBox()
        self.day_of_expense_combo_box.setStyleSheet(self.combo_main_style)
        self.btn_sub_expense = Validation.QPushButton("Submit")
        self.btn_sub_expense.setStyleSheet(self.btn_main_style)
        
        self.leftLayout.addWidget(self.amount_of_expense_label)
        self.leftLayout.addWidget(self.amount_of_expense_line)
        self.leftLayout.addLayout(self.hlayout1)
        self.hlayout1.addWidget(self.year_of_expense_label)
        self.hlayout1.addWidget(self.month_of_expense_label)
        self.hlayout1.addWidget(self.day_of_expense_label)
        self.leftLayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.year_of_expense_line)
        self.hlayout.addWidget(self.month_of_expense_line)
        self.hlayout.addWidget(self.day_of_expense_line)
        self.leftLayout.addLayout(self.hlayout2)
        self.hlayout2.addWidget(self.year_of_expense_combo_box)
        self.hlayout2.addWidget(self.month_of_expense_combo_box)
        self.hlayout2.addWidget(self.day_of_expense_combo_box)

        for i in range(1, 32):
            self.day_of_expense_combo_box.addItem(f"{i}")

        for month in self.months.keys():
            self.month_of_expense_combo_box.addItem(month)

        for i in range(1930, 2051):
            self.year_of_expense_combo_box.addItem(f"{i}")

        self.year_of_expense_combo_box.activated[int].connect(self.set_year_expense_line)
        self.month_of_expense_combo_box.activated[int].connect(self.set_month_expense_line)
        self.day_of_expense_combo_box.activated[int].connect(self.set_day_expense_line)
        
        self.leftLayout.addWidget(self.source_of_expense_label)
        self.leftLayout.addWidget(self.source_of_expense_line)
        self.leftLayout.addWidget(self.desc_of_expense_label)
        self.leftLayout.addWidget(self.description_expense_line)
        self.leftLayout.addWidget(self.type_of_expense_label)
        self.leftLayout.addWidget(self.type_of_expense_line)
        self.leftLayout.addWidget(self.type_of_expense_combo_box)
        self.leftLayout.addWidget(self.btn_sub_expense)
        
        self.close_exp_file_label = Validation.QLabel()
        self.close_exp_file_label.setText("please close the exp_file first!")
        self.close_exp_file_label.setVisible(False)
        self.close_exp_file_label.setStyleSheet('color: red')

        self.type_of_expense_combo_box.addItems(self.default_type_combo)
        self.type_of_expense_line.textChanged.connect(self.update_combo_box_expense)
        self.type_of_expense_combo_box.activated[int].connect(self.set_expense_line)
        
        self.btn_sub_expense.clicked.connect(self.take_exp)             
        
    def set_exp_attr(self):
        self.exp_amount = self.amount_of_expense_line.text()
        self.exp_day = self.day_of_expense_line.text()
        self.exp_month = self.month_of_expense_line.text()
        self.exp_year = self.year_of_expense_line.text()
        self.exp_source = self.source_of_expense_line.text()
        self.exp_desc = self.description_expense_line.text()
        self.exp_type = self.type_of_expense_line.text()     
        
    def take_exp(self):
        exp_amount = self.amount_of_expense_line.text()
        exp_day = self.day_of_expense_line.text()
        exp_month = self.month_of_expense_line.text()
        exp_year = self.year_of_expense_line.text()
        exp_source = self.source_of_expense_line.text()
        exp_desc = self.description_expense_line.text()
        exp_type = self.type_of_expense_line.text()
         
        exp_amount_val = self.digit_val(exp_amount)
        exp_day_val = self.day_val(exp_day, exp_month)
        exp_month_val = self.mounth_val(exp_month)
        exp_year_val = self.revexp_year_val(exp_year)
        if exp_source != "" :
            exp_source_val = True
        else :
            exp_source_val = False
        if len(exp_desc) <= 100 :        
            exp_desc_val = True
        else :
            exp_desc_val = False 
        if exp_type != "" :    
            exp_type_val = True
        else :
             exp_type_val = False
         
        exp_val_list = [exp_amount_val, exp_day_val, exp_month_val, 
                        exp_year_val, exp_source_val, exp_desc_val, exp_type_val]
         
        if False in exp_val_list :
            if not exp_val_list[0] :
                if not self.amount_of_expense_label.isVisible() :
                    self.amount_of_expense_label.setVisible(True)
            else :
                if self.amount_of_expense_label.isVisible() :
                    self.amount_of_expense_label.setVisible(False)       
            if not exp_val_list[1] :
                if not self.day_of_expense_label.isVisible() :
                    self.day_of_expense_label.setVisible(True)
            else :
                if self.day_of_expense_label.isVisible() :
                    self.day_of_expense_label.setVisible(False) 
            if not exp_val_list[2] :
                if not self.month_of_expense_label.isVisible() :
                    self.month_of_expense_label.setVisible(True)
            else :
                if self.month_of_expense_label.isVisible() :
                    self.month_of_expense_label.setVisible(False) 
            if not exp_val_list[3] :
                if not self.year_of_expense_label.isVisible() :
                    self.year_of_expense_label.setVisible(True)
            else :
                if self.year_of_expense_label.isVisible() :
                    self.year_of_expense_label.setVisible(False) 
            if not exp_val_list[4] :
                if not self.source_of_expense_label.isVisible() :
                    self.source_of_expense_label.setVisible(True)
            else :
                if self.source_of_expense_label.isVisible() :
                    self.source_of_expense_label.setVisible(False) 
            if not exp_val_list[5] :
                if not self.desc_of_expense_label.isVisible() :
                    self.desc_of_expense_label.setVisible(True)
            else :
                if self.desc_of_expense_label.isVisible() :
                    self.desc_of_expense_label.setVisible(False) 
            if not exp_val_list[6] :
                if not self.type_of_expense_label.isVisible() :
                    self.type_of_expense_label.setVisible(True)
            else :
                if self.type_of_expense_label.isVisible() :
                    self.type_of_expense_label.setVisible(False) 
        else :
            if self.amount_of_expense_label.isVisible() :
                    self.amount_of_expense_label.setVisible(False)
            if self.day_of_expense_label.isVisible() :
                    self.day_of_expense_label.setVisible(False) 
            if self.month_of_expense_label.isVisible() :
                    self.month_of_expense_label.setVisible(False)                 
            if self.year_of_expense_label.isVisible() :
                    self.year_of_expense_label.setVisible(False)   
            if self.source_of_expense_label.isVisible() :
                    self.source_of_expense_label.setVisible(False) 
            if self.desc_of_expense_label.isVisible() :
                    self.desc_of_expense_label.setVisible(False)   
            if self.type_of_expense_label.isVisible() :
                    self.type_of_expense_label.setVisible(False)                           
            self.set_exp_attr()
            self.create_user_expense_database()  
            
    def category(self):
        if self.current_layout == 'category':
            return
        self.current_layout = 'category'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)
        self.clear_layout(self.hlayout8)

        self.add_category_line = Validation.QLineEdit()
        self.add_category_line.setPlaceholderText("Category")
        self.add_category_line.setStyleSheet(self.line_main_style)
        self.add_btn = Validation.QPushButton("Add")
        self.add_btn.setStyleSheet(self.btn_main_style)
        self.category_label = Validation.QLabel("The category added before")
        self.category_label.setStyleSheet("color : red")
        self.category_label_err = Validation.QLabel("please close the file and try again")
        self.category_label_err.setStyleSheet("color : red")

        self.leftLayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.add_category_line)
        self.hlayout.addWidget(self.add_btn)
        self.leftLayout.addWidget(self.category_label)
        self.leftLayout.addWidget(self.category_label_err)
        self.category_label.hide()
        self.category_label_err.hide()

        self.add_btn.clicked.connect(self.add_text_to_db)       
            
    def search(self):
        if self.current_layout == 'search':
            return
        self.current_layout = 'search'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)
        self.clear_layout(self.hlayout8)

        self.leftLayout.addLayout(self.hlayout)
        self.search_line = Validation.QLineEdit()
        self.search_line.setStyleSheet(self.line_main_style)
        self.search_line.setPlaceholderText("Search")
        self.btn_searching = Validation.QPushButton("Searching")
        self.btn_searching.setStyleSheet(self.btn_main_style)
        self.day_revenue_check = Validation.QCheckBox("day_revenue")
        self.day_revenue_check.setStyleSheet(self.check_box_style)
        self.day_expense_check = Validation.QCheckBox("day_expense")
        self.day_expense_check.setStyleSheet(self.check_box_style)
        self.month_revenue_check = Validation.QCheckBox("month_revenue")
        self.month_revenue_check.setStyleSheet(self.check_box_style)
        self.month_expense_check = Validation.QCheckBox("month_expense")
        self.month_expense_check.setStyleSheet(self.check_box_style)
        self.year_revenue_check = Validation.QCheckBox("year_revenue")
        self.year_revenue_check.setStyleSheet(self.check_box_style)
        self.year_expense_check = Validation.QCheckBox("year_expense")
        self.year_expense_check.setStyleSheet(self.check_box_style)
        self.value_0_100_dollar_check = Validation.QCheckBox("0 - 100 $")
        self.value_0_100_dollar_check.setStyleSheet(self.check_box_style)
        self.value_100_1000_dollar_check = Validation.QCheckBox("100 - 1000 $")
        self.value_100_1000_dollar_check.setStyleSheet(self.check_box_style)
        self.value_more_than_1000_dollar_check = Validation.QCheckBox("More Than 1000 $")
        self.value_more_than_1000_dollar_check.setStyleSheet(self.check_box_style)
        self.wage_check = Validation.QCheckBox("Wage")
        self.wage_check.setStyleSheet(self.check_box_style)
        self.type_revenue_check = Validation.QCheckBox("Type Revenue")
        self.type_revenue_check.setStyleSheet(self.check_box_style)
        self.type_expense_check = Validation.QCheckBox("Type Expensee")
        self.type_expense_check.setStyleSheet(self.check_box_style)
        self.source_revenue_check = Validation.QCheckBox("Source Revenue")
        self.source_revenue_check.setStyleSheet(self.check_box_style)
        self.source_expense_check = Validation.QCheckBox("Source Expense")
        self.source_expense_check.setStyleSheet(self.check_box_style)
        self.revenue_desc_check = Validation.QCheckBox("revenue_description")
        self.revenue_desc_check.setStyleSheet(self.check_box_style)
        self.expense_desc_check = Validation.QCheckBox("expense_description")
        self.expense_desc_check.setStyleSheet(self.check_box_style)
        self.revenue_check = Validation.QCheckBox("revenue")
        self.revenue_check.setStyleSheet(self.check_box_style)
        self.expense_check = Validation.QCheckBox("expense")
        self.expense_check.setStyleSheet(self.check_box_style)
        
        self.hlayout.addWidget(self.search_line)
        self.hlayout.addWidget(self.btn_searching)
        self.leftLayout.addLayout(self.hlayout2)
        self.hlayout2.addWidget(self.day_revenue_check)
        self.hlayout2.addWidget(self.month_revenue_check)
        self.hlayout2.addWidget(self.year_revenue_check)
        self.hlayout2.addWidget(self.value_0_100_dollar_check)
        self.hlayout2.addWidget(self.value_100_1000_dollar_check)
        self.hlayout2.addWidget(self.value_more_than_1000_dollar_check)
        self.leftLayout.addLayout(self.hlayout3)
        self.hlayout3.addWidget(self.day_expense_check)
        self.hlayout3.addWidget(self.month_expense_check)
        self.hlayout3.addWidget(self.year_expense_check)
        self.hlayout3.addWidget(self.type_expense_check)
        self.hlayout3.addWidget(self.source_expense_check)
        self.leftLayout.addLayout(self.hlayout4)
        self.hlayout4.addWidget(self.type_revenue_check)
        self.hlayout4.addWidget(self.source_revenue_check)
        self.hlayout4.addWidget(self.revenue_check)
        self.hlayout4.addWidget(self.revenue_desc_check)
        self.hlayout4.addWidget(self.expense_check )
        self.hlayout4.addWidget(self.expense_desc_check)
        self.search_view = Validation.QTextBrowser()
        self.leftLayout.addWidget(self.search_view)
        self.search_view.setStyleSheet(self.view_style)
        self.btn_searching.clicked.connect(self.search_logic)
        
    def find_month(self, month_num):
        itr = 1
        for key, value in self.months.items():
            if itr == month_num:
                return key.lower()
            else:
                itr += 1
        return None        
        
    def search_logic(self):
        self.searched_word = self.search_line.text()
        if self.searched_word != "" or self.searched_word == "":
            rev_flag = False
            if self.revenue_check.isChecked():
                rev_flag = True
            exp_flag = False
            if self.expense_check.isChecked():
                exp_flag = True   
            rev_desc = False
            if self.revenue_desc_check.isChecked():
                rev_desc = True
            exp_desc = False
            if self.expense_desc_check.isChecked():
                exp_desc = True         
            rev_day_flag = False
            if self.day_revenue_check.isChecked():
                rev_day_flag = True
            exp_day_flag = False
            if self.day_expense_check.isChecked():
                exp_day_flag = True
            rev_month_flag = False
            if self.month_revenue_check.isChecked():
                rev_month_flag = True
            exp_month_flag = False
            if self.month_expense_check.isChecked():
                exp_month_flag = True
            rev_year_flag = False
            if self.year_revenue_check.isChecked():
                rev_year_flag = True
            exp_year_flag = False
            if self.year_expense_check.isChecked():
                exp_year_flag = True
            rev_type_flag = False
            if self.type_revenue_check.isChecked():
                rev_type_flag = True 
            exp_type_flag = False
            if self.type_expense_check.isChecked():
                exp_type_flag = True 
            rev_source_flag = False
            if self.source_revenue_check.isChecked():
                rev_source_flag = True 
            exp_source_flag = False
            if self.source_expense_check.isChecked():
                exp_source_flag = True              
            zero_hund_flag = False
            if self.value_0_100_dollar_check.isChecked():
                zero_hund_flag = True
            hund_touse_flag = False
            if self.value_100_1000_dollar_check.isChecked():
                hund_touse_flag = True
            more_flag = False 
            if self.value_more_than_1000_dollar_check.isChecked():
                more_flag = True
            
            now = Validation.datetime.now()
            Day = now.day
            Month = self.find_month(now.month)
            Year = now.year
            final_resault = "search resaults:\n"    
            if rev_flag:
                try:  
                    filter_list = []  
                    rev_db_path = os.path.join(self.curr_dir, self.revenue_file)
                    conn1 = sql.connect(rev_db_path)
                    cursor1 = conn1.cursor()
                    query = '''SELECT SUM(amount) as total_rev,
                                    GROUP_CONCAT(DISTINCT source) as sources,
                                    GROUP_CONCAT(DISTINCT type) as types
                               FROM REVENUE WHERE 1 = 1'''
                    if rev_desc:
                        query += " AND description LIKE '%' || ? || '%'"
                        filter_list.append(self.searched_word)
                    if rev_type_flag:
                        query += " AND type LIKE '%' || ? || '%'"
                        filter_list.append(self.searched_word)
                    if rev_source_flag:
                        query += " AND type LIKE '%' || ? || '%'"
                        filter_list.append(self.searched_word)      
                    if rev_day_flag:
                        query += " AND day = ?"
                        filter_list.append(Day)
                    if rev_month_flag:
                        query += " AND month = ?"
                        filter_list.append(Month)
                    if rev_year_flag:
                        query += " AND year = ?" 
                        filter_list.append(Year)  
                    if zero_hund_flag:
                        query += " AND amount BETWEEN 0 AND 100"
                    if hund_touse_flag:
                        query += " AND amount BETWEEN 100 AND 1000"
                    if more_flag:
                        query += " AND amount > 1000"  
                        
                    cursor1.execute(query, tuple(filter_list))
                    conn1.commit()
                    resaults = cursor1.fetchone()
                    total_rev = resaults[0]
                    sources = resaults[1]
                    types = resaults[2]
                    if total_rev is None:
                        total_rev = 0
                    final_resault += f"Revenue:\nTotal Filtered Revenue : {total_rev}\nSources: {sources}\nTypes: {types}\n"  
                
                    cursor1.close()
                    conn1.close()             
                except:
                    pass     
            if exp_flag:  
                try:
                    filter_list = [] 
                    exp_db_path = os.path.join(self.curr_dir, self.expense_file)
                    conn2 = sql.connect(exp_db_path)
                    cursor2 = conn2.cursor()
                    query = '''SELECT SUM(amount) as total_exp,
                                    GROUP_CONCAT(DISTINCT source) as sources,
                                    GROUP_CONCAT(DISTINCT type) as types
                               FROM EXPENSE WHERE 1 = 1'''
                    if exp_desc:
                        query += " AND description LIKE '%' || ? || '%'"
                        filter_list.append(self.searched_word)
                    if exp_type_flag:
                        query += " AND type LIKE '%' || ? || '%'"
                        filter_list.append(self.searched_word)
                    if exp_source_flag:
                        query += " AND type LIKE '%' || ? || '%'"
                        filter_list.append(self.searched_word)     
                    if exp_day_flag:
                        query += " AND day = ?"
                        filter_list.append(Day)
                    if exp_month_flag:
                        query += " AND month = ?"
                        filter_list.append(Month)
                    if exp_year_flag:
                        query += " AND year = ?" 
                        filter_list.append(Year)   
                    if zero_hund_flag:
                        query += " AND amount BETWEEN 0 AND 100"   
                    if hund_touse_flag:
                        query += " AND amount BETWEEN 100 AND 1000"
                    if more_flag:
                        query += " AND amount > 1000"  
                        
                    cursor2.execute(query, tuple(filter_list))
                    conn2.commit()
                    resaults = cursor2.fetchone()
                    total_exp = resaults[0]
                    sources = resaults[1]
                    types = resaults[2]
                    if total_exp is None:
                        total_exp = 0
                    final_resault += f"Expense:\nTotal Filtered Expense : {total_exp}\nSources: {sources}\nTypes: {types}"  
                    
                    cursor2.close()
                    conn2.close()  
                except:
                    pass
            self.search_view.setPlainText(final_resault)              
        
    def report(self):
        if self.current_layout == 'report':
            return
        self.current_layout = 'report'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)
        self.clear_layout(self.hlayout8)

        self.year_of_report_combo_box = Validation.QComboBox()
        self.year_of_report_combo_box.setStyleSheet(self.combo_main_style)
        self.month_of_report_combo_box = Validation.QComboBox()
        self.month_of_report_combo_box.setStyleSheet(self.combo_main_style)
        self.day_of_report_combo_box = Validation.QComboBox()
        self.day_of_report_combo_box.setStyleSheet(self.combo_main_style)

        self.year_of_report_combo_box2 = Validation.QComboBox()
        self.year_of_report_combo_box2.setStyleSheet(self.combo_main_style)
        self.month_of_report_combo_box2 = Validation.QComboBox()
        self.month_of_report_combo_box2.setStyleSheet(self.combo_main_style)
        self.day_of_report_combo_box2 = Validation.QComboBox()
        self.day_of_report_combo_box2.setStyleSheet(self.combo_main_style)

        for i in range(1, 32):
            self.day_of_report_combo_box.addItem(f"{i}")

        for month in self.months.keys():
            self.month_of_report_combo_box.addItem(month)

        for i in range(1930, 2051):
            self.year_of_report_combo_box.addItem(f"{i}")

        for i in range(1, 32):
            self.day_of_report_combo_box2.addItem(f"{i}")

        for month in self.months.keys():
            self.month_of_report_combo_box2.addItem(month)

        for i in range(1930, 2051):
            self.year_of_report_combo_box2.addItem(f"{i}")

        self.year_of_report_combo_box.activated[int].connect(self.set_year_report_line)
        self.month_of_report_combo_box.activated[int].connect(self.set_month_report_line)
        self.day_of_report_combo_box.activated[int].connect(self.set_day_report_line)

        self.year_of_report_combo_box2.activated[int].connect(self.set_year_report_line2)
        self.month_of_report_combo_box2.activated[int].connect(self.set_month_report_line2)
        self.day_of_report_combo_box2.activated[int].connect(self.set_day_report_line2)

        self.from_report_line = Validation.QLineEdit()
        self.from_report_line.setText("From")
        self.from_report_line.setStyleSheet("""
        QLineEdit {
           background-color: #AD4379; 
           color: #0A0A0A;               
           border: 3px solid #34568B;    
           border-radius: 10px;        
           padding: 4px;
        }
        QLineEdit:hover {
            background-color: #0081AB; 
        }
        """)
        self.from_report_line.setReadOnly(True)
        self.day_of_report_line = Validation.QLineEdit()
        self.day_of_report_line.setPlaceholderText("Day")
        self.day_of_report_line.setStyleSheet(self.line_main_style)
        self.month_of_report_line = Validation.QLineEdit()
        self.month_of_report_line.setPlaceholderText("Month")
        self.month_of_report_line.setStyleSheet(self.line_main_style)
        self.year_of_report_line = Validation.QLineEdit()
        self.year_of_report_line.setPlaceholderText("Year")
        self.year_of_report_line.setStyleSheet(self.line_main_style)

        self.until_report_line = Validation.QLineEdit()
        self.until_report_line.setText("Until")
        self.until_report_line.setStyleSheet("""
        QLineEdit {
           background-color: #AD4379; 
           color: #0A0A0A;               
           border: 3px solid #34568B;    
           border-radius: 10px;        
           padding: 4px;
        }
        QLineEdit:hover {
            background-color: #0081AB; 
        }
        """)
        self.until_report_line.setReadOnly(True)
        self.day_of_report_line2 = Validation.QLineEdit()
        self.day_of_report_line2.setPlaceholderText("Day")
        self.day_of_report_line2.setStyleSheet(self.line_main_style)
        self.month_of_report_line2 = Validation.QLineEdit()
        self.month_of_report_line2.setPlaceholderText("Month")
        self.month_of_report_line2.setStyleSheet(self.line_main_style)
        self.year_of_report_line2 = Validation.QLineEdit()
        self.year_of_report_line2.setPlaceholderText("Year")
        self.year_of_report_line2.setStyleSheet(self.line_main_style)

        self.day_report_check = Validation.QCheckBox("day_report")
        self.day_report_check.setStyleSheet(self.check_box_style)
        self.month_report_check = Validation.QCheckBox("month_report")
        self.month_report_check.setStyleSheet(self.check_box_style)
        self.year_report_check = Validation.QCheckBox("year_report")
        self.year_report_check.setStyleSheet(self.check_box_style)
        self.report_0_100_dollar_check = Validation.QCheckBox("0 - 100 $")
        self.report_0_100_dollar_check.setStyleSheet(self.check_box_style)
        self.report_100_1000_dollar_check = Validation.QCheckBox("100 - 1000 $")
        self.report_100_1000_dollar_check.setStyleSheet(self.check_box_style)
        self.report_more_than_1000_dollar_check = Validation.QCheckBox("More Than 1000 $")
        self.report_more_than_1000_dollar_check.setStyleSheet(self.check_box_style)
        self.cash_check = Validation.QCheckBox("Cash")
        self.cash_check.setStyleSheet(self.check_box_style)
        self.cheque_check = Validation.QCheckBox("Cheque")
        self.cheque_check.setStyleSheet(self.check_box_style)
        self.digital_check = Validation.QCheckBox("digital_currency")
        self.digital_check.setStyleSheet(self.check_box_style)
        self.saving_check = Validation.QCheckBox("Saving")
        self.saving_check.setStyleSheet(self.check_box_style)
        self.wage_check = Validation.QCheckBox("wage")
        self.wage_check.setStyleSheet(self.check_box_style)
        self.report_revenue_check = Validation.QCheckBox("Revenue")
        self.report_revenue_check.setStyleSheet(self.check_box_style)
        self.report_expense_check = Validation.QCheckBox("Expense")
        self.report_expense_check.setStyleSheet(self.check_box_style)
        self.btn_report = Validation.QPushButton("Report")
        self.btn_report.setStyleSheet(self.btn_main_style)
    
        self.leftLayout.addWidget(self.from_report_line)

        self.leftLayout.addLayout(self.hlayout4)
        
        self.hlayout4.addWidget(self.day_of_report_line)
        self.hlayout4.addWidget(self.month_of_report_line)
        self.hlayout4.addWidget(self.year_of_report_line)
        self.leftLayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.day_of_report_combo_box)
        self.hlayout.addWidget(self.month_of_report_combo_box)
        self.hlayout.addWidget(self.year_of_report_combo_box)

        self.leftLayout.addWidget(self.until_report_line)
        self.leftLayout.addLayout(self.hlayout5)
        self.hlayout5.addWidget(self.day_of_report_line2)
        self.hlayout5.addWidget(self.month_of_report_line2)
        self.hlayout5.addWidget(self.year_of_report_line2)
        self.leftLayout.addLayout(self.hlayout6)
        self.hlayout6.addWidget(self.day_of_report_combo_box2)
        self.hlayout6.addWidget(self.month_of_report_combo_box2)
        self.hlayout6.addWidget(self.year_of_report_combo_box2)

        self.leftLayout.addLayout(self.hlayout2)
        self.hlayout2.addWidget(self.day_report_check)
        self.hlayout2.addWidget(self.month_report_check)
        self.hlayout2.addWidget(self.year_report_check)
        self.hlayout2.addWidget(self.report_0_100_dollar_check)
        self.hlayout2.addWidget(self.report_100_1000_dollar_check)
        self.hlayout2.addWidget(self.report_more_than_1000_dollar_check)
        self.leftLayout.addLayout(self.hlayout3)
        self.hlayout3.addWidget(self.cash_check)
        self.hlayout3.addWidget(self.cheque_check)
        self.hlayout3.addWidget(self.digital_check)
        self.hlayout3.addWidget(self.wage_check)
        self.hlayout3.addWidget(self.saving_check)
        self.hlayout3.addWidget(self.report_revenue_check)
        self.hlayout3.addWidget(self.report_expense_check)
        self.leftLayout.addWidget(self.btn_report)
        self.report_view = Validation.QTextBrowser()
        self.leftLayout.addWidget(self.report_view)
        self.report_view.setStyleSheet(self.view_style)
        
        self.btn_report.clicked.connect(self.report_logic) 
        
    def month_index(self, month):
        Months = list(self.valid_mounths.keys())
        return Months.index(month.lower()) + 1   
    
    def report_logic(self):
        rep_from_day =  self.day_of_report_line.text() 
        rep_from_month =  self.month_of_report_line.text()  
        rep_from_year =  self.year_of_report_line.text()
        rep_until_day =  self.day_of_report_line2.text()
        rep_until_month =  self.month_of_report_line2.text()
        rep_until_year =  self.year_of_report_line2.text()
        
        rep_from_day_val1 = (rep_from_day != "")  
        rep_from_month_val1 = (rep_from_month != "")
        rep_from_year_val1 = (rep_from_year != "")
        rep_until_day_val1 = (rep_until_day != "") 
        rep_until_month_val1 = (rep_until_month != "") 
        rep_until_year_val1 =  (rep_until_year != "")
        
        rep_from_day_val2 = self.day_val(rep_from_day, rep_from_month)  
        rep_from_month_val2 = self.mounth_val(rep_from_month) 
        rep_from_year_val2 = self.revexp_year_val(rep_from_year) 
        rep_until_day_val2 = self.day_val(rep_until_day, rep_until_month) 
        rep_until_month_val2 = self.mounth_val(rep_until_month) 
        rep_until_year_val2 =  self.revexp_year_val(rep_until_year)
        
        rep_val_list = [rep_from_day_val1, rep_from_month_val1, rep_from_year_val1, 
                        rep_until_day_val1, rep_until_month_val1, rep_until_year_val1, 
                        rep_from_day_val2, rep_from_month_val2, rep_from_year_val2, 
                        rep_until_day_val2, rep_until_month_val2, rep_until_year_val2]
        
        current_date = Validation.datetime.now()
        curr_day = current_date.day
        curr_month = self.find_month(current_date.month)
        curr_year = current_date.year
            
        Months = list(self.valid_mounths.keys())
        
        rev_flag = False
        if self.report_revenue_check.isChecked():
            rev_flag = True
        exp_flag = False
        if self.report_expense_check.isChecked():
            exp_flag = True    
        day_report_flag = False
        if self.day_report_check.isChecked():
            day_report_flag = True    
        month_report_flag = False
        if self.month_report_check.isChecked():
            month_report_flag = True
        year_report_flag = False
        if self.year_report_check.isChecked() :
            year_report_flag = True
        zero_hund_flag = False
        if self.report_0_100_dollar_check.isChecked():
            zero_hund_flag = True
        hund_thous_flag = False
        if self.report_100_1000_dollar_check.isChecked():
            hund_thous_flag = True
        more_flag = False
        if self.report_more_than_1000_dollar_check.isChecked():
            more_flag = True
        saving_flag = False
        if self.saving_check.isChecked():
            saving_flag = True
        cash_flag = False
        if self.cash_check.isChecked():
            cash_flag = True
        wage_flag = False
        if self.wage_check.isChecked():
            wage_flag = True 
        cheque_flag = False
        if self.cheque_check.isChecked():
            cheque_flag = True    
        digital_flag = False
        if self.digital_check.isChecked():
            digital_flag = True  
            
        #fig , (ax1, ax2) = plt.subplots(1, 2, figsize = (5, 5))      
            
        final_ans = f"Report :\n" 
        if rev_flag:   
            filters = []
            filter_selected = False
            db_path = os.path.join(self.curr_dir, self.revenue_file)
            conn1 = sql.connect(db_path)
            cursor1 = conn1.cursor()
            query = '''SELECT SUM(amount) FROM REVENUE WHERE 1 = 1'''
            
            cursor1.execute(query)
            total_rev = cursor1.fetchone()[0]
            
            try:   
                query += " AND (1 = 1"     
                if False not in rep_val_list:
                    rep_from_day = int(rep_from_day)
                    rep_until_day = int(rep_until_day)
                    rep_from_month = self.month_index(rep_from_month)
                    rep_until_month = self.month_index(rep_until_month) 
                    rep_from_year = int(rep_from_year)
                    rep_until_year = int(rep_until_year)
                    min_day, max_day = min(rep_from_day, rep_until_day), max(rep_from_day, rep_until_day) 
                    min_month, max_month = min(rep_from_month, rep_until_month), max(rep_from_month, rep_until_month) 
                    min_year, max_year = min(rep_from_year, rep_until_year), max(rep_from_year, rep_until_year) 
                    conn1.create_function('MONTH_INDEX', 1, self.month_index)
                    query += " AND day BETWEEN ? AND ?"
                    filters.append(min_day)
                    filters.append(max_day)
                    query += " AND MONTH_INDEX(month) BETWEEN ? AND ?"
                    filters.append(min_month)
                    filters.append(max_month)
                    query += " AND year BETWEEN ? AND ?"
                    filters.append(min_year)
                    filters.append(max_year)
            
                if False not in rep_val_list:  
                    filter_selected = True      
                    query += ") AND (1 = 0"
                else:      
                    query += " OR 1 = 1) AND (1 = 0"
                if day_report_flag and False in rep_val_list: 
                    filter_selected = True
                    query += " OR day = ?"
                    filters.append(curr_day)
                    
                if month_report_flag and False in rep_val_list:
                    filter_selected = True
                    query += " OR month = ?"
                    filters.append(curr_month)      
                    
                if year_report_flag and False in rep_val_list:
                    filter_selected = True
                    query += " OR year = ?"
                    filters.append(curr_year)
                
                if True in [day_report_flag, month_report_flag, year_report_flag]:       
                    query += ") AND (1 = 0" 
                else:
                    query += " OR 1 = 1) AND (1 = 0"
                
                if zero_hund_flag:
                    query += " OR amount BETWEEN 0 AND 100"
               
                if hund_thous_flag:
                    query += " OR amount BETWEEN 100 AND 1000"
                    
                if more_flag:
                    query += " OR amount > 1000"
                
                if True in [zero_hund_flag, hund_thous_flag, more_flag]:
                    filter_selected = True        
                    query += ") AND (1 = 0" 
                else:
                    query += " OR 1 = 1) AND (1 = 0"     
               
                if saving_flag:
                    query += " OR source = 'saving'"
                    
                if wage_flag:
                    query += " OR source = 'wage'" 
                    
                if True in [saving_flag, wage_flag]:      
                    filter_selected = True  
                    query += ") AND (1 = 0" 
                else:
                    query += " OR 1 = 1) AND (1 = 0"      
                
                if cash_flag:
                    query += " OR type = 'Cash'"  
                    
                if cheque_flag:
                    query += " OR type = 'Cheque'"
                
                if digital_flag:
                    query += " OR type = 'Digital currency'"

                if True in [cash_flag, cheque_flag, digital_flag]:
                    filter_selected = True        
                    query += ")"
                else:
                    query += " OR 1 = 1)"    
            
                total = None
                if filter_selected:    
                    cursor1.execute(query, tuple(filters))
                    total = cursor1.fetchone()[0]    
                    conn1.commit()
                    
                if total is None:
                    total = 0 
                else:   
                    total = total_rev
                    
                final_ans += f"Revenue:\nTotal filtered revenue: {total} / total revenue: {total_rev}  /  ratio: {(total / total_rev) * 100}\n" 
            
                type_query = '''SELECT 
                                    type, SUM(amount)
                                FROM REVENUE
                                GROUP BY type
                                '''
                cursor1.execute(type_query)   
                type_rep = cursor1.fetchall()
                conn1.commit() 
            
                rev_labels = []
                rev_sizes = []
                for row in type_rep:
                    rev_labels.append(row[0])
                    rev_sizes.append(int(row[1]))
                    final_ans += f"Type: {row[0]} / amount of type: {row[1]} / ratio to total: %{(row[1] / total_rev) * 100}\n" 
                    final_ans += f"Ratio to fitered amount(filterd_amount/type_amount): %{(total / row[1]) * 100}\n"
                
                #ax1.pie(rev_sizes, labels = rev_labels, autopct = '%1.1f%%')
                #ax1.set_title('Type')    
                
                source_query =  '''SELECT source, SUM(amount)
                                    FROM REVENUE
                                    GROUP BY source
                                '''
                cursor1.execute(source_query)   
                source_rep = cursor1.fetchall()
                conn1.commit()
            
                rev_source_labels = []
                rev_source_sizes = []
                for row in source_rep:
                    rev_source_labels.append(row[0])
                    rev_source_sizes.append(int(row[1]))
                    final_ans += f"Source : {row[0]} / amount of source : {row[1]} / ratio : %{(row[1] / total_rev) * 100}" 
                    final_ans += f"Ratio to fitered amount(filterd_amount/source_amount): %{(total / row[1]) * 100}\n"  
                
                #ax2.pie(rev_source_sizes, labels = rev_source_labels, autopct = '%1.1f%%')
                #ax2.set_title('Source')           
             
                conn1.close()
            except:
                pass    
            
        if exp_flag:   
            filters = [] 
            filter_selected = False
            db_path = os.path.join(self.curr_dir, self.expense_file)
            conn2 = sql.connect(db_path)
            cursor2 = conn2.cursor()
            query = '''SELECT SUM(amount) FROM EXPENSE WHERE 1 = 1'''
            try:        
                cursor2.execute(query)
                total_exp = cursor2.fetchone()[0]
               
                query += " AND (1 = 1"     
                if False not in rep_val_list:
                    rep_from_day = int(rep_from_day)
                    rep_until_day = int(rep_until_day)
                    rep_from_month = self.month_index(rep_from_month)
                    rep_until_month = self.month_index(rep_until_month) 
                    rep_from_year = int(rep_from_year)
                    rep_until_year = int(rep_until_year)
                    min_day, max_day = min(rep_from_day, rep_until_day), max(rep_from_day, rep_until_day) 
                    min_month, max_month = min(rep_from_month, rep_until_month), max(rep_from_month, rep_until_month) 
                    min_year, max_year = min(rep_from_year, rep_until_year), max(rep_from_year, rep_until_year) 
                    conn2.create_function('MONTH_INDEX', 1, self.month_index)
                    query += " AND day BETWEEN ? AND ?"
                    filters.append(min_day)
                    filters.append(max_day)
                    query += " AND MONTH_INDEX(month) BETWEEN ? AND ?"
                    filters.append(min_month)
                    filters.append(max_month)
                    query += " AND year BETWEEN ? AND ?"
                    filters.append(min_year)
                    filters.append(max_year)
            
                if False not in rep_val_list:  
                    filter_selected = True      
                    query += ") AND (1 = 0"
                else:      
                    query += " OR 1 = 1) AND (1 = 0"
                if day_report_flag and False in rep_val_list: 
                    filter_selected = True
                    query += " OR day = ?"
                    filters.append(curr_day)
                    
                if month_report_flag and False in rep_val_list:
                    filter_selected = True
                    query += " OR month = ?"
                    filters.append(curr_month)       
            
                if year_report_flag and False in rep_val_list:
                    filter_selected = True
                    query += " OR year = ?"
                    filters.append(curr_year)
                
                if True in [day_report_flag, month_report_flag, year_report_flag]:       
                    query += ") AND (1 = 0" 
                else:
                    query += " OR 1 = 1) AND (1 = 0"
                
                if zero_hund_flag:
                    query += " OR amount BETWEEN 0 AND 100"
               
                if hund_thous_flag:
                    query += " OR amount BETWEEN 100 AND 1000"
                    
                if more_flag:
                    query += " OR amount > 1000"
                
                if True in [zero_hund_flag, hund_thous_flag, more_flag]:
                    ilter_selected = True        
                    query += ") AND (1 = 0" 
                else:
                    query += " OR 1 = 1) AND (1 = 0"     
               
                if saving_flag:
                    query += " OR source = 'saving'"
                    
                if wage_flag:
                    query += " OR source = 'wage'" 
                    
                if True in [saving_flag, wage_flag]:      
                    filter_selected = True  
                    query += ") AND (1 = 0" 
                else:
                    query += " OR 1 = 1) AND (1 = 0"      
                
                if cash_flag:
                    query += " OR type = 'Cash'"  
                    
                if cheque_flag:
                    query += " OR type = 'Cheque'"
                
                if digital_flag:
                    query += " OR type = 'Digital currency'"
            
                if True in [cash_flag, cheque_flag, digital_flag]:
                    filter_selected = True        
                    query += ")"
                else:
                    query += " OR 1 = 1)"    
            
                total = None
                if filter_selected:    
                    cursor2.execute(query, tuple(filters))
                    total = cursor2.fetchone()[0]    
                    conn2.commit()
                    
                if total is None:
                    total = 0 
                else:   
                    total = total_exp
                    
                final_ans += f"Expense:\nTotal filtered expense: {total} / total expense : {total_exp} / ratio: %{(total / total_exp) * 100}\n"
            
                type_query = '''SELECT type, SUM(amount)
                                FROM EXPENSE
                                GROUP BY type
                                '''
                cursor2.execute(type_query)   
                type_rep = cursor2.fetchall()
                conn2.commit() 
            
                exp_type_labels = []
                exp_type_sizes = []
                for row in type_rep:
                    exp_type_labels.append(row[0])
                    exp_type_sizes.append(row[1])
                    final_ans += f"Type : {row[0]} / amount of type : {row[1]} / ratio : %{(row[1] / total_exp) * 100}" 
                    final_ans += f"Ratio to fitered amount(filterd_amount/type_amount): %{(total / row[1]) * 100}\n"  
                
                source_query = '''SELECT source, SUM(amount)
                                  FROM EXPENSE
                                  GROUP BY source
                                '''
                cursor2.execute(source_query)   
                source_rep = cursor2.fetchall()
                conn2.commit() 
            
                exp_source_labels = []
                exp_source_sizes = []
                for row in source_rep:
                    exp_source_labels.append(row[0])
                    exp_source_sizes.append(row[1])
                    final_ans += f"Source : {row[0]} / amount of source : {row[1]} / ratio : %{(row[1] / total_exp) * 100}" 
                    final_ans += f"Ratio to fitered amount(filterd_amount/source_amount): %{(total / row[1]) * 100}\n"            
            
                conn2.close()
            except:
                pass
        self.report_view.setPlainText(final_ans) 
           
        #canvas = FigureCanvas(fig)
        #self.leftLayout.addWidget(canvas)
        
    def settings(self):
        if self.current_layout == 'settings':
            return
        self.current_layout = 'settings'
        self.clear_layout(self.leftLayout)
        self.clear_layout(self.hlayout)
        self.clear_layout(self.hlayout2)
        self.clear_layout(self.hlayout3)
        self.clear_layout(self.hlayout4)
        self.clear_layout(self.hlayout5)
        self.clear_layout(self.hlayout6)
        self.clear_layout(self.hlayout7)
        self.clear_layout(self.hlayout8)

        self.first_name_line_edit2 = Validation.QLineEdit()
        self.first_name_line_edit2.setPlaceholderText("firs name")
        self.first_name_line_edit2.setStyleSheet(self.line_main_style)
        self.last_name_line_edit2 = Validation.QLineEdit()
        self.last_name_line_edit2.setPlaceholderText('last name')
        self.last_name_line_edit2.setStyleSheet(self.line_main_style)
        self.password_line_edit2 = Validation.QLineEdit()
        self.password_line_edit2.setPlaceholderText('password')
        self.password_line_edit2.setStyleSheet(self.line_main_style)
        self.password_line_edit2.setEchoMode(Validation.QLineEdit.EchoMode.Password)
        self.repeat_password_line_edit2 = Validation.QLineEdit()
        self.repeat_password_line_edit2.setPlaceholderText('repeat password')
        self.repeat_password_line_edit2.setStyleSheet(self.line_main_style)
        self.repeat_password_line_edit2.setEchoMode(Validation.QLineEdit.EchoMode.Password)
        self.email_line_edit2 = Validation.QLineEdit()
        self.email_line_edit2.setPlaceholderText('email')
        self.email_line_edit2.setStyleSheet(self.line_main_style)
        self.phone_number_line_edit2 = Validation.QLineEdit()
        self.phone_number_line_edit2.setPlaceholderText('phone')
        self.phone_number_line_edit2.setStyleSheet(self.line_main_style)
        self.city_line_edit2 = Validation.QLineEdit()
        self.city_line_edit2.setPlaceholderText('city')
        self.city_line_edit2.setStyleSheet(self.line_main_style)
        self.day_line_edit2 = Validation.QLineEdit()
        self.day_line_edit2.setStyleSheet(self.line_main_style)
        self.day_line_edit2.setPlaceholderText('day')
        self.mounth_line_edit2 = Validation.QLineEdit()
        self.mounth_line_edit2.setStyleSheet(self.line_main_style)
        self.mounth_line_edit2.setPlaceholderText('month ***please enter letters***')
        self.year_line_edit2 = Validation.QLineEdit()
        self.year_line_edit2.setStyleSheet(self.line_main_style)
        self.year_line_edit2.setPlaceholderText('year')
        
        self.label_image = Validation.QLabel('No image uploaded', self)
        self.label_image.setScaledContents(True)
        self.label_image.setFixedSize(200, 100)
        self.label_image.setStyleSheet("color : blue")
        self.upload_btn = Validation.QPushButton('Upload Image', self)
        self.upload_btn.setStyleSheet(self.btn_main_style)
        self.upload_btn.clicked.connect(self.upload_image)

        self.display_btn = Validation.QPushButton('Display Image', self)
        self.display_btn.setStyleSheet(self.btn_main_style)
        self.display_btn.clicked.connect(self.display_image)

        self.leftLayout.addWidget(self.label_image)
        self.leftLayout.addWidget(self.upload_btn)
        self.leftLayout.addWidget(self.display_btn)

        self.leftLayout.addLayout(self.hlayout5)
        self.err_lab_firstname = Validation.QLabel("NAME ERROR")
        self.err_lab_firstname.setStyleSheet("color : red")
        self.err_lab_firstname.hide()
        self.hlayout5.addWidget(self.err_lab_firstname)
        self.err_lab_lastname = Validation.QLabel("NAME ERROR")
        self.err_lab_lastname.setStyleSheet("color : red")
        self.err_lab_lastname.hide()
        self.hlayout5.addWidget(self.err_lab_lastname)
        self.err_lab_password = Validation.QLabel("PASSWORD ERROR")
        self.err_lab_password.setStyleSheet("color : red")
        self.err_lab_password.hide()
        self.hlayout5.addWidget(self.err_lab_password)

        self.leftLayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.first_name_line_edit2)
        self.hlayout.addWidget(self.last_name_line_edit2)
        self.hlayout.addWidget(self.password_line_edit2)

        self.leftLayout.addLayout(self.hlayout6)
        self.err_lab_repassword = Validation.QLabel("PASSWORD ERROR")
        self.err_lab_repassword.setStyleSheet("color : red")
        self.err_lab_repassword.hide()
        self.hlayout6.addWidget(self.err_lab_repassword)
        self.err_lab_email = Validation.QLabel("EMAIL ERROR")
        self.err_lab_email.setStyleSheet("color : red")
        self.err_lab_email.hide()
        self.hlayout6.addWidget(self.err_lab_email)
        self.err_lab_phone = Validation.QLabel("PHONE ERROR")
        self.err_lab_phone.setStyleSheet("color : red")
        self.err_lab_phone.hide()
        self.hlayout6.addWidget(self.err_lab_phone)
        self.err_lab_city = Validation.QLabel("please fill the gap!")
        self.err_lab_city.setStyleSheet("color : red")
        self.err_lab_city.hide()

        self.leftLayout.addLayout(self.hlayout2)
        self.hlayout2.addWidget(self.repeat_password_line_edit2)
        self.hlayout2.addWidget(self.email_line_edit2)
        self.hlayout2.addWidget(self.phone_number_line_edit2)
        self.leftLayout.addWidget(self.err_lab_city)
        self.leftLayout.addWidget(self.city_line_edit2)

        self.leftLayout.addLayout(self.hlayout7)
        self.err_lab_day = Validation.QLabel("DAY ERROR")
        self.err_lab_day.setStyleSheet("color : red")
        self.err_lab_day.hide()
        self.hlayout7.addWidget(self.err_lab_day)
        self.err_lab_month = Validation.QLabel("NAME ERROR")
        self.err_lab_month.setStyleSheet("color : red")
        self.err_lab_month.hide()
        self.hlayout7.addWidget(self.err_lab_month)
        self.err_lab_year = Validation.QLabel("NAME ERROR")
        self.err_lab_year.setStyleSheet("color : red")
        self.err_lab_year.hide()
        self.hlayout7.addWidget(self.err_lab_year)
        self.leftLayout.addLayout(self.hlayout4)
        self.hlayout4.addWidget(self.day_line_edit2)
        self.hlayout4.addWidget(self.mounth_line_edit2)
        self.hlayout4.addWidget(self.year_line_edit2)

        self.leftLayout.addLayout(self.hlayout3)
        self.year_of_edit_combo_box = Validation.QComboBox()
        self.year_of_edit_combo_box.setStyleSheet(self.combo_main_style)
        self.month_of_edit_combo_box = Validation.QComboBox()
        self.month_of_edit_combo_box.setStyleSheet(self.combo_main_style)
        self.day_of_edit_combo_box = Validation.QComboBox()
        self.day_of_edit_combo_box.setStyleSheet(self.combo_main_style)
        for i in range(1, 32):
            self.day_of_edit_combo_box.addItem(f"{i}")

        for month in self.months.keys():
            self.month_of_edit_combo_box.addItem(month)

        for i in range(1920, 2006):
            self.year_of_edit_combo_box.addItem(f"{i}")

        self.year_of_edit_combo_box.activated[int].connect(self.set_year_edit_line)
        self.month_of_edit_combo_box.activated[int].connect(self.set_month_edit_line)
        self.day_of_edit_combo_box.activated[int].connect(self.set_day_edit_line)

        self.hlayout3.addWidget(self.day_of_edit_combo_box)
        self.hlayout3.addWidget(self.month_of_edit_combo_box)
        self.hlayout3.addWidget(self.year_of_edit_combo_box)

        self.change_info_btn = Validation.QPushButton("Change")
        self.change_info_btn.setStyleSheet(self.btn_main_style)
        self.leftLayout.addWidget(self.change_info_btn)
        
        self.delete_err = Validation.QLabel("please fill the gap!")
        self.delete_err.setVisible(False)
        self.delete_err.setStyleSheet("color: red")
        self.leftLayout.addWidget(self.delete_err)
        self.delete_info_line = Validation.QLineEdit()
        self.delete_info_line.setPlaceholderText("Delete the ...")
        self.delete_info_line.setStyleSheet(self.line_main_style)
        self.delete_info_line.setReadOnly(True)
        self.leftLayout.addWidget(self.delete_info_line)

        self.delete_info_combo = Validation.QComboBox()
        self.delete_info_combo.setStyleSheet(self.combo_main_style)
        self.delete_info_combo.addItems(self.delete_information)
        self.delete_info_combo.activated[int].connect(self.set_delete_line)
        self.leftLayout.addWidget(self.delete_info_combo)

        self.delete_user = Validation.QPushButton("Delete")
        self.delete_user.setStyleSheet(self.btn_main_style)
        self.leftLayout.addWidget(self.delete_user)
        
        self.change_info_btn.clicked.connect(self.change_information)
        self.delete_user.clicked.connect(self.Delete_User)
        
        self.sun_label = Validation.QLabel(self)
        self.moon_label = Validation.QLabel(self)
        self.sun_label.setFixedSize(100, 100)
        self.moon_label.setFixedSize(100, 100)
        self.sun_label.setScaledContents(True)
        self.moon_label.setScaledContents(True)

        self.sun_pixmap = Validation.QPixmap('C:/Users/ASUS/ap_project_2th_part/cloud-sun-.png')  
        self.moon_pixmap = Validation.QPixmap('C:/Users/ASUS/ap_project_2th_part/nite_moon.jpg')  
        self.sun_label.setPixmap(self.sun_pixmap)
        self.moon_label.setPixmap(self.moon_pixmap)

        self.sun_label.mousePressEvent = self.switch_to_light_mode
        self.moon_label.mousePressEvent = self.switch_to_dark_mode

        self.leftLayout.addLayout(self.hlayout8)

        self.hlayout8.addWidget(self.sun_label)
        self.hlayout8.addWidget(self.moon_label)
        
    def upload_image(self):
        img_db_path = os.path.join(self.curr_dir, 'images.db')
        #self.conn = sql.connect(img_db_path)
        #self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS images
                               (id INTEGER PRIMARY KEY, image BLOB)''')
        self.conn.commit()
        file_dialog = Validation.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.xpm *.jpg *.jpeg *.bmp)')

        if file_path:
            with open(file_path, 'rb') as file:
                blob_data = file.read()

            self.cursor.execute('INSERT INTO images (image) VALUES (?)', (blob_data,))
            self.conn.commit()
            self.label_image.setText('Image uploaded successfully!')

    def display_image(self):
        self.cursor.execute('SELECT image FROM images ORDER BY id DESC LIMIT 1')
        image_data = self.cursor.fetchone()

        if image_data:
            pixmap = Validation.QPixmap()
            pixmap.loadFromData(image_data[0])
            self.label_image.setPixmap(pixmap.scaled(200, 200, Validation.Qt.AspectRatioMode.KeepAspectRatio))       
        
    def change_information(self):
        first_name = self.first_name_line_edit2.text()
        last_name = self.last_name_line_edit2.text()
        password = self.password_line_edit2.text()
        re_password = self.repeat_password_line_edit2.text()
        email = self.email_line_edit2.text()
        phone_number = self.phone_number_line_edit2.text()
        city = self.city_line_edit2.text()
        day = self.day_line_edit2.text()
        month = self.mounth_line_edit2.text()
        year = self.year_line_edit2.text() 
        
        first_name_val = self.name_val(first_name)
        last_name_val = self.name_val(last_name)
        password_val = self.password_val(password)
        re_password_val = (self.password_val(re_password) and password == re_password)
        email_val = self.email_val(email)
        phone_number_val = self.phone_number_val(phone_number)
        city_val = (city != "")
        day_val = self.day_val(day, month)
        month_val = self.mounth_val(month)
        year_val = self.year_val(year)
        
        info_val_list = [first_name_val, last_name_val, password_val, re_password_val, 
                         email_val, phone_number_val, city_val, day_val, month_val, year_val]
        
        if False in info_val_list:
            if not info_val_list[0]:
                if not self.err_lab_firstname.isVisible():
                    self.err_lab_firstname.setVisible(True)
            else:
                if self.err_lab_firstname.isVisible():
                    self.err_lab_firstname.setVisible(False)
            if not info_val_list[1]:
                if not self.err_lab_lastname.isVisible():
                    self.err_lab_lastname.setVisible(True)
            else:
                if self.err_lab_lastname.isVisible():
                    self.err_lab_lastname.setVisible(False)
            if not info_val_list[2]:
                if not self.err_lab_password.isVisible():
                    self.err_lab_password.setVisible(True)
            else:
                if self.err_lab_password.isVisible():
                    self.err_lab_password.setVisible(False)
            if not info_val_list[3]:
                if not self.err_lab_repassword.isVisible():
                    self.err_lab_repassword.setVisible(True)
            else:
                if self.err_lab_repassword.isVisible():
                    self.err_lab_repassword.setVisible(False)
            if not info_val_list[4]:
                if not self.err_lab_email.isVisible():
                    self.err_lab_email.setVisible(True)
            else:
                if self.err_lab_email.isVisible():
                    self.err_lab_email.setVisible(False) 
            if not info_val_list[5]:
                if not self.err_lab_phone.isVisible():
                    self.err_lab_phone.setVisible(True)
            else:
                if self.err_lab_phone.isVisible():
                    self.err_lab_phone.setVisible(False)  
            if not info_val_list[6]:
                if not self.err_lab_city.isVisible():
                    self.err_lab_city.setVisible(True)
            else:
                if self.err_lab_city.isVisible():
                    self.err_lab_city.setVisible(False)
            if not info_val_list[7]:
                if not self.err_lab_day.isVisible():
                    self.err_lab_day.setVisible(True)
            else:
                if self.err_lab_day.isVisible():
                    self.err_lab_day.setVisible(False) 
            if not info_val_list[8]:
                if not self.err_lab_month.isVisible():
                    self.err_lab_month.setVisible(True)
            else:
                if self.err_lab_month.isVisible():
                    self.err_lab_month.setVisible(False) 
            if not info_val_list[9]:
                if not self.err_lab_year.isVisible():
                    self.err_lab_year.setVisible(True)
            else:
                if self.err_lab_year.isVisible():
                    self.err_lab_year.setVisible(False)                                                              
        else:
            if self.err_lab_firstname.isVisible():
                    self.err_lab_firstname.setVisible(False)
            if self.err_lab_lastname.isVisible():
                    self.err_lab_lastname.setVisible(False)  
            if self.err_lab_password.isVisible():
                    self.err_lab_password.setVisible(False)
            if self.err_lab_repassword.isVisible():
                    self.err_lab_repassword.setVisible(False)  
            if self.err_lab_email.isVisible():
                    self.err_lab_email.setVisible(False)  
            if self.err_lab_phone.isVisible():
                    self.err_lab_phone.setVisible(False) 
            if self.err_lab_city.isVisible():
                    self.err_lab_city.setVisible(False)
            if self.err_lab_day.isVisible():
                    self.err_lab_day.setVisible(False) 
            if self.err_lab_month.isVisible():
                    self.err_lab_month.setVisible(False)
            if self.err_lab_year.isVisible():
                    self.err_lab_year.setVisible(False)                                                                   
            
            db_path = os.path.join(self.curr_dir, self.users_file)
            
            change_conn = sql.connect(db_path)
            change_cursor = change_conn.cursor()
            
            create_query = '''CREATE TABLE IF NOT EXISTS Users (first_name, last_name,
                                    user_name TEXT, password TEXT,
                                    security_answer TEXT, email TEXT,
                                    phone_number INT, city TEXT,
                                    birth_year INT, birth_month TEXT, birth_day INT,
                                    UNIQUE(first_name, last_name,
                                        user_name, password,
                                        security_answer, email,
                                        phone_number, city,
                                        birth_year, birth_month, birth_day))'''
                            
            change_cursor.execute(create_query) 
            change_conn.commit()                 
                            
            insert_query = '''INSERT OR IGNORE INTO Users (
                                    first_name, last_name,
                                    user_name, password,
                                    security_answer, email,
                                    phone_number, city,
                                    birth_year, birth_month, birth_day)
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)      
                              '''          
            #curr_info = [self.first_name, self.last_name, self.user_name,
                         #self.password, self.security_question, self.email, self.phone_number, self.city,
                         #self.birth_year, self.birth_mounth, self.birth_day]                      
                              
            change_cursor.execute(insert_query, tuple(self.curr_info)) 
            change_conn.commit()                    
            
            change_info_query = '''UPDATE Users
                                    SET first_name = ?, last_name = ?,
                                        user_name = ?, password = ?,
                                        security_answer = ?, email = ?,
                                        phone_number = ?, city = ?,
                                        birth_year = ?, birth_month = ?, birth_day = ?
                                    WHERE 
                                        first_name = ? AND last_name = ? AND
                                        user_name = ? AND password = ? AND
                                        security_answer = ? AND email = ? AND
                                        phone_number = ? AND city = ? AND
                                        birth_year = ? AND birth_month = ? AND birth_day = ?'''                            
                                        
            new_info = [first_name, last_name, self.user_name,
                        password, self.security_question, email, 
                        phone_number, city, year, month, day]       
            
            params = new_info + self.curr_info
            change_cursor.execute(change_info_query, tuple(params)) 
            change_conn.commit()      
              
            change_cursor.close()    
            change_conn.close()       
            
            self.first_name = first_name
            self.last_name = last_name
            self.password = password
            self.email = email
            self.phone_number = phone_number
            self.city = city
            self.birth_day = day
            self.birth_mounth = month
            self.birth_year = year    
            
    def Delete_User(self):
        delete_text = ""
        delete_text = self.delete_info_line.text()
        
        if delete_text != "":
            if self.delete_err.isVisible():
                self.delete_err.setVisible(False) 
                
            rev_db_path = os.path.join(self.curr_dir, self.revenue_file) 
            exp_db_path = os.path.join(self.curr_dir, self.expense_file)
            cat_db_path = os.path.join(self.curr_dir, self.category_file) 
            user_db_path = os.path.join(self.curr_dir, self.users_file)
            if delete_text == "user":
                self.close()
                if os.path.exists(rev_db_path):
                    os.remove(rev_db_path)
                    
                if os.path.exists(exp_db_path):
                    os.remove(exp_db_path )   
                    
                if os.path.exists(cat_db_path):
                    os.remove(cat_db_path)
                
                if os.path.exists(user_db_path):
                    try :
                        conn = sql.connect(user_db_path)
                        cursor = conn.cursor()
                        
                        delete_query = '''DELETE FROM Users WHERE 
                                                first_name = ? AND last_name = ? AND
                                                user_name = ? AND password = ? AND
                                                security_answer = ? AND email = ? AND
                                                phone_number = ? AND city = ? AND
                                                birth_year = ? AND birth_month = ? AND birth_day = ?
                                        ''' 
                        cursor.execute(delete_query, self.curr_info)  
                        conn.commit()
                        
                        cursor.close()      
                        conn.close()         
                    except :
                        pass
                
            elif delete_text == "transaction":
                if os.path.exists(rev_db_path):
                    os.remove(rev_db_path)
                    
                if os.path.exists(exp_db_path):
                    os.remove(exp_db_path)   
                    
                if os.path.exists(cat_db_path):
                    os.remove(cat_db_path)
                        
            elif delete_text == "just revenue":
                if os.path.exists(rev_db_path):
                    os.remove(rev_db_path)
                        
            elif delete_text == "just expense":
                if os.path.exists(exp_db_path):
                    os.remove(exp_db_path)       
        else:
            if not self.delete_err.isVisible():
                self.delete_err.setVisible(True)         
        
    def create_user_revenue_databse(self): 
        db_path = os.path.join(self.curr_dir, self.revenue_file)
        conn =  sql.connect(db_path)   
        cursor = conn.cursor()
        
        create_table_query = '''CREATE TABLE IF NOT EXISTS REVENUE (
                                    amount INT NOT NULL,
                                    source TEXT NOT NULL,
                                    description TEXT,
                                    type TEXT NOT NULL,
                                    year INT NOT NULL,
                                    month TEXT NOT NULL,
                                    day INT NULL, 
                                    UNIQUE(amount, source, 
                                    description, type, year, month, day))'''
                          
        cursor.execute(create_table_query)
        conn.commit()
        
        insert_query = '''INSERT OR IGNORE INTO REVENUE 
                                (amount, source, description, type, year, month, day)
                          VALUES 
                                (?, ?, ?, ?, ?, ?, ?)'''                 
        
        try:       
            rev_info = (int(self.rev_amount), self.rev_source, self.rev_desc, 
                        self.rev_type, int(self.rev_year), self.rev_month.lower(), int(self.rev_day))
            cursor.execute(insert_query, rev_info)
            conn.commit()
            if cursor:
                cursor.close()
            if conn:    
                conn.close()
            if self.close_rev_file_label.isVisible():
                self.close_rev_file_label.setVisible(False)
        except:
            if not self.close_rev_file_label.isVisible():
                self.close_rev_file_label.setVisible(True) 
                
    def create_user_expense_database(self):
        db_path = os.path.join(self.curr_dir, self.expense_file)
        conn =  sql.connect(db_path)   
        cursor = conn.cursor()
        
        create_table_query = '''CREATE TABLE IF NOT EXISTS EXPENSE (
                                    amount INT NOT NULL,
                                    source TEXT NOT NULL,
                                    description TEXT,
                                    type TEXT NOT NULL,
                                    year INT NOT NULL,
                                    month TEXT NOT NULL,
                                    day INT NULL, 
                                    UNIQUE(amount, source, 
                                    description, type, year, month, day))'''
                          
        cursor.execute(create_table_query)
        conn.commit()
        
        insert_query = '''INSERT OR IGNORE INTO EXPENSE 
                                (amount, source, description, type, year, month, day)
                          VALUES 
                                (?, ?, ?, ?, ?, ?, ?)'''                 
        
        try:       
            exp_info = (int(self.exp_amount), self.exp_source, self.exp_desc, 
                        self.exp_type, int(self.exp_year), self.exp_month.lower(), int(self.exp_day))
            cursor.execute(insert_query, exp_info)
            conn.commit()
            if cursor:
                cursor.close()
            if conn:    
                conn.close()    
            if self.close_exp_file_label.isVisible():
                self.close_exp_file_label.setVisible(False)
        except:
            if not self.close_exp_file_label.isVisible():
                self.close_exp_file_label.setVisible(True)  
                
    def create_user_category_database(self):
        cat_db_path = os.path.join(self.curr_dir, self.category_file)
        conn = sql.connect(cat_db_path)
        cursor = conn.cursor()
        
        create_table_query = '''CREATE TABLE IF NOT EXISTS CATEGORY 
                                (
                                    category TEXT, 
                                    UNIQUE (category)
                                )'''
                                
        cursor.execute(create_table_query) 
        conn.commit()       
        
        add_item_query = '''INSERT OR IGNORE INTO CATEGORY (category)
                            VALUES (?)'''
                             
        for category in self.category_combo:
            cursor.execute(add_item_query, (category, ))
            conn.commit()
            
        conn.close()                                    
            
    def add_item_category_combo(self):
        cat_db_path = os.path.join(self.curr_dir, self.category_file)
        
        conn = sql.connect(cat_db_path)
        cursor = conn.cursor()
        
        select_query = '''SELECT * FROM CATEGORY'''
        cursor.execute(select_query) 
        rows = cursor.fetchall()
        conn.commit()
        
        items_category = [row[0] for row in rows]
        self.source_of_revenue_combo_box.addItems(items_category)
        
        conn.close()

    def add_text_to_db(self):
        cat_db_path = os.path.join(self.curr_dir, self.category_file)  
        #if not os.path.exists(cat_db_path):       
            #self.create_user_category_database()
        
        conn = sql.connect(cat_db_path)
        cursor = conn.cursor()
        
        text_category_xl = self.add_category_line.text()
        check_query = '''SELECT category FROM CATEGORY WHERE category = ?'''
        cursor.execute(check_query, (text_category_xl, )) 
        resault = cursor.fetchall()
        conn.commit()

        if resault:
            self.category_label.show()
        else:
            if self.category_label.isVisible():
                self.category_label.hide()
            try:
                insert_query = '''INSERT OR IGNORE INTO CATEGORY (category)
                                  VALUES (?)'''
        
                cursor.execute(insert_query, (text_category_xl, )) 
                conn.commit()
                self.add_category_line.clear()

                self.category_label_err.hide()
                self.category_label.hide()
            except PermissionError :
                self.category_label_err.show()  
        conn.close()                                    
                
    def exit(self):
        self.close()  
    
    def switch_to_dark_mode(self, event):
        self.leftWidget.setStyleSheet("background-color: #BBB477;")
        self.rightWidget.setStyleSheet("background-color: #2E5894;")

    def switch_to_light_mode(self, tevent):
        self.leftWidget.setStyleSheet("background-color: #FBE870;")
        self.rightWidget.setStyleSheet("background-color: #52afb6;")
                
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater() 
                
    def set_year_revenue_line(self, index):
        year = self.year_of_revenue_combo_box.itemText(index)
        self.year_of_revenue_line.setText(year)

    def set_month_revenue_line(self, index):
        month = self.month_of_revenue_combo_box.itemText(index)
        self.month_of_revenue_line.setText(month)

    def set_day_revenue_line(self, index):
        day = self.day_of_revenue_combo_box.itemText(index)
        self.day_of_revenue_line.setText(day)

    def set_source_line(self, index):
        day = self.source_of_revenue_combo_box.itemText(index)
        self.source_of_revenue_line.setText(day)            
                
    def set_revenue_line(self, index):
        revenue_type = self.type_of_revenue_combo_box.itemText(index)
        self.type_of_revenue_line.setText(revenue_type)

    def update_type_combo_box(self):
        text = self.type_of_revenue_line.text()
        if text and self.type_of_revenue_combo_box.findText(text) == -1:
            self.type_of_revenue_combo_box.addItem(text)

    def set_year_expense_line(self, index):
        year = self.year_of_expense_combo_box.itemText(index)
        self.year_of_expense_line.setText(year)

    def set_month_expense_line(self, index):
        month = self.month_of_expense_combo_box.itemText(index)
        self.month_of_expense_line.setText(month)

    def set_day_expense_line(self, index):
        day = self.day_of_expense_combo_box.itemText(index)
        self.day_of_expense_line.setText(day)            
                
    def set_year_report_line(self, index):
        year = self.year_of_report_combo_box.itemText(index)
        self.year_of_report_line.setText(year)

    def set_month_report_line(self, index):
        month = self.month_of_report_combo_box.itemText(index)
        self.month_of_report_line.setText(month)

    def set_day_report_line(self, index):
        day = self.day_of_report_combo_box.itemText(index)
        self.day_of_report_line.setText(day)

    def set_delete_line(self, index):
        day = self.delete_info_combo.itemText(index)
        self.delete_info_line.setText(day)

    def set_year_edit_line(self, index):
        year = self.year_of_edit_combo_box.itemText(index)
        self.year_line_edit2.setText(year)            
                
    def set_month_edit_line(self, index):
        month = self.month_of_edit_combo_box.itemText(index)
        self.mounth_line_edit2.setText(month)

    def set_day_edit_line(self, index):
        day = self.day_of_edit_combo_box.itemText(index)
        self.day_line_edit2.setText(day)

    def set_year_report_line2(self, index):
        year = self.year_of_report_combo_box2.itemText(index)
        self.year_of_report_line2.setText(year)

    def set_month_report_line2(self, index):
        month = self.month_of_report_combo_box2.itemText(index)
        self.month_of_report_line2.setText(month)             
                
    def set_day_report_line2(self, index):
        day = self.day_of_report_combo_box2.itemText(index)
        self.day_of_report_line2.setText(day)

    def set_expense_line(self, index):
        expense_type = self.type_of_expense_combo_box.itemText(index)
        self.type_of_expense_line.setText(expense_type)

    def update_combo_box_expense(self):
        text = self.type_of_expense_line.text()
        if text and self.type_of_expense_combo_box.findText(text) == -1:
            self.type_of_expense_combo_box.addItems(text) 
            
#if __name__ == '__main__' :
    #app = Validation.QApplication(Validation.sys.argv)
    #ex = MainUI()    
    #Validation.sys.exit(app.exec())                                                    