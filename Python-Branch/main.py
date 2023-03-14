import customtkinter
from tkinter import messagebox
import json

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Sir Model/Login")
root.geometry("500x350")
check = customtkinter.IntVar()

def Login(U, P):
    getVar = check.get()
    
    if(getVar == 0):
        messagebox.showinfo("Missing Something!", "Please accept the terms and conditions!")
    
    with open('logininfo.json') as user_file:
        parsed_json = json.load(user_file)
        Username_List = parsed_json['Usernames']
    user_file.close()
        


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

signup_Button = customtkinter.CTkButton(master=frame, text="Signup")
signup_Button.pack(pady=12, padx=10)

terms_Checkbox = customtkinter.CTkCheckBox(master=frame, text="I agree to the terms and conditions of use", variable=check)
terms_Checkbox.pack(pady=12, padx=10)

root.mainloop()