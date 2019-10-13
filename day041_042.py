#Classes in Python

class Book:
    def __init__(self, name, authar, pages, edition):
        self.name = name
        self.authar = authar
        self.pages = pages
        self.edition = edition
    
    def bookInfo(self):
        print("Book Name: " + self.name)
        print("Authar   : " + self.authar)
        print("Pages    : " + self.pages)
        print("Edition  : " + self.edition)

book1 = Book("The Lure", "Steve Schroeder", "540", "First Edition")
book1.bookInfo()
