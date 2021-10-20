
userInput = int(input("Velg tall: "))

resultat = ""

while userInput != 0:
    unit = userInput%2
    userInput = userInput//2
    resultat = str(unit)+ resultat

print("Den binære verdien er:", resultat)
