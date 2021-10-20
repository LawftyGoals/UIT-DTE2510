def main ():

    print(isConsecutiveFour([int(i) for i in input("Legg inn liste med tall: ").split()]))


def isConsecutiveFour (values):
    consecutive = False
    consecNum = 0
    consecTotal = 0
    
    for j in range(len(values)-3) :

        for i in range (1,4) :

            if values[j] == values[j + i]:

                consecTotal += 1
                consecNum = values[j]

                if consecTotal >= 3:
                    consecutive = True
                
            else:
                consecTotal = 0
                break


    return "Det er 4 påfølgende " + str(consecNum) + " tall i listen" if consecutive else "Det er ingen påfølgende tall i listen."

        
main()