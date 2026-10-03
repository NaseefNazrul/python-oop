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

# Going to make a book journal class 
class book_journal:
    counter = 0 # Number of books read so far 
    def __init__(self, type) -> None:
        print("Created a", type, "book journal")
        self.type = type
        self.books = {}
        