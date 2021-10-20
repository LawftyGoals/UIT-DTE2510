def main():
    print(anagrams([str(i) for i in input("skriv inn to ord med mellomrom som skille: ").split()]))

def anagrams(values):

    if len(values[0]) == len(values[1]):

        ord_1_liste = []
        ord_2_liste = []

        anagram = False

        for j in range(len(values)):
            if j == 0:
                for ii in range(len(values[j])):
                    ord_1_liste.append(values[j][ii])
            elif j == 1:
                for ii in range(len(values[j])):
                    ord_2_liste.append(values[j][ii])

        for jj in ord_1_liste:
            if jj in ord_2_liste:
                anagram = True
            else:
                anagram = False
                break

        if anagram == True:

            for k in ord_2_liste:
                if k in ord_1_liste:
                    anagram = True
                else:
                    anagram = False
                    break
        
        if anagram == True:
            return "Ordene er anagram"
        
        else:
            return "Ordene er ikke anagram"


    else:
        return "Ordene er ikke anagram."



if __name__ == "__main__":
    main()
