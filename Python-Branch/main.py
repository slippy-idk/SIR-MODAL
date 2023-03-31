# Imports
import customtkinter
from tkinter import messagebox
import tkinter as tk

# Theme Setting
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Basic Setup
root = customtkinter.CTk()
root.title("Sir Model/Login")
root.geometry("500x350")
check = customtkinter.IntVar()

def userModelUI():
    # Hides the login menu.
    root.withdraw()

    # Create secondary (or popup) window.
    userModelUI_window = tk.Toplevel()
    userModelUI_window.title(Username.get()+'/Sir Model/Menu')
    userModelUI_window.config(width=500, height=500)

    # Create a button to close (destroy) this window.
    button_close = customtkinter.CTkButton(
        userModelUI_window,
        text="Close window",
        command=userModelUI_window.destroy
    )
    button_close.place(x=250, y=250)


# Setup an "account"
def Login():
    getVar = check.get()

    if (getVar == 0):
        return messagebox.showerror("Missing Something!", "Please accept the terms and conditions!")

    if(Username.get() == None):
        return messagebox.showerror("Missing Something!", "Please enter a username!")
    
    userModelUI()



frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login Screen")
label.pack(pady=12, padx=10)

Username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
Username.pack(pady=12, padx=10)

login_Button = customtkinter.CTkButton(master=frame, text="Login", command=lambda: Login())
login_Button.pack(pady=12, padx=10)


terms_Checkbox = customtkinter.CTkCheckBox(master=frame, text="I agree to the terms and conditions of use", variable=check)
terms_Checkbox.pack(pady=12, padx=10)

root.mainloop()
