import string
import random
import getpass

# print(string.ascii_letters) # --> Upper case and lower case letter
# print(string.ascii_lowercase) # --> lower case letter
# print(string.ascii_uppercase) # --> Upper case letter
# print(string.digits) # --> Digits
# print(string.punctuation) # --> Pinctuation

s1 =string.ascii_lowercase
s2 =string.ascii_uppercase
s3 =string.digits
s4 =string.punctuation

def MakingPassword(s1,s2,s3,s4):
    length = int(input("Enter the password length\t")) # --> Input the length of PassWord
    save = []
    save.extend(list(s1))
    save.extend(list(s2))
    save.extend(list(s3))
    save.extend(list(s4))
    #print("Your Password is ",end="\t")
    return "".join(random.sample(save,length))

MakingPassword(s1,s2,s3,s4)


# --> 1st Method 👇👇👇
# random.shuffle(save)
# print("Your Password is ",end="\t")
# print("".join(save[0:length]))

# --> 2nd Method 👇👇👇
# print("Your Password is ",end="\t")
# print("".join(random.sample(save,length)))

# --> Exercise Solution Here 👇👇👇👇

# --> Varaiable 👇👇👇
# gmailAcc = ""
# gmailPass = ""
# twitterAcc = ""
# twiterPass = ""
# FbAcc = ""
# FbPass = ""
# instaAcc = ""
# instaPass = ""
# while(True):
#     choice = input("\n\nEnter the choice for making acoounts\n1)Gmail\n2)Twitter\n3)Facebook\n4)Instagram\n5)NoAccount\t")
#     if choice == "Gmail":
#         gmailAcc = input("Enter your account in the form \"name@gmail.com\"-->\t")
#         print("Password Automatically Generate ",end="\n") 
#         gmailPass = MakingPassword(s1,s2,s3,s4)
#     elif choice == "Twitter":    
#         twitterAcc = input("Enter your account \t")
#         print("Password Automatically Generate ",end="\n") 
#         twiterPass = MakingPassword(s1,s2,s3,s4)
#     elif choice == "Facebook":
#         FbAcc = input("Enter your account \t")
#         print("Password Automatically Generate ",end="\n") 
#         FbPass = MakingPassword(s1,s2,s3,s4)
#     elif choice == "Instagram":
#         instaAcc = input("Enter your account \t")
#         print("Password Automatically Generate",end="\n") 
#         instaPass = MakingPassword(s1,s2,s3,s4)
#     elif choice == "NoAccount":
#         print("Thanks For coming")
#         break
#     else:
#         print("Thanks For Making All Account")
#         break


# with open ("Account_Password.txt","a") as file:
#                                                                     #Here 👇👇👇 is tab Space
#     file.write(f"Gmail Account --> {gmailAcc} and Password --> {gmailPass}      Twitter Account --> {twitterAcc} and Password --> {twiterPass}")
#     file.write(f"   FaceBook Account --> {FbAcc} and Password --> {FbPass}      Instagram Account --> {instaAcc} and Password --> {instaPass}")

# with open("Account_Password.txt") as File:
#     print(File.readlines())

# https://docs.python.org/3/library/strins1 