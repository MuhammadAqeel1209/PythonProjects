# --> 👇👇👇 All Libiraries import
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root = Tk()
root.title("Untitled Notepad") # --> tittle
root.wm_iconbitmap("NotePad.ico") # --> icons
root.geometry("644x788") # --> Widht and height

# Fucntions 
def NewFile(): # --> Craeting a new blank file 
    global file
    root.title("Untitled Notepad")
    file = None
    TextArea.delete(1.0,END)

def OpenFile(): # --> open a file 
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad") # Set the title 
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
 

def SaveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad") # Set the title 
            tmsg.showinfo("Save","Your File is save")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def QuitApp():
    root.destroy()

def Cut():
    TextArea.event_generate(("<<Cut>>")) # --> Automatically Handle Cut Function 

def Copy():
    TextArea.event_generate(("<<Copy>")) # --> Automatically Handle Copy Function 

def Paste():
    TextArea.event_generate(("<<Paste>>")) # --> Automatically Handle Paste Function 

def About():
    tmsg.showinfo("Note Pad","Note Pad By Muhamad Aqeel")



# --> Text Area
TextArea = Text(root,font="lucida 12")
file = None
TextArea.pack(expand=True,fill=BOTH)

# Add --> Scroll Bar 
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
TextArea.config(yscrollcommand = Scroll.set)
Scroll.config(command=TextArea.yview)


# --> Lets Create Menu bar
Menubar = Menu(root)
# --> File Menu Start
fileMenu = Menu(Menubar,tearoff=0)

# --> To Open the new File
fileMenu.add_command(label="New",command=NewFile)

# --> To Open the existing file 
fileMenu.add_command(label="Open",command=OpenFile)

# --> To Save a File
fileMenu.add_command(label="Save",command=SaveFile)
fileMenu.add_separator()

# --> Exit Function 
fileMenu.add_command(label="Exit",command=QuitApp)

Menubar.add_cascade(label="File",menu=fileMenu)
# --> File Menu End

# --> Edit Menu Start
editMenu = Menu(Menubar,tearoff=0)
editMenu.add_command(label="Cut",command=Cut)
editMenu.add_command(label="Copy",command=Copy)
editMenu.add_command(label="Paste",command=Paste)
Menubar.add_cascade(label="Edit",menu=editMenu)
# --> Edit Menu End

# --> Help Menu Start
helpmenu = Menu(Menubar,tearoff=0)
helpmenu.add_command(label="About My NotePad",command=About)
Menubar.add_cascade(label="Help",menu=helpmenu)

# --> Help Menu End

root.config(menu=Menubar)


root.mainloop()