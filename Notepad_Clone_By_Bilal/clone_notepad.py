from tkinter import * 
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
import pyautogui as pg


root = Tk()
root.geometry('900x400')
root.minsize(width = 100,height = 100)
root.wm_iconbitmap("1.ico")
file = ""
if file == "":
    root.title("Untitled - Notepad")
def newfile():
        global file
        root.title("Untitled - Notepad")
        file = None
        textbox.delete(1.0,END)
def edit():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
                                                              ("Text Documents","*.txt*")])
    if file == "":
        file = None
    else:
         root.title(os.path.basename(file) + " - Notepad")
         textbox.delete(1.0, END)
         with open(file,'r') as f:
             read = f.read()
             textbox.insert(1.0,read)
             f.close()
             
def save():
    global file
    file = asksaveasfilename(initialfile="Untitled.txt",defaultextension = ".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt*")])
    if file == "":
        file =  None
    else:
        with open(file , 'w')as f:
            write = f.write(textbox.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
def saveas():
      global file
      file = asksaveasfilename(initialfile="Untitled.txt",defaultextension = ".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt*")])
      if file == "":
         file =  None
      else:
        with open(file , 'w')as f:
            write = f.write(textbox.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
def cut():
    textbox.event_generate(("<<Cut>>"))
def copy():
    textbox.event_generate(("<<Copy>>"))
def paste():
    textbox.event_generate(("<<Paste>>"))
    
def helps():
    # print("U+1F917")
    return tmsg.showinfo("Help","Go To Our Help Care Center For Any Type Of Help")
def rate():
    a = tmsg.askquestion("Was Your Experience Good?","Was Your Experience Good?")
    print(a)
    if a == "yes":
        msg = "Great : Please Rate Us On Play Store"  
        tmsg.showinfo("Experience",msg)   
    else:
        msg="What Went Wrong : Please Explain Us Breifly" 
        tmsg.showinfo("Experience",msg)   
def quitpad():
    root.destroy()
def undo():
    textbox.event_generate(("<<Undo>>"))
def redo():
    textbox.event_generate(("<<Redo>>"))



		# mark located string as red
		# textbox.tag_config('found', foreground ='green', background = 'yellow')
    

# mymenu = Menu(root)
# mymenu.add_command(label="File",command=files)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)

yourmenu= Menu(root)

subm1 = Menu(yourmenu,tearoff=0)
subm1.add_command(label="New",command=newfile)
subm1.add_command(label="Open",command=edit)
subm1.add_command(label="Save",command=save)
subm1.add_command(label="Save As",command=saveas)


yourmenu.add_cascade(label="File",menu=subm1)



subm2 = Menu(yourmenu,tearoff=0)

subm2.add_separator()

subm2.add_command(label="Cut",command=cut)
subm2.add_command(label="Copy",command=copy)
subm2.add_command(label="Paste",command=paste)
subm2.add_separator()

subm2.add_command(label="Undo",command=undo)
subm2.add_command(label="Redo",command=redo)
subm2.add_separator()

m4 = Menu(yourmenu,tearoff=0)
m4.add_command(label="Help",command=helps)
m4.add_command(label="Rate Us",command=rate)

exita = Menu(yourmenu,tearoff=0)
exita.add_command(label = "Exit",command=quitpad)

yourmenu.add_cascade(label="Edit",menu=subm2)
yourmenu.add_cascade(label="Help",menu=m4)
yourmenu.add_cascade(label = "More",menu=exita)
root.config(menu=yourmenu)
root.config(menu=yourmenu)
root.config(menu=yourmenu)
textbox = Text(root,font="Lucida_Console_Regular 20",undo=True)
file = None
textbox.pack(expand=True,fill=BOTH)
Scroll = Scrollbar(textbox)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=textbox.yview)
textbox.config(yscrollcommand=Scroll.set)
root.mainloop()
