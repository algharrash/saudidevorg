#Inheritance in Python

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

class eBook(Book):
    def __init__(self, name, authar, pages, edition, kind):
        super().__init__(name, authar, pages, edition)
        self.kind = kind
    
    def bookInfo(self):
        print("Book Name: " + self.name)
        print("Authar   : " + self.authar)
        print("Pages    : " + self.pages)
        print("Edition  : " + self.edition)
        print("Kind     : " + self.kind)

ebook1 = eBook("The Lure", "Steve Schroeder", "540", "First Edition", "PDF")
ebook1.bookInfo()
