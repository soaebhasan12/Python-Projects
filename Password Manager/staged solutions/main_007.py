from tkinter import *
from tkinter import messagebox
# import random
from random import choice, randint, shuffle
import pyperclip

# Challenge-01 : Working with images and Setting up the Canvas.

# Challenge-02: Use grid() and columnspan to Complete the User Interface (UI).

# Challenge-03: Challenge Data to File.
        # 1. create a function called() save().
        # 2. Write to the data inside the entries to a data.txt file when the Add button is clicked.
        # 3. Each website, emailand password combination should be on a new line inside the file.
        # 4. All fields need to be cleared after Add button is pressed

# Lecture 006:  Dialog Boxes and Pop-Ups in Tkinter.
# Challenge-04: Do not save thedata and show the pop up if the website or password fields were left empty.

# Lecture 007: Generate a Password & Copy it to the Clipboard.
# Challenge-04: Change the existing for loops to use Python List Comprehension instead.
              # Remember to combine the results so that you can shuffle them to create a password.









# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # nr_letters = random.randint(8, 10)
        # nr_symbols = random.randint(2, 4)
        # nr_numbers = random.randint(2, 4)

        password_list = []

        # for char in range(nr_letters):
        #   password_list.append(random.choice(letters))
        password_letters = [choice(letters) for _ in range(randint(8, 10))]


        # for char in range(nr_symbols):
        #   password_list += random.choice(symbols)
        password_numbers = [choice(symbols) for _ in range(randint(2, 4))]


        # for char in range(nr_numbers):
        #   password_list += random.choice(numbers)
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]


        password_list = password_letters + password_numbers + password_numbers
        shuffle(password_list)

        password = "".join(password_list)

        # password = ""
        # for char in password_list:
        #   password += char

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
logo_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/29 - Building a Password Manager GUI App with Tkinter/Coding Exercise/logo.png")           

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