class User:
    def __init__(self, first_name, last_name, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
      summary = f"""
      Name: {self.first_name} {self.last_name}
      Email: {self.email}
      Username: {self.username}
      """
      return summary

    def greet_user(self):
        greeting = f"Hello {self.first_name} {self.last_name}"
        return greeting
    
    def increment_login(self):
        self.login_attempts += 1 

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, email, username):
        super().__init__(first_name, last_name, email, username)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print("You have the following privileges")
        for privilege in self.privileges:
            print(f"\t{privilege}")