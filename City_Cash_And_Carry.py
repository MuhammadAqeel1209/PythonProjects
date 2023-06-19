#Customer Function -->👉 that give name of customer
def Customer():
    name = input("Enter your name Customer\t")
    print(f"Welcome \"{name}\" Sir in (SGS)")

#Menus Function -->👉 work of that function -->1)Show the menu
def Menu(menu):
      if(menu == 1):
            # display the dictionary(about menu list)
            for i in priceList.keys():    
                print(f"{i} are in menu and price is {priceList[i]}")
      else:
        print("Invalid Input !!") 
#Order Function --> 👉 work of that function -->1)Asking of Order and 2)Confrim Your Order                    
def Order():
    #Asking For Order
    more = input("\n\nDo You Want The Order \"Yes\" or \"No\"\t")
    while (more != "No"): 
        if(more == "No"):
            print("Your Order Complete\nThanks for coming") 
        if(more != "Yes"):
            print("Invalid Input!!!")
            break   
        j = 0      
        order = input("\nEnter the Order From menu\t")
        if order in menuList:
                quantity = int(input("Enter the quantity\t"))
                reamingamount = quantity - int(menuList[order]) #Calculate the quantity of stock
                if(order == "Egg"):
                    print(f"your order {order} in {quantity} in dozen")
                    SaveOrder(order, quantity) #Save your order in the list of order
                    bill.append(quantity * priceList[order]) #Save the money of your order
                    more = input("You Wanted to more order \"Yes\" or \"No\" \t")
                elif(order == "Bread" or order == "ColdDrink"):
                    print(f"your order {order} in {quantity} in pack") #Calculate the quantity of stock
                    SaveOrder(order, quantity)#Save your order in the list of order
                    bill.append(quantity * priceList[order]) #Save the money of your order
                    more = input("You Wanted to more order \"Yes\" or \"No\" \t")
                elif(order == "Sugar" or order == "Flour"):
                    print(f"your order {order} in {quantity} in kg") #Calculate the quantity of stock
                    SaveOrder(order, quantity)#Save your order in the list of order
                    bill.append(quantity * priceList[order]) #Save the money of your order
                    more = input("You Wanted to more order \"Yes\" or \"No\" \t")     
        else:
            print(f"{order} not available in my store")       
        j = j + 1 
    if(more == "No"):     
        print("\n\nYour Order is complete Go To Cashier for Bill") 
        GoToCasheir() #When Order Complete and move to cashier for bill

def SaveOrder(order,quantity):
    #Order and quantity save in the dictionary
    data = f"{order} : {quantity}" 
    order,quantity = data.split(":")
    billList[order] = quantity

def ShowBill():
    count = -1
    sum = 0
    print("Name\tQuantity\tPrice")
    for i in billList.keys():
        #Show the bill of your complete order
        print(f"{i}\t{billList[i]}",end="\t\t")
        for j in bill:
            count = count + 1
            sum = sum + bill[count] #Calculate the total bill 
            print(bill[count])
            break
    print(f"\n Total Bills is {sum}")
    return sum    #Return the total bill

def GoToCasheir():
    #Asking about Payment method --> 👉1)Cash and 2)Card
    choice = int(input("Enter \"1\" for Cash Payment\nEnter \"2\" For Card\t"))
    total = ShowBill() #Save the total bill in the varaible
    if(choice == 1):
        Payment = int(input("Enter the payment for bill\t"))
        if(Payment == total): #Payment and Total equal show nothing left
            print("Thanks for Coming and Your Bill is Cleared")
        elif(Payment > total):#Payment > Total equal show  left
            left = Payment - total
            print(f"Thanks for Coming and Your Bill is Cleared and your extra money \"{left}\" and Receive it")
        else:
            print("Your Bill is not cleared")
    elif(choice == 2):
        cardNo = int(input("Enter the card number\t"))# --> Detail About Card
        Payment = int(input("Enter the payment for bill\t")) #--> Enter the payment of your order
        if(Payment == total):
            print("Thanks for Coming and Your Bill is Cleared")
        else:
            print("Your Bill is not cleared")
    else:
        print("Plz Chose Correct option")            

print("-----------------------------------------------------------------------")
print("----------------------------Welcome In---------------------------------")
print("---------------------------Sheikh Grossary ----------------------------")
print("----------------------------Store(SGS)---------------------------------")
print("-----------------------------------------------------------------------")

print("\n\n-----------------------------------------------------------------------") 
menuList = {"Egg":15 ,"Bread":13  ,"ColdDrink":16,"Sugar":23,"Flour":24 } 
priceList = {"Egg":100 ,"Bread":130  ,"ColdDrink":600,"Sugar":130,"Flour":180 }
billList = {}
bill = []
Customer() #-->Calling customer Function
menu = int(input("\nPress \"1\" For Open Menu\t"))
Menu(menu) #--> Calling menu Function  
Order() #Calling Order Function