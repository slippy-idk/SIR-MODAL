import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Sir Model/Login")
root.geometry("500x350")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login Screen")
label.pack(pady=12, padx=10)

Username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
Username.pack(pady=12, padx=10)
Password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
Password.pack(pady=12, padx=10)

login_Button = customtkinter.CTkButton(master=frame, text="Login")
login_Button.pack(pady=12, padx=10)

signup_Button = customtkinter.CTkButton(master=frame, text="Signup")
signup_Button.pack(pady=12, padx=10)

terms_Checkbox = customtkinter.CTkCheckBox(master=frame, text="I agree to the terms and conditions of use")
terms_Checkbox.pack(pady=12, padx=10)

root.mainloop()