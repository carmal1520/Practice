from priv_admin import Admin

liam = Admin("liam", "Arocho", "moose@live.com", "mrmoose")
print(liam.describe_user())

liam_prive = ["can reset passwords"]

liam.privileges.privileges = liam_prive
print(liam.privileges.show_privileges())
