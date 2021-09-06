
vekt = float(input("Skriv inn vekten din i kilogram: "))
hoyde = float(input("Skriv inn høyden din i meter: "))

bmiVerdi = vekt/pow(hoyde, 2)
bmiTolkning = ""

if( bmiVerdi < 18.5):
    bmiTolkning = "undervektig"
elif(bmiVerdi < 25.0):
    bmiTolkning = "normal vekt"
elif(bmiVerdi < 30.0):
    bmiTolkning = "overvektig"
else:
    bmiTolkning = "veldig overviktig"

print("Du har en BMI verdi på", round(bmiVerdi,2), "som betyr at du er", bmiTolkning + ".")
