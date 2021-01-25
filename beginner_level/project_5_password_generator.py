#Password Generator Project
import random
lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator App!")
nr_up_letters = int(input("How many uppercase letters would you like in your password?\n"))
nr_lw_letters = int(input("How many lowercase letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level
easy_password = ""

for char in range(1, nr_lw_letters + 1):
    easy_password += random.choice(lower_case_letters)

for char in range(1, nr_up_letters + 1):
    easy_password += random.choice(upper_case_letters)

for char in range(1, nr_symbols + 1):
    easy_password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    easy_password += random.choice(numbers)

print("Your easy password is: "+easy_password)

#Hard Level
password_list = []

for char in range(1, nr_lw_letters + 1):
  password_list.append(random.choice(lower_case_letters))

for char in range(1, nr_up_letters + 1):
  password_list.append(random.choice(upper_case_letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)


hard_password = ""
for char in password_list:
  hard_password += char

print(f"Your hard password is: {hard_password}")