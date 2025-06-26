from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Challenge-01: Working with images and Setting up the Canvas.

# Challenge-02: Use grid() and columnspan to Complete the User Interface (UI).



window = Tk()                           # Challenge-01
window.title("Passoword Manager")       # Challenge-01
window.config(padx=50, pady=50)         # Challenge-01

canvas = Canvas(width=200, height=200)       # Challenge-01
logo_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/29 - Building a Password Manager GUI App with Tkinter/Coding Exercise/logo.png")          # Challenge-01

# canvas.create_image(image=logo_img)               # Challenge-01
canvas.create_image(100, 100, image=logo_img)       # Challenge-01
canvas.grid(column=1, row=0)


# Labels:
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)



# Button
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)


                                       # Challenge-01

window.mainloop()                                   # Challenge-01