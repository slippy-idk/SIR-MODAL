# Imports
import customtkinter
from tkinter import messagebox
import tkinter as tk
from matplotlib import pyplot as plt
import os

# Theme Setting
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Directory Change
os.chdir('./Python-Branch/SIR+UI')

# Basic Setup
root = customtkinter.CTk()
root.title("Sir Model/Login")
root.geometry("500x350")
check = customtkinter.IntVar()

# Variables 
day = 1 # Setting day

DS = 0 #
DI = 0 # Setting of the formula variables, they are equivalent to the globalisation, just without the key word.
DR = 0 #

# Functions
def generateData(S, I, R, DSVar, DIVar, DRVar, currentDayVar, maxDayVar, contactRateVar, recoveryRateVar):
    try:
        # This is grabbing user input, and converting it into the correct format.
        susceptible = int(S.get())
        infected = int(I.get())
        recovered = int(R.get())
        maxDays = int(maxDayVar.get())

        contactRate = float(contactRateVar.get())
        recoveryRate = float(recoveryRateVar.get())
        loop = False
        
        totalPopulation = susceptible + infected + recovered # Calculating the total population, equal to your N value.

        # DSVAR, DIVAR, DRVAR are all equal to the current DS, DI, DR values, which are currently nothing.
        
        if(contactRate > 1.0 or recoveryRate > 1.0):
            return messagebox.showerror("Error!", "Please make sure that you only enter an infected per day and a recovery per day lower than 1.0")
        
        # currentDayVar is equal to the day, and maxDays is equal to the max day that the user inputed
        # While the current day is less than the max day, we will continually complete this

        loop = True
        while(loop == True):
            DSVar = -(contactRate * susceptible * infected) / totalPopulation # The original: -(contact_rate * S * I) / N
            DIVar = (contactRate * susceptible * infected) / totalPopulation - recoveryRate * infected # The original: (contact_rate * S * I ) / N - Rec_rate * I
            DRVar = recoveryRate * infected # The original: DR = Rec_rate * I
                
            susceptible = susceptible + DSVar # The original: S = S + DS
            infected = infected + DIVar # The original: I = I + DI 
            recovered = recovered + DRVar # The original: R = R + DR
                
            # print("==== "+str(currentDayVar)+" ====")
            # print("S: "+str(susceptible))
            # print("I: "+str(infected))
            # print("R: "+str(recovered))
    
            if(currentDayVar == maxDays):
                loop = False
                break

            currentDayVar = currentDayVar + 1

        # Basic Functional Graph
        x = [5, 4, 3, 3, 2, 8]
        y = [5, 1, 3, 2, 2, 8]
        z = [1, 1, 5, 2, 2, 3]
        plt.title('Generated SIR Data')
        plt.plot(x, color='red')
        plt.plot(y, color='blue')
        plt.plot(z, color='purple')
        plt.show()

    except(ValueError):
        return messagebox.showerror("Error", "Please make sure that you only enter numbers and decimals (where applicable) and that all boxes are filled!")

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
    userModelUI_window.geometry("600x600")

    # Border setting
    frame = customtkinter.CTkFrame(master=userModelUI_window)
    frame.pack(pady=36, padx=30, fill="both", expand=True)

    # Lable setting
    uilabel = customtkinter.CTkLabel(master=frame, text="Model Menu")
    uilabel.pack(pady=12, padx=10)

    uilabelWarning = customtkinter.CTkLabel(master=frame, text="Infected per day and recovered per day = 0.X (format)")
    uilabelWarning.pack(pady=12, padx=10)

    # Box Setting
    susceptibleBox = customtkinter.CTkEntry(master=frame, placeholder_text="Susceptible")
    susceptibleBox.pack(pady=12, padx=10) # Taking in total susceptible.

    infectedBox = customtkinter.CTkEntry(master=frame, placeholder_text="Infected")
    infectedBox.pack(pady=12, padx=10) # Taking in total infected.

    recoveredBox = customtkinter.CTkEntry(master=frame, placeholder_text="Recovered")
    recoveredBox.pack(pady=12, padx=10) # Taking in total recovered.

    simulationDayBox = customtkinter.CTkEntry(master=frame, placeholder_text="Total Days")
    simulationDayBox.pack(pady=12, padx=10) # Taking in the total amount of simulated days.

    contactRateBox = customtkinter.CTkEntry(master=frame, placeholder_text="Infected per day")
    contactRateBox.pack(pady=12, padx=10) # Taking in the total contact rate.

    recoveryRateBox = customtkinter.CTkEntry(master=frame, placeholder_text="Recover per day")
    recoveryRateBox.pack(pady=12, padx=10) # Taking in the total recovery rate.
    
    runButton = customtkinter.CTkButton(master=frame, text="Run", command=lambda: generateData(susceptibleBox, infectedBox, recoveredBox, DS, DI, DR, day, simulationDayBox, contactRateBox, recoveryRateBox))
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
