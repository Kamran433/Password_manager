import tkinter
from tkinter import messagebox
import random
# --------------------------Generator-------------------------
def passbutton():
    pspace.delete(0, len(pspace.get()))
    non_capitals = "abcdefghijklmnopqrstuvwxyz"
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!@#¤%&/()?"
    npass = ""
    password =random.choices(non_capitals, k=3) + random.choices(capitals,k=3) + random.choices(numbers, k=3) + random.choices(symbols, k=3)
    random.shuffle(password)
    for i in password:
        npass+=i
    pspace.insert(0, npass)
    messagebox.showinfo(title="Password", message="A new password was generated")
# ------------------------Password-Saving---------------------
def addbutton():
    if (space1.get() == "" or space2.get() == "" or pspace.get() == ""):
        messagebox.showerror(title="Error", message="Please make sure no fields are left empty")
    else:
        m = messagebox.askokcancel(title="Confirmation", message=f"You entered \nwebsite : {space1.get()}\nEmail : {space2.get()}\nPassword : {pspace.get()}\nDo you want to save this information?")
        if(m):
           f = open("info.txt", "a")
           f.write(f"{space1.get()} | {space2.get()} | {pspace.get()}\n")
           space1.delete(0, len(space1.get()))
           pspace.delete(0, len(pspace.get()))
           messagebox.showinfo(title="deletion",message="press OK to clear entries")
           f.close()
# ------------------------------UI----------------------------
window=tkinter.Tk()
window.title("Password-Manager")
window.minsize(height=400,width=450)
imageshow = tkinter.PhotoImage(file="password.png")
canvas=tkinter.Canvas(height=200,width=200)
canvas.create_image(100,100,image = imageshow)
canvas.grid(row=0,column=1,padx=60,pady=20,sticky="W")
website = tkinter.Label(text="Website:")
website.grid(row=1,column=0)
space1 = tkinter.Entry(width=41)
space1.grid(row=1,column=1,sticky="W",padx=20)
space1.focus()
userid=tkinter.Label(text="Email/Username:")
userid.grid(row=2,column=0)
space2=tkinter.Entry(width=41)
space2.grid(row=2,column=1,sticky="W",padx=20)
space2.insert(0,"kamran1243434@gmail.com")
plabel=tkinter.Label(text="Password:")
plabel.grid(row=3,column=0,columnspan=1)
pspace=tkinter.Entry(width=20)
pspace.grid(row=3,column=1,sticky="W",padx=20)
pbutton=tkinter.Button(text="Generate Password",command=passbutton)
pbutton.grid(row=3,column=1,sticky="E",padx=20)
add=tkinter.Button(text="Add",command=addbutton,width=39)
add.grid(row=4,column=1,sticky="W",padx=20)
window.mainloop()
