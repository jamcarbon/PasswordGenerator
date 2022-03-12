# version 0.1

import random
from tkinter import *
import pyperclip

OPTIONS = [
    "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
# How many characters you want on the password

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$.=+()"
# characters to use on the auto-generated password

window = Tk()

window.title('Password Generator')

window.geometry('550x270')


def generatepassword():
    passwordlenght = int(variable.get())
    generatepassword.password = "".join(random.sample(characters, passwordlenght))
    label.config(text=generatepassword.password)
    print(passwordlenght)  # print on the console how many characters used for the password
    print(generatepassword.password)  # print on the console the generated password


def copytoclipboard():
    pyperclip.copy(generatepassword.password)


variable = StringVar(window)
variable.set(OPTIONS[4])  # default password length on main screen

label1 = Label(window, text="Password Length:")
label1.pack(padx=15)

list1 = OptionMenu(window, variable, *OPTIONS)
list1.pack(padx=20, pady=10)

generatebtn = Button(window, text="Click to Generate Password", command=generatepassword)
generatebtn.pack()

label = Label(window, text="")
label.pack(padx=200, pady=50)

copybtn = Button(window, text="Copy to Clipboard", command=copytoclipboard)
copybtn.pack()

window.mainloop()


