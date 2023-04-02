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

# Functions
def generateData(S, I, R):
    try:
        # Variables for the formula, don't change what they equal to, they equal to user input.
        susceptible = int(S.get())
        infected = int(I.get())
        recovered = int(R.get())
    
    except(ValueError):
        messagebox.showerror("Error", "Please make sure that you only enter numbers!")
    
    # Add the simulation code here.
    # Make sure that the defined functions are not defined within this function, they should be defined outside the function.
    # If there's any issues, or problems with implementation, let me know by opening an issue and we can work on it together.


def closingSystem(R, U):
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        U.destroy()
        R.destroy()


def userModelUI(U):
    # Hides the login menu
    root.withdraw()

    # Create secondary (or popup) window
    userModelUI_window = tk.Toplevel()
    userModelUI_window.title(U.get()+'/Sir Model/Menu')
    userModelUI_window.geometry("500x500")

    # Border setting
    frame = customtkinter.CTkFrame(master=userModelUI_window)
    frame.pack(pady=36, padx=30, fill="both", expand=True)

    # Lable setting
    label = customtkinter.CTkLabel(master=frame, text="Model Menu")
    label.pack(pady=12, padx=10)

    # Box Setting
    susceptibleBox = customtkinter.CTkEntry(master=frame, placeholder_text="Susceptible")
    susceptibleBox.pack(pady=12, padx=10)

    infectedBox = customtkinter.CTkEntry(master=frame, placeholder_text="Infected")
    infectedBox.pack(pady=12, padx=10)

    recoveredBox = customtkinter.CTkEntry(master=frame, placeholder_text="Recovered")
    recoveredBox.pack(pady=12, padx=10)

    runButton = customtkinter.CTkButton(master=frame, text="Run", command=lambda: generateData(susceptibleBox, infectedBox, recoveredBox))
    runButton.pack(pady=30, padx=10)

    userModelUI_window.protocol("WM_DELETE_WINDOW", lambda:closingSystem(root, userModelUI_window))


# Setup an "account"
def Login(U):
    getVar = check.get()

    if (getVar == 0):
        return messagebox.showerror("Missing Something!", "Please accept the terms and conditions!")

    if(U.get() == None):
        return messagebox.showerror("Missing Something!", "Please enter a username!")
    
    userModelUI(Username)


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login Screen")
label.pack(pady=12, padx=10)

Username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
Username.pack(pady=12, padx=10)

login_Button = customtkinter.CTkButton(master=frame, text="Login", command=lambda: Login(Username))
login_Button.pack(pady=12, padx=10)


terms_Checkbox = customtkinter.CTkCheckBox(master=frame, text="I agree to the terms and conditions of use", variable=check)
terms_Checkbox.pack(pady=12, padx=10)

root.mainloop()
