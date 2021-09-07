import random

spillerTall = int(input("Velg et tall. 0 : Stein, 1 : Saks, 2: Papir: "))
dataTall = random.randint(0,2)

if(spillerTall == 0):
    if (dataTall == 0):
        print("Dataen velger Stein, UAVGJORT!")
    elif (dataTall == 1):
        print("Dataen velger Saks, Du Vinner!")
    elif (dataTall == 2):
        print("Dataen velger Papir, Du Taper!")
elif(spillerTall == 1):
    if (dataTall == 0):
        print("Dataen velger Stein, Du Taper!")
    elif (dataTall == 1):
        print("Dataen velger Saks, UAVGJORT!")
    elif (dataTall == 2):
        print("Dataen velger Papir, Du Vinner!")
elif(spillerTall == 2):
    if (dataTall == 0):
        print("Dataen velger Stein, Du Vinner!")
    elif (dataTall == 1):
        print("Dataen velger Saks, Du Taper!")
    elif (dataTall == 2):
        print("Dataen velger Papir, UAVGJORT!")
else:
    print("Ikke godtatt tall")
