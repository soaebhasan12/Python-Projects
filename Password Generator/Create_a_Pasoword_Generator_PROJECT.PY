# Project : Create a Pasoword Generator.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 's', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'S', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%','&', '*', '+']

print("Welcome to the PyPassword Generator!")

number_of_letters = int(input("How many letters would you like in your password ?\n"))
number_of_integers = int(input("How many Integers would you like in your password ?\n"))
number_of_symbols = int(input("How many symbols would you like in your password ?\n"))



# EASY level PASSWORD GENERATOR (easy to crack by hacker) :


# password = ""

# for char in range(1, number_of_letters + 1):
#     random_char = random.choice(letters)
#     password = password + random_char
    
    
# for char in range(1, number_of_integers + 1):
#     random_char = random.choice(numbers)
#     password = password + random_char
    
    
# for char in range(1, number_of_symbols + 1):
#     random_char = random.choice(symbols)
#     password = password + random_char
    
# print(password)






# Hard Level :-


password_list = []

for char in range(1, number_of_letters + 1):
    password_list.append(random.choice(letters))
    
    
for char in range(1, number_of_integers + 1):
    password_list.append(random.choice(numbers))
    
    
for char in range(1, number_of_symbols + 1):
    password_list.append(random.choice(symbols))
    
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password = password + char
print()
print(f"Your Password is: {password}")









