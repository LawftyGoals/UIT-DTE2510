
brukerTall = int(input("velg et 3 talls siffer: "))

reversering = (brukerTall%10)*100+((brukerTall//10)%10)*10+(brukerTall//100)

if (brukerTall > 999 or brukerTall > 99):
    if (brukerTall == reversering):
        print("Tallet",brukerTall,"er et palindrometall.")
    else:
        print("Tallet er ikke et palindrometall.")
else:
    print("Ugyldig tall.")
