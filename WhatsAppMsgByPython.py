#Question --> 👉👉👉 Send the msg in WhatsApp to anyone using python infnite time
#import all libiraries 👇👇👇
import random
import pyautogui as pg
import time 

name = ('Ali','Ahmed','Aqeel','Ehtsham','Faran')
time.sleep(1)

for i in range(100):
    namemsg = random.choice(name)
    pg.write("Name is "+namemsg)
    pg.press('enter')

#Run the progarm then immedaitely cursor move on the chat where you send the msg    