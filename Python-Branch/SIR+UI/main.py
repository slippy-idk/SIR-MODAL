# Imports
import customtkinter
from tkinter import messagebox
import tkinter as tk
from matplotlib import pyplot as plt

import os
import csv
from pathlib import Path
import pandas as pd

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
day = 1

DS = 0
DI = 0
DR = 0

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
        
        totalPopulation = susceptible + infected + recovered
        
        if(contactRate > 1.0 or recoveryRate > 1.0):
            return messagebox.showerror("Error!", "Please make sure that you only enter an infected per day and a recovery per day lower than 1.0")

        file = Path("./Data.csv")
        if(file.exists()):
            with open('Data.csv', 'w') as previousFile:
                previousFile.close()
        else:
            with open('Data.csv', "x") as createdFile:
                createdFile.close()
        
        loop = True
        writerVal = 0
        while(loop == True):
            DSVar = -(contactRate * susceptible * infected) / totalPopulation
            DIVar = (contactRate * susceptible * infected) / totalPopulation - recoveryRate * infected
                
            susceptible = susceptible + DSVar
            infected = infected + DIVar
            recovered = recovered + DRVar

            with open('Data.csv', 'a') as csvFile:
                fieldName = ['Day', 'Susceptible', 'Infected', 'Recovered']
                writer = csv.DictWriter(csvFile, fieldnames=fieldName)

                if(writerVal < 1):
                    writer.writeheader()
                else:
                    pass 

                writer.writerow({'Day': currentDayVar, 'Susceptible': susceptible, 'Infected': infected, 'Recovered': recovered})
                csvFile.close()
    
            if(currentDayVar == maxDays):
                loop = False
                break

            currentDayVar = currentDayVar + 1
            writerVal = writerVal + 1
        
        data = pd.read_csv('Data.csv')

        # Basic Functional Graph
        plt.title('Generated SIR Data')
        plt.plot(data['Susceptible'], color='blue')
        plt.plot(data['Infected'], color='red')
        plt.plot(data['Recovered'], color='green')
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
