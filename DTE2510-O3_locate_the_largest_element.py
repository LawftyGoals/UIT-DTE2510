def locate_largest():
    number_of_rows = int(input("Legg inn antall rader du ønsker i listen: "))

    full_list = []

    for i in range(number_of_rows):
        full_list.append(input("Legg inn raden: ").split(" "))

    largest = full_list[0][0]

    largest_location = [0,0]

    for i in range(number_of_rows):
        for j in range(len(full_list[i])):
            
            if int(full_list[i][j]) > int(largest):
                largest = full_list[i][j]
                largest_location = [i,j]
    
    print(*largest_location, sep = ",")

locate_largest()



