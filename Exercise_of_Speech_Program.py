"""if you have not gtts Module 
1) You write pip install gtts on Cmd Prompt
2) After Installing you import the gtts Module"""
from gtts  import gTTS
import os

print("\n\n")
print("=====================================================================")
print("========================= Welcome to ================================")
print("========================= ShortsOuts ================================")
print("========================= to Students ===============================")
print("=====================================================================")

size = int(input("Enter the size of list\t"))  #👈-->Size Of List
namelist = []  #👈-->List

for i in range(size):
    i = input("Enter the name of student\t") #👈-->Input in the list
    namelist.append(i)

#--> File Handling here 👇👇👇
with open("Speech.txt","w") as file:
    file.write("ShortsOut to ")
    file.write(" ".join(namelist)) #👈-->convert list element into list one by one
    print("\n")
    

file = open("Speech.txt","r")   
text = file.read().replace("\n"," ")
    
language = "en" #👈--> Set The Language
output = gTTS(text = text,lang = language,slow = False) #👈--> Set The Text, Language and speed

output.save("outputFile.mp3")  #👈--> save the audio
print(f"Name of student who receives shortouts--> {text}")
file.close() #👈-->close the file
os.system("start outputFile.mp3") #👈--> Play the audio


