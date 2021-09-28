def genomeParser(genome):

    starter = "ATG"

    ender = ["TAG", "TAA", "TGA", "ATG"]

    genes = []

    if starter in genome:
        for i in genome.split("ATG"):
            geneCol = ""
            for j in range(len(i)-2):
                if (i[j]+i[j+1]+i[j+2]) in ender:
                    break
                else:
                    geneCol += i[j]
            genes.append(geneCol)
        
        for ii in genes:
            print(ii)

    else:
        print("Ingen gener funnet")


def main():
    genomeParser(input("Legg inn genome streng for å sjekke om det er gener: "))


main()
                