class EQ:

    def __init__(self, queens = [-1,-1,-1,-1,-1,-1,-1,-1]):
        
        self.queens = queens

    def get(self, index_num):
        
        return self.queens[index_num]

    def set(self, index_num, value_num):

        self.queens[index_num] = value_num

    def isSolved(self):
        # this segment checks each number in the array, it then creates a copy and removes the current value.
        # if the number drops bellow 7 (8 values minus minimum 1 value) it returns false because more than
        # one entry has been removed.
        for i in self.queens:
            i_less_queens = self.queens.copy()
            i_less_queens.remove(i)
            if len(i_less_queens) < 7:
                print(self.queens[0])
                return False
        
        # this segment now checks each list element value and then checks the diagonally right value. It
        # uses the range of 0 to 7 to acccess the queens list. it then uses a progressively reducing range
        # between 1 and 8 minus the list index. By doing this it accesess the next list value (being one
        # higher than current list value) and checks if it is the same as current list value increased by
        # list index. I think I explained this more complicated then I could have.
        for j in range(len(self.queens)):
            for jj in range (1, 8-j):
                if self.queens[j]+jj == self.queens[j+jj]:
                    return False
        
        # this segment does the same as above but reverses the diagonal direction to left.
        for k in range(len(self.queens), -1, -1):
            for kk in range (1, 8-k):
                if self.queens[k]-kk == self.queens[k+kk]:
                    return False
        
        # if no conditions above met, return true.
        return True
    
    def printBoard(self):
        # In order to print board a for loop is used to pass through each queens list value, a list is 
        # then created to hold each row of the print board_list. A second loop will then make each tile,
        # checking the value of the current queens list index to see which tile should be printed with
        # a Q. At the end of a list a final | is added to the end of the list to close off the board.
        for i in range(len(self.queens)):
            board_list = ""

            for ii in range(len(self.queens)):
                if self.queens[ii] == i:
                    board_list +='|Q'
                else:
                    board_list += '| '

            board_list += '|'

            print(*board_list, sep = "")


def main ():
    board1 = EQ()

    board1.set(0, 2)

    board1.set(1, 4)

    board1.set(2, 7)

    board1.set(3, 1)

    board1.set(4, 0)

    board1.set(5, 3)

    board1.set(6, 6)

    board1.set(7, 5)

    print("Is board1 a correct eight queen placement?",

        board1.isSolved())

 

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])

    if board2.isSolved():

        print("Eight queens are placed correctly in board2")

        board2.printBoard()

    else:

        print("Eight queens are placed incorrectly in board2")


if __name__ == "__main__":
    main()