
def printDistinctNum(number):

    listM = []

    list2 = []

    for j in number:
        listM.append(int(j))

    for i in listM:
        if i not in list2:
            list2.append(i)

    print(listM, list2)


printDistinctNum(input("skriv in listen med heltalt fordelt med mellomrom: ").split())