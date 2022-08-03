from user_priv_admin import User, Amin, Privileges

carlos = Amin("Carlos", "Maldonado", "leeto", "leeto@hotmail.com")
carlos.describe_user()
carlos_privileges = [
    "can reset passwords"
]
carlos.privileges.privileges = carlos_privileges

carlos.privileges.show_privileges()