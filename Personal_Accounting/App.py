import sys
from PyQt6.QtWidgets import QApplication
from Welcome import welcome

#Application class : This class contains all above classes and their methods to run the app  
class App(welcome):
    def __init__(self):
        welcome.__init__(self)
        self.Run_App()
        
    def Run_App(self):
        self.welcome_page()    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()    
    sys.exit(app.exec())