import os
print("\n--------------------------------------Welcome in Seret Code Language--------------------------------------")
print("------------------------------------------------------------------------------------------------------------\n")
#----------FIRST ENTER YOUR NAME------------
myName = input("Enter your name:\t")
#----------ENTER YOUR FRIEND NAME------------
frndName = input("Enter your Friend name who decodes your msg:\t")
#------------FIRST ENTER THE MSG------------ 
msg = input("\nEnter your msg\t")
os.system("cls")
#-----------MSG CONVET TO LIST  ------------
msg_list = list(msg)

#1st Code The Message
def Coding(msg):
    #FIND THE LENGTH OF STRING
    if(len(msg_list) <= 3 ):
        #REVERSE THE LIST
        msg_list.reverse()
    else:
        test1 = "D"
        test2 = "S"
        #INSERT--> SOME STRING IN LIST WHERE YOU WANT
        msg_list.insert(0, test1)
        #APEND--> STORE THE SOME STRING IN THE LAST OF LIST
        msg_list.append(test2)
        #REVERSE THE LIST
        msg_list.reverse()

    #--------LIST CONVERT TO STRING--------
    finalMsg = "".join(msg_list)
    return finalMsg


#2nd Decode The Message
def Decoding(msg_list):
    #FIND THE LENGTH OF STRING
    if(len(msg_list) <= 3 ):
        #REVERSE THE LIST
        msg_list.reverse()
    else:
        #DELETE THE EXTRA STRING THAT IS INSERT FOR Coding
        del msg_list[0]
        #DELETE THE EXTRA STRING THAT IS APPEND FOR Coding
        del msg_list[-1]
        #REVERSE THE LIST
        msg_list.reverse()

    #--------LIST CONVERT TO STRING--------
    finalMsg = "".join(msg_list)
    #DISPLAY THE SECRET MSG
    print("\n---------------:\t--------")
    print( "Final Message is:\t",finalMsg)
    print("\n---------------:\t--------")


MyMsg = Coding(msg_list)
print("\n---------------------------:\t--------")
print("Your Coding Message is that:\t",MyMsg)
print("---------------------------:\t--------\n")
MyMsg_List = list(MyMsg)

partnerName = input("Enter Your Partner Name who decode your msg:\t")
if(partnerName == frndName):
    Decoding(MyMsg_List)
else:
    print("\nYou Cannot see the msg because this is a highly secure function")
    