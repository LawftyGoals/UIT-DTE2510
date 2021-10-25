import random

def in_motion (slots_nr: int, balls: int):
    slots = [0]*slots_nr

    for i in range (0, balls):
        path_string = ""
        path = 0
        
        for j in range (0, slots_nr):
            chance = random.randint(0,1)

            if chance == 0:
                path_string += "L"
            else:
                path +=1
                path_string += "R"
            
        slots[path-1] +=1
        
        print(path_string)

    return slots

# This could be made as it's own function. histogram_creation() function feks.
# Black - PIP makes sure code is formatted correctly.
# Added return statement to in_motion, this passes to slots in main(), then uses print_histogram function.
#
#

def print_histogram(slots: list):

    for ii in range(max(slots)+2, 0, -1):
        
        row = ""

        for jj in slots:

            if jj >= ii:

                row += "O"
            
            else:

                row += " "
        
        print(row)



def main():

    slots = in_motion(int(input("Skriv inn antall ønsker spor: ")), int(input("Skriv inn antall ønsket baller: ")))
    print_histogram(slots)
    


if __name__ == "__main__":
    main()