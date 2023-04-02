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
    global susetible
    global suseptible
    global Innfected
    force_inf = Infectivity*Innfected
    force_inf = force_inf*pop
    force_inf = force_inf/pop
    force_inf = round(force_inf)
    print("current change of susetible pop -" + str(force_inf))
    Innfected = Innfected + force_inf
    susetible = susetible - force_inf
    print("the current innfected pop " + str(Innfected))
    
def amon():
    global Recovery
    global susetible
    global Innfected
    norm = Infectivity*Innfected
    norm = norm*pop
    norm = round(norm)
    force_rec = Recovery*Innfected
    force_rec = force_rec - norm
    print("change of reocovery " + str(force_rec))

amon()
    




