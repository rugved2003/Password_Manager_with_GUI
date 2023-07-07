from tkinter import*
from tkinter import messagebox
from random import random, choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_numbers+ password_symbols
    shuffle(password_list)
    pw = "".join(password_list)
    password_entry.insert(0,pw)

    pyperclip.copy(pw)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS",message="please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details enterd: \nEmail: {email}"
                               f'\nPassword: {password} \nIs it Ok to Save')
        if is_ok:
            with open('data.txt',"a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file='logo.png')
logo = canvas.create_image(100, 100, image=img)
canvas.grid(column=1,row=0)

#label
website_label=Label(text='Website:')
website_label.grid(column=0,row=1)
username = Label(text = 'Username:')
username.grid(column=0,row=2)
password_label= Label(text = 'Password:')
password_label.grid(column=0,row=3)

#entries
web_entry = Entry(width= 35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
username_entry = Entry(width= 35)
username_entry.grid(row=2, column=1,columnspan=2)
username_entry.insert(0, "rugved@gmail.com")
password_entry = Entry(width= 25)
password_entry.grid(column=1, row=3)


#buttons
generate_button = Button(text='Generate Password', command = generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text ='Add',width= 30,command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
