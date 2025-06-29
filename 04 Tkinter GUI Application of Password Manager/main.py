from tkinter import *
from tkinter import messagebox
# import random
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list = []

        password_letters = [choice(letters) for _ in range(randint(8, 10))]

        password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_numbers + password_numbers
        shuffle(password_list)

        password = "".join(password_list)

        password_entry.insert(0, password)

        pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_entry.get()    
    password = password_entry.get()


    if len(website) == 0 or len(password) == 0:
         messagebox.showinfo(title="Oops", message="Please make sureyou have not left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                        f"\nPassword: {password} \nIs is ok to save?")

        if is_ok:
                with open("data_007.txt", "a") as data_file:
                        data_file.write(f"{website} | {email} | {password}\n")
                        website_entry.delete(0, END)
                        password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #




window = Tk()                            
window.title("Passoword Manager")        
window.config(padx=50, pady=50)          

canvas = Canvas(width=200, height=200)        
logo_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/29 - Building a Password Manager GUI App with Tkinter/Coding Exercise/Python-Projects/Tkinter GUI Application of Password Manager/logo.png")           

# canvas.create_image(image=logo_img)                
canvas.create_image(100, 100, image=logo_img)        
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
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()                                    