day = 1
S = 80
I = 20
R = 0
pop = 100

ST = 0

TI = 0

TR = 0

inf_rate = 2
inf_length = 4

rec_rate = 1.0 / inf_length



def sus():
    global S
    global ST
    ST = -inf_rate*S*I/ pop
    print(ST)

def inf():
    global I
    global TI
    TI = inf_rate*S*I/ pop
    print(TI)

def rec():
    global R
    global TR
    TR = rec_rate * I
    print(TR)


def change():
    global TR
    global TI
    global ST
    global S
    global I
    global R
    S = S + ST
    print("Susetible = " + str(S))

sus()
change()

