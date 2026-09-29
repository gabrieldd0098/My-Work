from tkinter import *
from tkinter import messagebox
import secrets
import string
import pyperclip
import json

#PASSWORD GENERATOR ------------------------------- #
def generate_password(min_length=10, max_length=20):
    length = secrets.randbelow(max_length - min_length + 1) + min_length

    pwd = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    all_chars = string.ascii_letters + string.digits + string.punctuation
    pwd += [secrets.choice(all_chars) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(pwd)

    pwd_new = "".join(pwd)
    password_entry.delete(first=0, last=END) #to avoid accumulating
    password_entry.insert(index=0, string=pwd_new)
    pyperclip.copy(pwd_new) #insert and copy to clipboard

#SAVE & SEARCH PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Email": email,
            "Password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="E R R O R", message="Please enter all required information!")
    else:
        # is_ok = messagebox.askokcancel(title=f"Website: {website}", message=f"This is what you have entered: \nEmail:"
        #                                                         f" {email}\nPassword: {password}\nIs it OK To Save?")

        # if is_ok:
            try: #TEEF
                with open(file="precious.json", mode="r") as data_file:
                    # data_file.write(f"WEBSITE: {website}\nEMAIL: {email}\nPASSWORD: {password}\n----------------\n")
                    data = json.load(data_file) #s1 read old data
            except FileNotFoundError:
                with open(file="precious.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data) #s2 updating old data
                with open(file="precious.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4) #s3 save new data
            finally:
                website_entry.delete(first=0, last=END)
                password_entry.delete(first=0, last=END)

def search():
    website = website_entry.get()
    try:
        with open(file="precious.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="E R R O R", message="Data not found!")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\nPASSWORD COPIED TO CLIPBOARD")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="E R R O R", message=f"Details for {website} do not exist!")

#UI SETUP ------------------------------- #
window = Tk()
window.title("[-PWD MGR-]")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="E-Mail/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(index=0, string="katedesalle@zmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#buttons
gen_pass_button = Button(text= "Generate Password", command=generate_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width= 13, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
