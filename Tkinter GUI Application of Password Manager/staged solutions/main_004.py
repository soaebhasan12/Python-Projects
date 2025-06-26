from tkinter import *

# Challenge-01: Working with images and Setting up the Canvas.

# Challenge-02: Use grid() and columnspan to Complete the User Interface (UI).

# Challenge-03: Challenge Data to File.
        # 1. create a function called() save().
        # 2. Write to the data inside the entries to a data.txt file when the Add button is clicked.
        # 3. Each website, emailand password combination should be on a new line inside the file.
        # 4. All fields need to be cleared after Add button is pressed

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()    
    password = password_entry.get()

    with open("data_004.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #




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
website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "soaebhasan04@gmail.com")
password_entry = Entry(width=27)
password_entry.grid(column=1, row=3, columnspan=1)



# Button
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()                                   # Challenge-01