import random
import copy

boardSize= 4

# wyswietlenie planszy
def printBoard():
    largest=0
    for row in board:
        for element in row:
            if element>largest:
                largest=element
    
    largestNumberLength=len(str(largest))

    for row in board:
        presentRow="|"
        for element in row:
            if element == 0:
                presentRow += " "*largestNumberLength+"|"
            else:
                presentRow += " "*(largestNumberLength-len(str(element))) + str(element)+"|"
        print(presentRow)

# dodanie jednego wiersza do lewej strony
def addOneRowL(row):   
    for i in range(boardSize-1):
        for j in range(boardSize-1, 0, -1):
            if row[j-1]==0:
                row[j-1]=row[j]
                row[j]=0
    
    for i in range(boardSize-1):
        if row[i]==row[i+1]:
            row[i]*=2
            row[i+1]=0

    for i in range(boardSize-1, 0, -1):
        if row[i-1]==0:
            row[i-1]=row[i]
            row[i]=0

    return row

# dodanie jednego wiersza do prawej strony
def addOneRowR(row):   
    for i in range(boardSize-1):
        for j in range(boardSize-1):
            if row[j+1]==0:
                row[j+1]=row[j]
                row[j]=0
    
    for i in range(boardSize-1):
        if row[i+1]==row[i]:
            row[i]*=2
            row[i+1]=0

    for i in range(boardSize-1):
        if row[i+1]==0:
            row[i+1]=row[i]
            row[i]=0

    return row

# dodanie wszystkich wierszy do lewej strony
def addAllRowsL(currentBoard):
    for i in range(boardSize):
        currentBoard[i]=addOneRowL(currentBoard[i])

    return currentBoard

# dodanie wszystkich wierszy do prawej strony
def addAllRowsR(currentBoard):
    for i in range(boardSize):
        currentBoard[i]=addOneRowR(currentBoard[i])

    return currentBoard

# transponowanie planszy
def transpose(currentBoard):
    for i in range(boardSize):
        for j in range(i, boardSize):
            if not j==i:
                temp = currentBoard[i][j]
                currentBoard[i][j]=currentBoard[j][i]
                currentBoard[j][i]=temp
    return currentBoard

# dodanie wszystkich kolumn do g??ry
def addAllRowsU(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = addAllRowsL(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard

#dodanie wszystkich kolumn do do??u
def addAllRowsD(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = addAllRowsR(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard


# funkcja zwracaj??ca 4 w jednym na o??miu przypadk??w, a w pozosta??ych siedmiu zwraca 2
def pickNewNumber():
    if random.randint(1,8)==1:
        return 4
    else:
        return 2

# funkcja dodajaca now?? warto???? do planszy w losowo wybranym, wolnym miejscu
def addNewValue():
    rowNum = random.randint(0, boardSize-1)
    colNum = random.randint(0, boardSize-1)

    while not board[rowNum][colNum]==0:
        rowNum = random.randint(0, boardSize-1)
        colNum = random.randint(0, boardSize-1)

    board[rowNum][colNum]=pickNewNumber()

# funkcja sprawdzaj??ca czy gra zosta??a wygrana
def won():
    for row in board:
        if 2048 in row:
            return True
        else:
            return False

# funkcja sprawdzaj??ca czy gra zosta??a przegrana
def lost():
    tempBoard1=copy.deepcopy(board)
    tempBoard2=copy.deepcopy(board)

    tempBoard1=addAllRowsL(tempBoard1)
    if tempBoard1==tempBoard2:
        tempBoard1=addAllRowsR(tempBoard1)
        if tempBoard1==tempBoard2:
            tempBoard1=addAllRowsU(tempBoard1)
            if tempBoard1==tempBoard2:
                tempBoard1=addAllRowsD(tempBoard1)
                if tempBoard1==tempBoard2:
                    return True
    return False

# tworzenie planszy pocz??tkowej
board=[]
for i in range(boardSize):
    row=[]
    for j in range(boardSize):
        row.append(0)
    board.append(row)

numNeeded=2
while numNeeded>=0:
    rowNum = random.randint(0, boardSize-1)
    colNum = random.randint(0, boardSize-1)

    if board[rowNum][colNum]==0:
        board[rowNum][colNum]=pickNewNumber()
        numNeeded -=1

# przedstawienie gry
print("Witaj w grze 2048! Celem tej gry jest uzyskanie liczby 2048 poprzez ????czenie liczb na planszy w r????nych kierunkach. \nGdy w konsole wpiszesz 'w' to liczby przsun?? si?? w g??r??, 's' w d????, 'a' w lewo, a 'd' w prawo. Powodzenia!\n\nPlansza:")
printBoard()

gameOver = False

# ruchy i wyniki po wpisaniu warto??ci przez gracza
while not gameOver:
    move = input("W kt??r?? stron?? chcesz przesun???? plansze? ")

    tempBoard = copy.deepcopy(board)

    if move=="w":
        board=addAllRowsU(board)
    elif move=="s":
        board=addAllRowsD(board)
    elif move=="a":
        board=addAllRowsL(board)
    elif move=="d":
        board=addAllRowsR(board)
    else:
        print("Wpisa??e?? z??y kierunek")

    if board==tempBoard:
        print("Spr??buj inny kierunek")
    else:
        if won():
            printBoard()
            print("Wygra??e??!")
            gameOver=True
        else:
            addNewValue()
            printBoard()
            if lost():
                print("Niestety przegra??e?? :(")
                gameOver=True      