"""Write a Library class with no_of_books and books as two instance variables.
Write a program to create a library from this Library class and show how you can
print all books, add a book and get the number of books using different methods.
Show that your program doesnt persist the books after the program is stopped!
"""

print("----------------------------------Welcome In Library In System----------------------------------")
print("------------------------------------------------------------------------------------------------\n")

class Library: #-->Class Of Libaray

    def __init__(self): # -->Default Constructor 
        #-----Initilize The All Things----
        self.no_of_book = 0
        self.list_of_books = []
        self.BorrowBook = []
        self.name = ""
        self.returnName = ""
        self.ReturnBook = []

    def AddBook(self): #--> Add The Book
        size = int(input("Enter the size of Book List\t")) #-->Size Of Book Of list
        for i in range(size):#-->Loop For enter the book
            book = input("\nEnter the book name\t")  #-->Enter the Book Name
            self.list_of_books.append(book) #-->Append the Book in the list
            self.no_of_book = self.no_of_book + 1 #-->Increment the amount of book

    def PrintBook(self):#-->print the book
        print(f"Books are:--> {self.list_of_books}")

    def AmountOfBookRerurn(self): #-->Return the total number of book
        return self.no_of_book  

    def BorrowOfBook(self): #-->For Borrow The Book
        self.name = input("Enter the your name:\t") #-->Name Of Person
        self.PrintBook() #Calling Print Function
        amount = int(input("Enter the amount of book for Borrow\t")) #-->Amount Of Book For Borrow
        for i in range(amount): #--> Loop For enter the book
            choice = input("Chose The Book From List Of Books\t")#-->print all Book And Select the Book For Borrow 
            self.BorrowBook.append(choice)#-->Append the Book in the list
        for i in range(self.no_of_book): #-->Outer Loop
            for j in range(amount):  #-->Inner Loop
                    if(self.BorrowBook[j] == self.list_of_books[i]): #Compare the Books on both loop index
                        self.ReturnBook.append(self.BorrowBook[j])  #Append thw book who find in list in return of list     
            j = j + 1  #-->increment of inner loop        
        i =  i + 1 #-->increment of outer loop
        print(f"{self.name} Selects the book from list are for borrow -->\"{self.ReturnBook}\"") 

    def ReturnOfBook(self): #-->For Return The Book
       self.returnName = input("Enter the your name:\t") #-->Name Of Person
       if(self.name == self.returnName): #-->Compare the Borrow Person Name and Return Person Name
        print(f"{self.name} Return The Books are -->\"{self.ReturnBook}\"") #-->Print the list
       else:
        print("You are not the person who borrow the book from my library") 
#-----------------------------------MAIN---------------------------------------------
NtuLibrary = Library() #-->Making Object
NtuLibrary.AddBook() #-->Calling add function
print("\n--------------------------Books Detail----------------------------------\n")
NtuLibrary.PrintBook() #-->Calling the Print Function
print(F"\nAmount Of Book In Library:--> {NtuLibrary.AmountOfBookRerurn()}\n") #-->Print the Amount Total Book 

print("\n--------------------------Books Borrow Detail----------------------------------\n")
Borrow = input("Do You Want To Some Book For Borrow Then Write True OtherWise False:\t") #-->Asking Question For Borrow
if(Borrow == "True"): #-->Check The Condition
    NtuLibrary.BorrowOfBook() #Calling the Borrow Function
elif(Borrow == "False"): #-->Check The Condition
    print("Thanks For Coming")
else: #-->Default Condition
    print("Plz Choce Correct Option!!\nThanks For Coming")    

#Check The Condition Person Borrow The Book or Not
if(Borrow == "True"):
    print("\n--------------------------Books Return Detail----------------------------------\n")
    Return = input("Return For The Book Then Write True OtherWise False:\t") #-->Asking Question For Return
    if(Return == "True"):#-->Check The Condition
        NtuLibrary.ReturnOfBook() #Calling the Return Function
    elif(Return== "False"):#-->Check The Condition
        print("Thanks For Coming")
    else:#-->Default Condition
        print("Plz Choce Correct Option!!\nThanks For Coming")
#Default Condition           
else:
    print("Thanks For Coming In Ntu Library")

with open("Libarry.txt","w") as File:
    File.write(str(NtuLibrary.__dict__))  

print("\n\n\n------------------------------------In The File Of Libarary------------------------------------") 
with open("Libarry.txt","r") as file:
    print(file.read())   