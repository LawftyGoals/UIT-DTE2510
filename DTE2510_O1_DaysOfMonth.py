
whatYear = int(input("Velg et årstall: "))



if((whatYear % 4 == 0 and whatYear % 100 != 0) or (whatYear % 400 == 0)):
    print("Det er 29 dager i Februar", str(whatYear) + ". Året er et skuddår.")
else:
    print("Det er 28 dager i Februar", str(whatYear) + ". Året er ikke et skuddår.")


