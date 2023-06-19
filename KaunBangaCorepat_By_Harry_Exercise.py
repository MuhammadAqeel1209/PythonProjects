#-----------------KAUN BANEGA CORERPATI-----------------
#-----------------QUESTIONS FOR SHOW    ----------------
questionInShows = [
    #-----------1ST QUESTION-----------
    ["0) Which Color of flag of Pakistan",
    "a)Red and Brown" ,              "b)Green and White",
    "c)Red And Green",              "d)Green and Yellow",2],

    #-----------2ND QUESTION-----------
    ["1) Which the national flower of Pakistan",
    "a)Rose" ,                       "     b)Jasmine",
    "c)Sun Flower",                "d)Tulip",2],
    
    #-----------3RD QUESTION-----------
    ["2) Which national animal of Pakistan",
    "a)Tiger" ,                        "   b)Markhor",
    "c)Elephant",                   "d)Lion",2],
    
    #-----------4TH QUESTION-----------
    ["3) Which is the captain of Pakistan cricket",
    "a)Rizwan" ,                        "b)Babar Azam",
    "c)Sarfraz",                      "d)Shadab",2],
    
    #-----------5TH QUESTION-----------
    ["4) Who was the first governal genral  of Pakistan",
    "a)Quaid-e-Azam" ,                  "  b)Allam Iqbal",
    "c)Sir Syed Ahmed",              "d)Fatima Jinnah",1],
    
    #-----------6TH QUESTION-----------
    ["5) Which Color of flag of Turkey",
    "a)Red " ,                            "b)Green ",
    "c)White",                         "d)Yellow",1],
    
    #-----------7TH QUESTION-----------
    ["6) Which is the biggest city of Pakistan",
    "a)Lahore" ,                       "b)Multan",
    "c)Gunjranwala",                "d)Karachi",4],
    
    #-----------8TH QUESTION-----------
    ["7) Which city of Pakistan have clock tower",
    "a)Faisalabad" ,                   "b)Lahore",
    "c)Gunjranwala",                 "d)Karachi",1],
    
    #-----------9TH QUESTION-----------
     ["8) Which city of Pakistan have Minar Pakistan",
    "a)Faisalabad" ,                   "b)Lahore",
    "c)Gunjranwala",                 "d)Karachi",2],
    
    #-----------10TH QUESTION-----------
     ["9) Which city of Pakistan have beach",
    "a)Faisalabad" ,                   "b)Lahore",
    "c)Gunjranwala",                 "d)Karachi",4],
    
    #-----------11TH QUESTION-----------
    ["10) Which city of Pakistan has heart of Pakistan",
    "a)Faisalabad" ,                   "b)Lahore",
    "c)Gunjranwala",                 "d)Karachi",2],
]
    
    #---------------LEVEL OF KAUN BANEGA COREPATI---------------
        # 0,   1,  2,   3,   4,    5,    6,    7,    8,     9,      10    
level = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,"Finish Game"]

#INITILIZE THE MONEY ZERO BEFORE START THE GAME
money = 0
#INITILIZE THE LIFE LINES BEFORE START THE GAME
amountLineLines = 3

print("\n--------------WELCOME IN KAUN BANEGA CROREPATI --------------")
print("--------------------------------------------------------------\n")
name = input("What is your Name Sir!:\t")

#LOOP FOR DISPLAY THE QUESTIONS ONE BY ONE
for i in range(0,len(questionInShows)):
    #QUESTION LIST ONE BY ONE INDEX IN ONE VARAIABLE QUESTION
        question = questionInShows[i]

        print("----------------------------------------------------------------")
        
        #DISPLAY THE LEVEL OF QUESTION AND ITS RUPEES
        print(f"\n{name} Sir --> Question For {level[i]}")
        #SHOW THE QUESTION
        print(f"{question[0]}")
        #SHOW THE FIRST OPTION                    #SHOW THE SECOND OPTION  
        print(f"{question[1]}\t\t"               f"{question[2]}")
        #SHOW THE THIRD OPTION                    #SHOW THE FORTH OPTION  
        print(f"{question[3]}\t\t"               f"{question[4]}")  
        
        #ASKING FOR TAKING LIFELINES OR NOT
        if(amountLineLines != 0):
            choice = int(input("\n\nEnter Your Choice \n1)For Taking LifeLines\n2) For No Taking LifLines\t"))
            if(choice == 1):#-->Check the choice condition and life lines
                print("\n-----------------------Welcome in the Life Lines Part-----------------------")
                print(f"\nLifeLines are {amountLineLines} in amount are available") #-->Msg Display
                #Taking Input about the Life lines
                lifeLines = int(input("Enter the your Choice for lifelines\n1)For Friends\n2)For Family\t"))
                if(lifeLines == 1):#-->Check Condition  whose life lines check
                    print("Call The Friend\n") #-->Call To The that Person 
                    amountLineLines = amountLineLines - 1 #-->Decrese the Lifelines 
                elif(lifeLines == 2):#-->Check Condition  whose life lines check
                    print("Call The Family\n")#-->Call To The that Person 
                    amountLineLines = amountLineLines - 1#-->Decrese the Lifelines
                else:
                    print("Choce Correct Option")        
        else:
            print(f"Thanks But {name} not wanted to take lifelines") 
        print(f"\nYou have left {amountLineLines} lifelines ") #-->Show The Left Amount of life lines
        # ASK USER TO ANSWER THAT QUESTIONS WHICH SHOW ON THE SCREEN
        reply = int(input("Enter the reply of question from 1 to 4-->\t"))       
        #CHECK THE ANSWER OF QUESTION
        if(reply == question[-1]): #IF USER ANSWER = CORRECT OPTION OF QUESTION
            #AFTER THE RIGHT ANSWER THET MSG DISPLAY
            print(f"Correct Answer\t {name} Sir won {level[i]} Rs")
            # IF LEVEL OF GAME = 4 
            #FIRST LEVEL CLEAR
            if(i == 4):
                #AND MONEY IS EQUAL TO 10000
                money = 10000
                print("1st Level Complete")
                print("\n------------------------------------------------------------------\n")
                ask = int(input("Enter the your choice \n1)For Play More\n2)For No More\t"))
                if(ask == 1):
                    print("Ok you Want to play More")
                elif(ask == 2):
                    print("Thanks For Playing The Game")
                    break
                else:
                    print("Choice The Correct Option")
                    break    
            # IF LEVEL OF GAME = 9 
            #NEXT  LEVEL CLEAR
            elif(i == 9):    
                 #AND MONEY IS EQUAL TO 320000 
                money =  320000   
        else:
            #OHTER WISE DISPLAY THAT MSG
            print("\nSir Your Answer is Wrong\nThanks For Playing The Game")
            #STOP THE LOOP
            break
print("\n-----------------------------------------------------")
#IF YOU PASSED FIRST LEVEL AND NEXT LEVEL THAT SHOW YOUR MONEY AND GIVE TO CONGRTULATION ON WINING
print(f"\n{name} Sir take money to your home after winning is {money} Rs")
#IF YOUR MONEY = 10000 FIRST LEVEL COMPLETE
if(money == 10000 ):
    print("1st Level complete")

#IF YOUR MONEY = 320000 FINAL LEVEL COMPLETE LEVEL COMPLETE    
elif(money == 320000):
    print("FINAL Level complete")

 #IF MONEY = 0 THEN NO LEVEL COMPLETE   
else:
    print("No Level complete")  
print("--------------Thanks For Coming --------------\n")              
