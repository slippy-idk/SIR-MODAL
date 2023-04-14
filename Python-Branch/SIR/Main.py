###warning do not touch anything to do with the calculation lesy you know what your are doing
# as touching one small detail of the calculation can make it scitificly invalid and can ruin other parts of the calculation
# 

sim_day = int(input("please enter the amount of days you wish to simulate"))  # the ammount of days simmulated
days = 1

##Warning the two below varibles must be worked as a decimle point or be converted as working with whole numbers makes the program volotile####
contact_rate = float(input("please enter the amount of people are infected per day in a decimle point "))
Rec_rate = float(input("please enter the mean recover rate in  decimal point"))

S = int(input("please enter the amount of sustebile population")) # the susetible population

I = int(input("please enter the amount of people inffected on day 1")) # the innfected population

R = 0 # the recovetred population


N = S + I + R # the total population

def SIR(): # works out change of the variables according to the SIR model
    global DS
    global DI
    global DR
    DS =  -(contact_rate * S * I) / N
    DI = (contact_rate * S * I ) / N - Rec_rate * I
    DR = Rec_rate * I
    Calc()

def Calc(): # works out the calcuklation and changes of varibles based of the SIR function's calculations
    global S
    global I
    global R 
    S = S + DS
    I = I + DI
    R = R + DR
    print("s = " + str(S))
    print("I = " + str(I))
    print("r = " + str(R))
    day()

def day(): #works out the days and wether the simulation should run to the end or it should re run through the calculations again
    global days
    if days > sim_day:
        print("program finished")
    else:
        days = days + 1
        print(days)
        SIR()

print("day = " + str(days))
SIR()

