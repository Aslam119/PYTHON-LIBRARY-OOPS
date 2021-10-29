class Library:

    books = []
    count = 0

    def insertBook(self,name,author):
        self.count += 1
        book = {
            "name":name,
            "author":author,
            "id":self.count,
        }
        print("BOOK SUCCESFULLY INSERTED YOUR ID IS NOTE IT!: ",self.count)

        self.books.append(book)
    
    def removeBook(self,id):
        isFound = False
        for book in self.books:
            if book["id"] == id:
                self.books.remove(book)
                print("BOOK SUCCESFULLY REMOVED")
                isFound = True
                break
        if not isFound:
            print("BOOK UNSUCCESSFULY REMOVED WRONG ID I GUESS")
    def getNum(self):
        counter = 0
        for book in self.books:
            counter += 1

        print("BOOKS: ",counter)

    def getBook(self,id):
        isFound = False
        for book in self.books:
            if book["id"] == id:
                print(book)
                isFound = True
                break
        
        if not isFound:
            print("BOOK NOT FOUND WRONG ID I GUESS")

    def printBooks(self):
        for book in self.books:
            print(book)

def useLibrary():
    library = Library()
    isRunning = True
    while isRunning:
        command = str(input("Enter command (insert,remove,get,size,print,exit): "))
        command = command.lower()
        if command == "insert":
            title = str(input("Enter Title: "))
            author = str(input("Enter AUTHOR: "))
            library.insertBook(title,author)
        elif command == "remove":
            id = int(input("Enter Book Id: "))
            library.removeBook(id)
        elif command == "size":
            library.getNum()
        elif command == "get":
            id = int(input("Enter Book Id: "))
            library.getBook(id)
        elif command == "print":
            library.printBooks()
        elif command == "exit":
            print("THANK YOU !!!")
            isRunning = False
            break
        else:
            print("WRONG COMMAND")

useLibrary()
