from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = user_name_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Empty Fields!")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# Search Button function
def search_button():
    try:
        web = website_entry.get()
        with open("data.json", "r") as file:
            websites = json.load(file)
            if web in websites:
                values = websites[web]
                messagebox.showinfo(title=f"{web}", message=f"Email: {values['email']}\nPassword: {values['password']}")
            else:
                raise ValueError("Website doesn't exist")
    except ValueError as e:
        messagebox.showerror(title="Error", message=e)
    finally:
        website_entry.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #
# Creating the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Creating the canvas
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

# Creating Website label
website_label = Label(text="Website")
website_label.grid(column=0, row=1)

# Creating Email/username label
user_name_label = Label(text="Email/Username")
user_name_label.grid(column=0, row=2)

# Password Label
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Website Entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

# Search Button
generate_button = Button(text="Search", width=11, command=search_button)
generate_button.grid(column=2, row=1)

# Email/username Entry
user_name_entry = Entry(width=35)
user_name_entry.grid(column=1, row=2, columnspan=2)
user_name_entry.insert(0, "khy23.kk@gmail.com")

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Generate Password Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()