# Imports
import customtkinter
from tkinter import messagebox
import json

# Theme Setting
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Basic Setup
root = customtkinter.CTk()
root.title("Sir Model/Login")
root.geometry("500x350")
check = customtkinter.IntVar()

# Setup an account
def Setup(U, P):
    getVar = check.get()

    if(getVar == 0):
        return messagebox.showerror("Missing Something!", "Please accept the terms and conditions!")
    
    with open('logininfo.json', 'w') as user_file:
        input_Username = Username.get()
        input_Password = Password.get()
        print(input_Username, input_Password)
        
    user_file.close()

    return messagebox.showinfo("Completed", "You have been added to the login system.")

# Username + Password Check
def Login(U, P):
    getVar = check.get()
    
    if(getVar == 0):
        return messagebox.showerror("Missing Something!", "Please accept the terms and conditions!")
    
    with open('logininfo.json', 'r') as user_file:
        parsed_json = json.load(user_file)
        Username_List = parsed_json['Usernames']
        Password_List = parsed_json['Passwords']
    user_file.close()

    if(Username in Username_List and Password in Password_List):
        print("Found.") 
    else:
        return messagebox.showerror("Oh no!", "Can't find your inputed data!")
        


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login Screen")
label.pack(pady=12, padx=10)

Username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
Username.pack(pady=12, padx=10)

Password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
Password.pack(pady=12, padx=10)

login_Button = customtkinter.CTkButton(master=frame, text="Login", command=lambda: Login(Username, Password))
login_Button.pack(pady=12, padx=10)

signup_Button = customtkinter.CTkButton(master=frame, text="Signup", command=lambda: Setup(Username, Password))
signup_Button.pack(pady=12, padx=10)

terms_Checkbox = customtkinter.CTkCheckBox(master=frame, text="I agree to the terms and conditions of use", variable=check)
terms_Checkbox.pack(pady=12, padx=10)

root.mainloop()