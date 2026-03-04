from random import choice
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
from random import randint,shuffle,choice
def password_creator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    passsword_symbols=[choice(symbols) for _ in range (randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]


    password_list = password_numbers+password_letters+passsword_symbols




    shuffle(password_list)

    password="".join(password_list)
    #password = ""
    #for char in password_list:
     # password += char

    giris3.insert(0,password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    app=giris1.get()
    email=giris2.get()
    password=giris3.get()

    if email=="" :
        messagebox.showinfo(title="warn",message="do not leave empty email")
    elif password=="":
        messagebox.showinfo(title="warn",message="do not leave empty password")

    else:
        with open("aliko.txt",mode="a")as file:


            file.write(app+"  |  ")
            file.write(email+"  |  ")
            file.write(password+"\n")
            giris1.delete(0,END)
            giris2.delete(0,END)
            giris3.delete(0,END)




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")

window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
lock_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row=0)

label1=Label(text="Website:")
label1.grid(column=0,row=1 )
label2=Label(text="Email/Username:")
label2.grid(column=0,row=2)
label3=Label(text="Password:")
label3.grid(column=0,row=3)

giris1=Entry(width=42)
giris1.grid(column= 1,row=1 ,columnspan=2)
giris2=Entry(width=42)
giris2.insert(0,"ramazan0058.rc@gmail.com")
giris2.grid(column= 1,row=2 ,columnspan=2)
giris3=Entry(width=24)
giris3.grid(column= 1,row=3 )

button_password_generator=Button(text="Generate Password",command=password_creator)
button_password_generator.grid(column= 2,row=3 )
button_add=Button(text="Add",width=36,command=save)
button_add.grid(column=1 ,row=4, columnspan=2 )




window.mainloop()


