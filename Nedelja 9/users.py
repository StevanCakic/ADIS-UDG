class User:
    def __init__(self, name):
        self.__name = name
        print("User init")
    def who_am_i(self):
        print("I'm User")
    def login(self):
        print("User login")

class Admin(User):
    def __init__(self, name, super_admin=False):
        User.__init__(self, name)
        
        self.__super_admin = super_admin
        print("Admin")
    
    def who_am_i(self):
        print("I'm Admin")
    
    def delete_user(self):
        print("I can delete User")
    
user1 = User("User 1")
print("----------")
admin1 = Admin("Admin 1")
print("----------")
user1.who_am_i()
print("----------")
admin1.who_am_i()
print("----------")
admin1.login()
print("----------")
admin1.delete_user()
