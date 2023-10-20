from .librarian import *

class Client:
    def __init__(self):
        self.server = Librarian()
        self.shelf = list()
        with open(self.server._file) as f:
            for line in f:
                load = str(line.strip())
                self.shelf.append(load)

    def seeShelf(self):
        print("\n.....processing....")
        if not self.shelf:
            with open(self.server._file) as f:
                for line in f:
                    content = str(line.strip())
                    self.shelf.append(content)
                for k,v in enumerate(self.shelf,start = 1):
                    print(f"{k}. {v}")

        else:
            self.shelf = []
            with open(self.server._file) as f:
                for line in f:
                    content = str(line.strip())
                    self.shelf.append(content)
                for k,v in enumerate(self.shelf,start = 1):
                    print(f"{k}. {v}")

    def searchBookByLetter(self):
        print("\n.....processing....")
        if self.shelf:
            letter = input("\nenter letter ")
            if not letter == "" and len(letter) == 1:
                for v in self.shelf:
                    if v.startswith(letter):
                        print(f"- {v}")
            else:
                print("\n*invalid!\nEnter the first letter of the book title!")
        else:
            print("\nshelf is empty!")
    
    def searchBookByName(self):
        print("\n.....processing....")
        if self.shelf:
            bookName = input("\nEnter book Name ")
            print("\n.....processing....")
            if bookName in self.shelf:
                print(bookName.title())
            else:
                print(f"{bookName} not found!\ncheck name and retry!")

        else:
            print("\nshelf is empty!")
