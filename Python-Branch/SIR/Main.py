#variables relating to the virus itself 
Infectivity = int(input("Please eneter the innfectivity rate of the modal virus"))
Recovery = int(input("please enter the mean revery rate of a virus"))

#variables relating to the current states of the simnulated population
susetible = 1000
recovered = 0
Innfected = 1
susetible = susetible - Innfected  #might be redunent
pop = susetible + Innfected #this variable is the current population of the twon worked out may work out as might be redunent
day = 0  # the currfent day


#thease varibels are unused int he current versin but may be used lated for user simplicity
Rday = 1/Recovery
caseinf = Infectivity/Recovery

simdays = int(input("How many days would you like to simulate"))

def sussy(): #below is the function that simulates the infection of a day by shwing the change in suseptible 
    force_inf = Infectivity*Innfected
    force_inf = force_inf*pop
    force_inf = force_inf/pop
    force_inf = round(force_inf)
    print("current change of susetible pop -" + str(force_inf))
    susetible = susetible - force_inf
    print("current susetible pop is" + str(susetible))
    infection()

def infection(): #this is the calculatin that detimins the infectin change for that day
    force_rec = Infectivity*susetible*Innfected
    force_rec = force_rec/susetible
    force_rec = force_rec - Recovery
    force_rec = round(force_rec)
    print("the current innfected pop " + str(force_rec))
    recovery()


def recovery():
    force_rev = Recovery*Innfected
    force_rev = round(force_rev)
    print("The number of recoverd and immune pop is " + str(force_rev))
 

sussy()



