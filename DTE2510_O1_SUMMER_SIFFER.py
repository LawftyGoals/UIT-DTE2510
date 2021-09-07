numVal = int(input("Tast inn et 4 siffers tall mellom 0 og 1000: "))
summering = 0

summering = (numVal % 10) + ((numVal // 10) % 10) + ((numVal // 100) % 10) + ((numVal // 1000) % 10)

print("Det summerte tallet er:",summering)
