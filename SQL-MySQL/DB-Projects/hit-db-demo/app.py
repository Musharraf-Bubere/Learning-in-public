import sys
from dbhelper import DBhelper

class Flipkart:

    def __init__(self):
        self.db = DBhelper()
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
            1. Enter 1 to register
            2. Enter 2 to Login
            3. Anything else to leave
            """)

            if user_input == "1":
                self.register()
            elif user_input == "2":
                self.login()
            else:
                sys.exit(1000)

    def register(self):
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        password = input("Enter the password: ")

        if not name or not email or not password:
            print("All fields are required")
            return

        response = self.db.register(name, email, password)

        if response == 1:
            print("Registration Successful")
        else:
            print("Registration failed")

    def login(self):
        print("Login feature coming soon")

obj = Flipkart()