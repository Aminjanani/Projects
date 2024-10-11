# user class : This class includes the user's attributes       
class user:
    def __init__(self):
        self.user_name = ""
        self.first_name = ""
        self.last_name = ""
        self.password = ""
        self.repeat_password = ""
        self.security_question = ""
        self.email = ""
        self.phone_number = ""
        self.city = ""
        self.birth_day = "" 
        self.birth_mounth = "" 
        self.birth_year = ""
        self.users_file = "users_file.db"
        
    def set_user_attr(self, user_info):
        self.first_name = user_info[0]
        self.last_name = user_info[1]
        self.user_name = user_info[2]
        self.password = user_info[3]
        self.security_question = user_info[4]
        self.email = user_info[5]
        self.phone_number = user_info[6]
        self.city = user_info[7]
        self.birth_year = user_info[8]
        self.birth_mounth = user_info[9]
        self.birth_day = user_info[10]