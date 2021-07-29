from users import User


class Privileges:

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nThis admin has such privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):

    def __init__(self, first_name, last_name, username, email, age):
        super().__init__(first_name, last_name, username, email, age)
        self.privileges = Privileges()
