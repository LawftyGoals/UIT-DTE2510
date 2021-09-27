def parser(stringy):

    tester = []


    genes = ""

    for i in range(0,len(stringy)-1,3):

        geneTrip = ""

        for j in range(0,3):
            geneTrip += stringy[i+j]
        
        tester.append(geneTrip)

    print(tester)
    isGene = False

    for ii in range(len(tester)):

        if isGene:
            genes+=tester[ii]

        if (isGene == True) and (tester[ii] == "TAG" or tester[ii] == "ATG" or tester[ii] == "TAA" or tester[ii] == "TGA"):
            isGene = False
            print(genes)
            genes = ""
        elif tester[ii] == "ATG":
            isGene = True

    print(genes)

parser("TTATGTTTTAAGGATGGGGCGTTAGTT")