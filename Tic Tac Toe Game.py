#Simple Tic Tac Toe Game
#Made by Connor Hall

from colored import Fore, Back , Style
class Game:
    def printBoard(self):
        #Print a 3 x 3 board


        for i in range (11):
            for j in range(23):

                if (j,i) in color_boxes:
                    print(f"{Back.green}", end="")
                
                if (j,i) in num_coordinates.keys():
                    print(num_coordinates.get((j,i)), end = "")
                    

                elif (j,i) in x_coordinates:
                    print("X",end="")

                elif (j,i) in o_coordinates:
                    print("O",end="")

                elif j == 7 or j == 15:
                    if i == 3 or i == 7:
                        print("+", end="")

                    else:
                        print("|", end ="")

                elif i == 3 or i == 7:
                    print("-", end ="")

                else:
                    print(" ", end ="")
                print(f"{Style.reset}",end="")

            print()
    
    def user1Input(self):
        validAnswer = False
        while not validAnswer:
            try:
                ans = int(input("Where would you like to play? Please select a region that has not been taken already: "))
                if ans in num_coordinates.values():
                    validAnswer = True
            except:
                print("Please enter a valid number. ")
            

        for k,v in num_coordinates.items():
            if v == ans:
                x_coordinates.append(k)
                num_coordinates.pop(k)
                break
    
    def user2Input(self):
        validAnswer = False
        while not validAnswer:
            try:
                ans = int(input("Where would you like to play? Please select a region that has not been taken already: "))
                if ans in num_coordinates.values():
                    validAnswer = True
            except:
                print("Please enter a valid number. ")
            

        for k,v in num_coordinates.items():
            if v == ans:
                o_coordinates.append(k)
                num_coordinates.pop(k)
                break

    def winnerCheck(self):
        global winner
        global phrase
        if (3,1) in x_coordinates and (11,1) in x_coordinates and (19,1) in x_coordinates:
            winner = True
            phrase = f"{player1_name} wins across the top row."
            regions.append((3,1))
            regions.append((11,1))
            regions.append((19,1))
        elif (3,1) in o_coordinates and (11,1) in o_coordinates and (19,1) in o_coordinates:
            winner = True
            phrase = f"{player2_name} wins across the top row."
            regions.append((3,1))
            regions.append((11,1))
            regions.append((19,1))

        elif (3,5) in x_coordinates and (11,5) in x_coordinates and (19,5) in x_coordinates:
            winner = True
            phrase = f"{player1_name} wins across the middle row."
            regions.append((3,5))
            regions.append((11,5))
            regions.append((19,5))

        elif (3,5) in o_coordinates and (11,5) in o_coordinates and (19,5) in o_coordinates:
            winner = True
            phrase = f"{player2_name} wins across the middle row."
            regions.append((3,5))
            regions.append((11,5))
            regions.append((19,5))

        elif (3,9) in x_coordinates and (11,9) in x_coordinates and (19,9) in x_coordinates:
            winner = True
            phrase = f"{player1_name} wins across the bottom row."
            regions.append((3,9))
            regions.append((11,9))
            regions.append((19,9))

        elif (3,9) in o_coordinates and (11,9) in o_coordinates and (19,9) in o_coordinates:
            winner = True
            phrase = f"{player2_name} wins across the bottom row."
            regions.append((3,9))
            regions.append((11,9))
            regions.append((19,9))

        elif (3,1) in x_coordinates and (3,5) in x_coordinates and (3,9) in x_coordinates:
            winner = True
            phrase = f"{player1_name} wins across the left column."
            regions.append((3,1))
            regions.append((3,5))
            regions.append((3,9))

        elif (3,1) in o_coordinates and (3,5) in o_coordinates and (3,9) in o_coordinates:
            winner = True
            phrase = f"{player2_name} wins across the left column."
            regions.append((3,1))
            regions.append((3,5))
            regions.append((3,9))

        elif (11,1) in x_coordinates and (11,5) in x_coordinates and (11,9) in x_coordinates:
            winner = True
            phrase =f"{player1_name} wins across the middle column."
            regions.append((11,1))
            regions.append((11,5))
            regions.append((11,9))

        elif (11,1) in o_coordinates and (11,5) in o_coordinates and (11,9) in o_coordinates:
            winner = True
            phrase = f"{player2_name} wins across the middle column."
            regions.append((11,1))
            regions.append((11,5))
            regions.append((11,9))

        elif (19,1) in x_coordinates and (19,5) in x_coordinates and (19,9) in x_coordinates:
            winner = True
            phrase = f"{player1_name} wins across the right column."
            regions.append((19,1))
            regions.append((19,5))
            regions.append((19,9))

        elif (19,1) in o_coordinates and (19,5) in o_coordinates and (19,9) in o_coordinates:
            winner = True
            phrase = f"{player2_name} wins across the right column."
            regions.append((19,1))
            regions.append((19,5))
            regions.append((19,9))

        elif (3,1) in x_coordinates and (11,5) in x_coordinates and (19,9) in x_coordinates:
            winner = True
            phrase = f"{player1_name} wins across the left diagnol."
            regions.append((3,1))
            regions.append((11,5))
            regions.append((19,9))

        elif (3,1) in o_coordinates and (11,5) in o_coordinates and (19,9) in o_coordinates:
            winner = True
            phrase = f"{player2_name} wins across the left diagnol."
            regions.append((3,1))
            regions.append((11,5))
            regions.append((19,9))

        elif (3,9) in x_coordinates and (10,5) in x_coordinates and (17,1) in x_coordinates:
            winner = True
            phrase = f"{player1_name} wins across right diagnol."
            regions.append((3,9))
            regions.append((11,5))
            regions.append((19,1))

        elif (3,9) in o_coordinates and (11,5) in o_coordinates and (19,1) in o_coordinates:
            winner = True
            phrase = f"{player2_name} wins across right diagnol."
            regions.append((3,9))
            regions.append((11,5))
            regions.append((19,1))

        #Draw Check
        elif not num_coordinates:
            phrase = "Draw"


    def coloredBoxes(self):
        if len(regions) != 3:
            return
        
        for i in regions:
            x = i[0]
            y = i[1]
            
            color_boxes.append((x-3,y-1))
            color_boxes.append((x-2,y-1))
            color_boxes.append((x-1,y-1))
            color_boxes.append((x,y-1))
            color_boxes.append((x+1,y-1))
            color_boxes.append((x+2,y-1))
            color_boxes.append((x+3,y-1))
            color_boxes.append((x-3,y))
            color_boxes.append((x-2,y))
            color_boxes.append((x-1,y))
            color_boxes.append((x,y))
            color_boxes.append((x+1,y))
            color_boxes.append((x+2,y))
            color_boxes.append((x+3,y))
            color_boxes.append((x-3,y+1))
            color_boxes.append((x-2,y+1))
            color_boxes.append((x-1,y+1))
            color_boxes.append((x,y+1))
            color_boxes.append((x+1,y+1))
            color_boxes.append((x+2,y+1))
            color_boxes.append((x+3,y+1))

            

        return color_boxes



                

#############################################################################################
#Code for output
#############################################################################################

board = Game()

press = input("Welcome to the game of Tic Tac Toe, please press enter to begin. ")

again = True
player1_name = input("What is player one's name: ")
player2_name = input("What is player two's name: ")

while again:
    winner = False
    num_coordinates = {
    (3,1):1,
    (11,1):2,
    (19,1):3,
    (3,5):4,
    (11,5):5,
    (19,5):6,
    (3,9):7,
    (11,9):8,
    (19,9):9
    }
    x_coordinates = []
    o_coordinates = []
    regions = []
    color_boxes = []
    phrase=""

    board.printBoard()
    while not winner:
        board.user1Input()
        board.printBoard()
        board.winnerCheck()
        board.coloredBoxes()
        if winner or not num_coordinates:
            break
        board.user2Input()
        board.printBoard()
        board.winnerCheck()
        board.coloredBoxes()

    board.printBoard()
    print(phrase)

   
    again = input("Would you like to play again(Y/N): ")
    if again == "N":
        again = False

print("Game Over. Thanks for playing. ")



                