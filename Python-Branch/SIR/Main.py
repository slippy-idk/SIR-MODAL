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

# Variables 
pop = 0
ST = 0
TI = 0
TR = 0
recRate = 0

day = 0

# Functions
def generateData(S, I, R, varST, currentDay, simulationMax, varInfectionRate, varPop, varTI, varTR, varRecRate, varInfectionLength):
    try:
        susceptible = int(S.get())
        infected = int(I.get())
        recovered = int(R.get())
        simulationMaxInt = int(simulationMax.get())
        infectionRateInt = int(varInfectionRate.get())
        infectionLengthInt = int(varInfectionLength.get())
    
    except(ValueError):
        messagebox.showerror("Error", "Please make sure that you only enter numbers!")

    
    if(simulationMax == 0):
        messagebox.showerror("Error", "Please make sure that you simulate at least 1 day.")
    
    while(currentDay < simulationMaxInt):
        varPop = susceptible + infected + recovered
        varST = infectionRateInt * susceptible * infected / varPop
        varTI = infectionRateInt * susceptible * infected / varPop
        varRecRate = 1.0 / infectionLengthInt

        varTR = varRecRate * infected
        susceptible = susceptible + varST 
        infected = infected + varTI 
        recovered = recovered + varTR

        # print("Current susceptible: "+str(susceptible))
        # print("Current infected: "+str(infected))
        # print("Current recovered: "+str(recovered))

        currentDay = currentDay + 1 

        if(currentDay == simulationMax):
            break # I will change this to make a graph or something, I'm not sure.
    
    # print("Done.")

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

    infectionRateBox = customtkinter.CTkEntry(master=frame, placeholder_text="Infection rate")
    infectionRateBox.pack(pady=12, padx=10)

    infectionLengthBox = customtkinter.CTkEntry(master=frame, placeholder_text="Infection length")
    infectionLengthBox.pack(pady=12, padx=10)
    
    totalSimulationBox = customtkinter.CTkEntry(master=frame, placeholder_text="Total simulation time")
    totalSimulationBox.pack(pady=12, padx=10)

    runButton = customtkinter.CTkButton(master=frame, text="Run", command=lambda: generateData(susceptibleBox, infectedBox, recoveredBox, ST, day, totalSimulationBox, infectionRateBox, pop, TI, TR, recRate, infectionLengthBox))
    runButton.pack(pady=20, padx=10)

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
