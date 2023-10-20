global Password
with open("src/pf.txt") as f:
    for line in f:
        Password = int(line.strip())

class Librarian:
    def __init__(self):
        self._Pass = Password 
        self._shelf = list()
        self._session = int()
        self._file = "src/shelf.txt"

    def logIn(self):
        print("\nProcessing...")
        for a in range(2):
            try:
                verify = int(input("\nEnter pin "))
            except :
                print("\n*digits only")
            else:
                if verify == self._Pass:
                    print("\nWelcome ...")
                    self._session += 1
                    return None
                else:
                    print("*invalid\nretry")
    
    def logOut(self):
        if self._session:
            self._session = int()
            print("logged out!")
        else:
            print("\nnot logged in!")

    def changePass(self):
        print("\n....processing....")
        if self._session:
            for b in range(2):
                try:
                    previous_P = int(input("\nEnter previous password "))
                except:
                    print("\ndigits only")
                else:
                    if previous_P == self._Pass:
                        try:
                            new_P = int(input("\nCreate new password "))
                        except:
                            print("\n*digits only")
                        else:
                            with open("pf.txt","w+") as f:
                                f.write(str(new_P))
                            self._Pass = new_P
                            print("\nPassword changed!")
                            return None
                    else:
                        print("\nincorrect pin\nretry")

        else:
            print("\naction can\'t be performed\nlog in!")

    def addBook(self):
        print("\n....processing....")
        if self._session:
            try:
                verify = int(input("\nEnter your pin "))
            except:
                print("\n*digits only")
            else:
                if verify == self._Pass:
                    print("\nWelcome ...")
                    try:
                        numOfBooks = int(input("\nHow many books do you want add to the shelf ? "))
                    except:
                        print("\n*enter required input only")
                    else:
                        print("\nEnter book name ")
                        with open(self._file,"a+") as f:
                            for bookName in range(numOfBooks):
                                uploadBook = input()
                                print(f"uploading {uploadBook}....\n")
                                if not uploadBook in f:
                                    f.write(f"{uploadBook}\n")
                                else:
                                    print(f"\n{uploadBook} already exists!")
                            print("....\ndone!")

                else:
                    print("\nincorrect pin\nretry")

        else:
            print("\naction can\'t be performed\nlog in!".title())

    def seeShelf(self):
        print("\n....processing....")
        if self._session:
            if self._shelf:
                self._shelf = []
                with open(self._file) as refresh:
                    for line in refresh:
                        content = line.strip()
                        self._shelf.append(content)

                for k,v in enumerate(self._shelf,start = 1):
                    print(f"{k}. {v}")
            else:
                with open(self._file) as s:
                    for line in s:
                        load = line.strip()
                        self._shelf.append(load)
                print("\nrefreshing...\nRetry!")

        else:
            print("\naction can\'t be performed\nlog in!".title())
    
    def removeBook(self):
        print("\n....processing....")
        if self._session:
            try:
                verify = int(input("\nEnter your pin "))
            except:
                print("\n*digits only")
            else:
                if verify == self._Pass:
                    print("\nWelcome ...")
                    try:
                        noOfBookToRemove = int(input("\nTip : Max removal = 5\nHow many book(s) do you want to remove? "))
                    except:
                        print("\ninvalid input")
                    else:
                        if noOfBookToRemove <= 0 or noOfBookToRemove > 5:
                            print(f"\nError\ncan\'t remove {noOfBookToRemove} at once!")
                        else:
                            print("\nEnter name of book to be deleted")
                            for books in range(noOfBookToRemove):
                                delete = input()
                                if delete in self._shelf:
                                    self._shelf.remove(delete)
                                    print(f"\"{delete}\" was deleted")
                                else:
                                    print(f"\"{delete}\" not found!")


                else:
                    print("\nincorrect!\naccess denied")

        else:
            print("\naction can\'t be performed\nlog in!".title())
