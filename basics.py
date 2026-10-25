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


# -----------------------------------USER CLASS------------------------------------------
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



# ------------------------------------Book------------------------------------------
# Stores all the Book's information 
class Book: 
    def __init__(self, title, author, ISBN = None, *genre): # We archive all books' infos
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre

    def info(self):
        print("Title", self.title)
        print("Author", self.author)
        print("Genre", *self.genre)
        if self.ISBN != None:
            print("ISBN", self.ISBN)

# ----------------------------------BookReview---------------------------------------
# Stores the total number of books 
# Stores the list of people that gave the reviews 
# Shows the books that are reviewed
# Users can post a review
# Users can remove a review 
# Users can register 
# Users can log in 
# Users can view a review by checking the book
# shows every review
# search a user  
# Profile viewer of the current logged in user

class BookReview:
    def __init__(self) -> None:
        self.users = {}
        self.books_reviewed = {} # {title:[book_object, [User1_review, User2_review, and so on]} will store the User and then access their review 
                                    # We access the each user's class for the views depending on the book
        self.current_user = None 
        # This is for keeping the current_user logged in 

    def register(self, first_name, last_name, dot, email, password):
        if first_name in self.users:
            print("The user is already registered")
        else:
            new_user = User(first_name, last_name, dot, email, password)
            self.users[first_name] = new_user

    def login(self, first_name, password):
        if first_name in self.users:
            if password == self.users[first_name].password:
                self.current_user = first_name
            else:
                print("Wrong Password, please try again")
        else:
            print("The user is not registered")

    def post_review(self, title, author, ISBN = None, *genre, review):
        # The user has to be logged in first 
        if self.current_user == None: 
            print("Please log in to post a review")
        else:
            if title in self.books_reviewed:
                self.users[self.current_user].reviews[title] = review
                self.books_reviewed[title][1].append(self.users[self.current_user])
                print("Your Review has been successfully posted")
            else:
                new_book = Book(title, author, ISBN, *genre)
                self.users[self.current_user].reviews[title] = review
                self.books_reviewed[title] = [new_book,[self.users[self.current_user]]]
                print("Your Review has been successfully posted")

    def remove_review(self, title):
        if self.current_user == None:
            print("Please log in first")
        else:
            if title in self.users[self.current_user].reviews:
                # As we are archiving all the books, we only delete the user's reviews
                del self.users[self.current_user].reviews[title]
                print("Your review has been removed")
            else:
                print("You have not reviewed this book")

    def showBooks(self):
        print(str(len(self.books_reviewed)) + " Have been reviewed")
        for title in self.books_reviewed:
            print(title)

    def showReviews(self):
        if len(self.books_reviewed) == 0: 
            print("No books have been reviewd :(")
        else:
            for title, info in self.books_reviewed.items():
                info[0].info()
                print(" ")
                print("Reviews")
                for user in info[1]:
                    print(user.first_name + ": " + user.reviews[title])
                    print(" ")
                print("------------------------------------------------------------------------------------------------")
                print(" ")

    def searchBook(self,title):
        if title in self.books_reviewed:
            print(self.books_reviewed[title].info())
            print(" ")
            for user in self.books_reviewed[title][1]:
                print(user.first_name + ": " + user.reviews[title])
                print(" ")
        else:
            print("The book you are searching for does not exist")

    def searchUser(self, first_name):
        if first_name in self.users:
            self.users[first_name].info()
            for title, review in self.users[first_name].reviews.items():
                print(title + " : " + review)
        else:
            print("The user does not exist")

    def viewProfile(self):
        if self.current_user == None:
            print("Please log in first to view profile")
        else:
            self.users[self.current_user].info()
            for title, review in self.users[self.current_user].reviews.items():
                print(title," : ", review)

    def logout(self):
        if self.current_user == None:
            print("You are already logged out")
        else:
            self.current_user = None
            print("Logged out!")







#-------------------------------------------Script-----------------------------------------
