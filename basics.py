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
# Date of Birth
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

    @property
    def password(self):
        raise AttributeError("Cannot access the password")
    
    def change_password(self, curr_pass, new_pass):
        if curr_pass == self.__password:
            self.__password = new_pass
            print("Password changed successfully")
        else:
            print("Wrong password")

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, new_email):
        if '@' in new_email:
            self._email = new_email
            print("Email has been changed to", new_email)
        else:
            print("Incorrect email entered")


    def info(self):
        print(f"{self.first_name} {self.last_name}")
        print(self.dot)
        if not self.reviews:
            print(f"{self.first_name} has not published any reviews")
            return
        for book, review in self.reviews.items():
            print(book + ": " + review)



# ---------------------Book---------------------------
# Stores all the Book's information 
class Book: 
    def __init__(self, title, author, ISBN = None, *genre) :
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre

# ------------------BookReview--------------------
# Stores the total number of reviews 
# Stores the list of people that gave the reviews 
# Users can post a review
# Users can remove a review 
# Users can register 
# Users can log in 
# Users can view a review depending on a book
# Can review each and every review  

class BookReview:
    def __init__(self) -> None:
        self.users = {}
        self.books_reviewed = {}

    def 

        