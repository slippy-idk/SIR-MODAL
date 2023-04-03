sim_day = int(input("please enter the amount of days you wish to simulate")
day = 1
S = int(input("please enter your susetible population"))
I = int(input("please neter your infected population"))
R = 0
pop = S + I + R

ST = 0 # need to declere the three variables below so they become global beforehand
#they all focous around the change of the modal pop for that group the next day 
TI = 0

TR = 0

inf_rate = int(input("please enter the amount of people a day the infected cause the infection to spread"))
inf_length = int(input("please enter the amount of days the infection lasts"))

rec_rate = 1.0 / inf_length



def sus(): # work out change of susetible pop
    global S
    global ST
    ST = -inf_rate*S*I/ pop
    inf()

def inf():
    global I
    global TI
    TI = inf_rate*S*I/ pop
    rec()

def rec():
    global R
    global TR
    TR = rec_rate * I
    change()


def change():
    global TR
    global TI
    global ST
    global S
    global I
    global day
    global R
    S = S + ST
    I = I + TI
    R = R + TR
    print("Susetible = " + str(S))
    print("Infected = " + str(I))
    print("Recovered = " + str(R))
    day = day + 1
    wam()

def test():
    print("a")

def wam():
    global day
    print(day)
    if day > sim_day:
        print("l")
    else:
        sus()
        
wam()
    
