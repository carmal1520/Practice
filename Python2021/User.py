class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_atttempts = 0

    def describe_user(self):
        user_info = {
            "First Name" : self.first_name,
            "Last Name" : self.last_name,
            "Username" : self.username,
            "Email" : self.email,
        }

        for key, value in user_info.items():
            print(f"{key} : {value}")

    def greet_user(self):
        msg = f"\nHello {self.first_name.title()} {self.last_name.title()}"
        print(msg)

    def increment_login_attempts(self):
        self.login_atttempts += 1
