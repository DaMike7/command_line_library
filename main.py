from src.client import *
from src.librarian import *

class Library:
    def __init__(self,name):
        self.name = name
        self.user = Client()
        self.Admin = Librarian()

    def identify(self):
        print("\n....processing....")
        print("""
        \nEnter
        (1) to continue
        (2) to exit
        
        \tor

        Enter Pin To Login As Admin
        """.title())
        try:
            action = int(input('\t=> '))
        except:
            print("\n*digits only!")
        else:
            if action == self.Admin._Pass:
                print("\n...processing...")
                while True:
                    try:
                        action_a = int(input("\nEnter\n1. to log in\n2. to change password\n3. to upload a book\n4. to delete a book\n5. to see the whole catalogue\n6. to log out\n\n".title()))
                    except:
                        print("\n*digits only!")
                    else:
                        if action_a == 1:
                            self.Admin.logIn()
                        elif action_a == 2:
                            self.Admin.changePass()
                        elif action_a == 3:
                            self.Admin.addBook()
                        elif action_a == 4:
                            self.Admin.removeBook()
                        elif action_a == 5:
                            self.Admin.seeShelf()
                        elif action_a == 6:
                            self.Admin.logOut()
                            return None
                        else:
                            print("\n*invalid!")

            elif action == 1:
                print("\n...processing...")
                while True:
                    try:
                        action_b = int(input("\nEnter\n1. to see the whole catalogue\n2. to search book by letter\n3. to search book by name\n4. to log out\n".title()))
                    except:
                        print("\n*digits only!")
                    else:
                        if action_b == 1:
                            self.user.seeShelf()

                        elif action_b == 2:
                            self.user.searchBookByLetter()
                        elif action_b == 3:
                            self.user.searchBookByName()
                        elif action_b == 4:
                            print("\nlogged out!")
                            return None
                        else:
                            print("\ninvalid!")

            elif action == 2:
                print("\nIt was nice having you around!\ncome some other time.".title())
                exit()

            else:
                print("\n*invalid!")

def main(L):
    print(f"Welcome to {L.name}.")
    while True:
        L.identify()

if __name__ == "__main__":
    L = Library("The Community Library")
    main(L)
