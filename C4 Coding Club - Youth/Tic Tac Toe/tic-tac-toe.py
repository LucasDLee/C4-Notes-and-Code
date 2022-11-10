# print('{0} | {1} | {2}\n{3} | {4} | {5}\n{6} | {7} | {8}'.format('Geeks', 'For', 'Geeks'))

gameOn = input("Do you want to start the game? ")

def runGame():
    while gameOn:
        print("Player 1\n---------------------")
        player1Move = str(input("What tile would you like to use:"))
        
        break
    return

def showBoard():
    line1 = "{0} | {1} | {2}".format(' ', ' ', ' ')
    line2 = "{0} | {1} | {2}".format(' ', ' ', ' ')
    line3 = "{0} | {1} | {2}".format(' ', ' ', ' ')
    divider1 =""
    divider2 = ""
    for x in range(len(line1)):
        divider1 += "-"
        divider2 += "-"

    showBoard = ("{l1}\n{d1}\n{l2}\n{d2}\n{l3}").format(l1 = line1, l2 = line2, l3 = line3, d1 = divider1, d2 = divider2)
    print(showBoard)

def checkWinner():
    return

runGame()