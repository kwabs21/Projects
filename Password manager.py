from tkinter import *
from tkinter import messagebox
from random import  randint, shuffle, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters) ]
    password_symbols = [choice(symbols) for _ in range(nr_symbols) ]
    password_numbers = [choice(numbers) for _ in range(nr_numbers) ]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    # print(f"Your password is: {password}")

    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_get = web_entry.get()
    pass_get = pass_entry.get()
    em_get = em_entry.get()

    if len(web_get)==0 or len(pass_get)==0 or len(em_get)==0:
        messagebox.showinfo(title="Ooops", message="Do not leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=web_get, message=f"These are the details entered: \n Email: {em_get}\n"
                                                              f" Password: {pass_get}\n. Is it okay to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{web_get} | {em_get} | {pass_get}\n")
                web_entry.delete(0,END)
                pass_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password= Label(text="Password:")
password.grid(column=0, row=3)

# Entrys
web_entry = Entry(width=35)
web_entry.grid(column=1,row=1,columnspan=2)
web_entry.focus()

em_entry = Entry(width=35)
em_entry.grid(column=1, row=2,columnspan=2)
em_entry.insert(0,"fromescape@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

# Buttons
gen = Button(text="Generate Password", command=generate_password)
gen.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()