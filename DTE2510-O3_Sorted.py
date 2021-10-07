


def isListSorted():
    numList = input("Legg inn en liste med tall: ").split()

    isSorted = False

    for i in range(len(numList)-1):
        if int(numList[i]) <= int(numList[i+1]):
            isSorted = True
        else:
            isSorted = False
            break
    
    return "Listen er sortert" if isSorted==True else "Listen er ikke sortert"

        

print(isListSorted())