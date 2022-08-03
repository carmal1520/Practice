class User:

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        user_info = {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Username" : self.username,
            "Email" : self.email,
        }

        for x, y in user_info.items():
            print(f"{x} : {y}")
    
    def greet_user(self):
        message = f"Welcome back {self.first_name.title()} {self.last_name.title()}!"
        print(message)
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self. login_attempts = 0

class Amin(User):

    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()

class Privileges():

    def __init__(self, privileges = []):
        self.privileges = privileges
        
    def show_privileges(self):
        
        if self.privileges:
            for privilege in self.privileges:
                print(privilege)