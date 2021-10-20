import random

def in_motion (slotsNr: int, balls: int):
    slots = [0]*slotsNr

    for i in range (0, balls):
        pathString = ""
        path = 0
        
        for j in range (0, slotsNr):
            chance = random.randint(0,1)

            if chance == 0:
                pathString += "L"
            else:
                path +=1
                pathString += "R"
            
        slots[path] +=1
        
        print(pathString)

    for ii in range(max(slots)+2, 0, -1):
        
        row = ""

        for jj in slots:

            if jj >= ii:

                row += "O"
            
            else:

                row += " "
        
        print(row)



def main():
    in_motion(int(input("Skriv inn antall ønsker spor: ")), int(input("Skriv inn antall ønsket baller: ")))


if __name__ == "__main__":
    main()