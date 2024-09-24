import tkinter as tk
from tkinter import messagebox
import os

CREDENTIALS_FILE = "credentials.txt"

def create_credentials_file():
    if not os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "w") as file:
            pass

def show_login_form():
    registration_frame.grid_forget()
    login_frame.grid(pady=20)

def show_registration_form():
    login_frame.grid_forget()
    registration_frame.grid(pady=20)

def login():
    username = entry_username_login.get()
    password = entry_password_login.get()
    
    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            if not line.strip():  # Skip empty lines
                continue
            
            try:
                stored_username, stored_password, _, _ = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    messagebox.showinfo("Login Successful", "Welcome!")
                    return
            except ValueError:
                continue  # Skip lines that don't have the expected format
            
    messagebox.showerror("Login Failed", "Invalid username or password")

def register():
    username = entry_username_reg.get()
    password = entry_password_reg.get()
    address = entry_address.get()
    contact = entry_contact.get()
    
    if username and password and address and contact:
        with open(CREDENTIALS_FILE, "a") as file:
            file.write(f"{username},{password},{address},{contact}\n")
        messagebox.showinfo("Registration Successful", "User registered successfully!")
        show_login_form()  # Show login form after successful registration
    else:
        messagebox.showerror("Registration Failed", "Please fill in all fields")

create_credentials_file()

root = tk.Tk()
root.title("User Authentication")
root.geometry("300x400")

# Registration Frame
registration_frame = tk.Frame(root)

label_username_reg = tk.Label(registration_frame, text="Username:")
label_username_reg.grid(row=0, pady=5)

entry_username_reg = tk.Entry(registration_frame)
entry_username_reg.grid(row=1, pady=5)

label_password_reg = tk.Label(registration_frame, text="Password:")
label_password_reg.grid(row=2, pady=5)

entry_password_reg = tk.Entry(registration_frame, show='*')
entry_password_reg.grid(row=3, pady=5)

label_address = tk.Label(registration_frame, text="Address:")
label_address.grid(row=4, pady=5)

entry_address = tk.Entry(registration_frame)
entry_address.grid(row=5, pady=5)

label_contact = tk.Label(registration_frame, text="Contact:")
label_contact.grid(row=6, pady=5)

entry_contact = tk.Entry(registration_frame)
entry_contact.grid(row=7, pady=5)

button_register = tk.Button(registration_frame, text="Register", command=register)
button_register.grid(row=8, pady=10)

button_switch_to_login = tk.Button(registration_frame, text="Already have an account? Login", command=show_login_form)
button_switch_to_login.grid(row=9, pady=5)

registration_frame.grid(pady=20)  # Show registration frame first

# Login Frame
login_frame = tk.Frame(root)

label_username_login = tk.Label(login_frame, text="Username:")
label_username_login.grid(row=0, pady=5)

entry_username_login = tk.Entry(login_frame)
entry_username_login.grid(row=1, pady=5)

label_password_login = tk.Label(login_frame, text="Password:")
label_password_login.grid(row=2, pady=5)

entry_password_login = tk.Entry(login_frame, show='*')
entry_password_login.grid(row=3, pady=5)

button_login = tk.Button(login_frame, text="Login", command=login)
button_login.grid(row=4, pady=10)

button_switch_to_registration = tk.Button(login_frame, text="Don't have an account? Register", command=show_registration_form)
button_switch_to_registration.grid(row=5, pady=5)

root.mainloop()






