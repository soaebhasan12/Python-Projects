from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Challenge-01: Working with images and Setting up the Canvas.

window = Tk()
window.title("Passoword Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=5, highlightbackground="black")
logo_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/29 - Building a Password Manager GUI App with Tkinter/Coding Exercise/logo.png")

# canvas.create_image(image=logo_img)
canvas.create_image(100, 100, image=logo_img)

canvas.pack()

window.mainloop()