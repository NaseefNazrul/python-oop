# The list of things I will apply 
# Access Modifiers 
# @property decorator 
# @attribute.setter decorator 
# _attribute the underscore is convention to say its a protecter variable 
# __attribute is for private variables 
# Static attribute 
# Instance attribute
# @staticmethod decorator
# Can make method protected or private using _ or __ respectively

# Going to make a user class and book review class (very surface level)


# -----------USER CLASS--------------
# This will contain all the information of the user
# First Name
# Last Name
# Date of Birt
# email - protected
# password - private
# List of books they reviewed
# Prints user info as well as the reviews they published 
# can change password 
#     - asking for the current password and changing 
# can change email  
#     - making sure the email is correct

class User:
    user_rev_count = 0

    def __init__(self, first_name, last_name, dot, email, password) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.dot = dot
        self._email = email
        self.__password = password
        self.reviews = {}

    def change_pass(self, curr_pass, new_pass):
        if curr_pass == self.__password:
            self.__password = new_pass
            print("New password has been allocated")
        else:
            print("Wrong password")

    def change_email(self, new_email):
        if '@' in new_email:
            self._email = new_email
            print("Email has been changed to", new_email)
        else:
            print("Incorrect email entered")

    def info(self):
        