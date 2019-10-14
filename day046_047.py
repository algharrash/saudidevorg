#week 7 challenge

class Library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf

myLibrary = Library(300, 45)

class science_section(Library):
    def __init__(self, book, shelf, name):
        super().__init__(book, shelf)
        self.name = name
    
    def print_section(self):
        print("Section:" + self.name)
        print("Book   :" , self.book)
        print("Shelf  :" , self.shelf)

mySection = science_section(300, 45, "Physics Books")
mySection.book = 20
mySection.shelf = 4
mySection.print_section()

