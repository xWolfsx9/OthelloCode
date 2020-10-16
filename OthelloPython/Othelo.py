Count = 8
PlayerX = 'X'
PlayerO = 'O'
Empty = ' '
Board = [[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]
CountTable = [0, 0, 0, 0, 0, 0, 0, 0]

def ClearBoard():
    for baris in range (0, Count):
        for kolom in range (0,Count):
            Board[baris][kolom] = Empty

def NewBoard():
    ClearBoard()
    Board[3][3] = PlayerX
    Board[4][4] = PlayerX
    Board[3][4] = PlayerO
    Board[4][3] = PlayerO

def PrintBoard():
    print("  01234567")
    for baris in range (0, Count):
        print(baris, end=' ')
        for kolom in range (0, Count):
            print(Board[baris][kolom], end='')
        print()

def CalculateGained (yp, xp):
    print(Turn)
    #0 (atas)
    x = xp
    y = yp - 1
    CountTable[0] = 0
    while (y>=0):
        if Board[y][x] == Empty:
            CountTable[0] = 0
            break
        elif Board[y][x] == Turn :
            break
        else:
            y-=1
            CountTable[0]+=1

    #1 (kanan)
    x = xp+1
    y = yp
    CountTable[1] = 0
    while (x<Count):
        if Board[y][x] == Empty:
            CountTable[1] = 0
            break
        elif Board[y][x] == Turn :
            break
        else:
            x+=1
            CountTable[1]+=1



    #2 (bawah)
    x = xp
    y = yp + 1
    CountTable[2] = 0
    while (y<Count):
        if Board[y][x] == Empty:
            CountTable[2] = 0
            break
        elif Board[y][x] == Turn :
            break
        else:
            y+=1
            CountTable[2]+=1

    #3 (kiri)
    x = xp-1
    y = yp
    CountTable[3] = 0
    while (x>=0):
        if Board[y][x] == Empty:
            CountTable[3] = 0
            break
        elif Board[y][x] == Turn :
            break
        else:
            x-=1
            CountTable[3]+=1

    #4 (atas kiri)
    x = xp-1
    y = yp-1
    CountTable[4] = 0
    while (y>=0 and x>=0):
        if Board[y][x] == Empty:
            CountTable[4] = 0
            break
        elif Board[y][x] == Turn:
            break
        else:
            x-=1
            y-=1
            CountTable[4]+=1


    #5 (atas kanan)
            
    x = xp + 1  
    y = yp - 1  
    CountTable[5] = 0
    while (y>=0 and x<Count):
        print("Ok", CountTable[5])
        if Board[y][x] == Empty:
            print("a")
            CountTable[5] = 0
            break
        elif Board[y][x] == Turn:
            print("b")
            break
        else:
            x+=1
            y-=1
            CountTable[5]+=1
    print("dOk", CountTable[5])

    #6 (bawah kanan)
    x = xp + 1
    y = yp + 1
    CountTable[6] = 0
    while (y<Count and x<Count):
        if Board[y][x] == Empty:
            CountTable[6] = 0
            break
        elif Board[y][x] == Turn:
            break
        else:
            x+=1
            y+=1
            CountTable[6]+=1

    #7 (bawah kiri)
    x = xp - 1
    y = yp + 1
    CountTable[7] = 0
    while (y<Count and x>=0):
        if Board[y][x] == Empty:
            CountTable[7] = 0
            break
        elif Board[y][x] == Turn:
            break
        else:
            x-=1
            y+=1
            CountTable[7]+=1
    print("dOk", CountTable[5])
    TotalCount = 0
    for i in range (0, 8):
        print(i, CountTable[i])
        TotalCount+=CountTable[i]
    print("Total", TotalCount)
    return TotalCount


def ChangeColor(yp, xp):
    #0
    x = xp
    y = yp - 1
    for i in range (1, CountTable[0]+1):
        Board[y][x] = Turn
        y-=1
    
    #1
    x = xp+1
    y = yp
    for i in range (1, CountTable[1]+1):
        Board[y][x] = Turn
        x+=1

    #2
    x = xp
    y = yp + 1
    for i in range (1, CountTable[2]+1):
        Board[y][x] = Turn
        y+=1

    #3
    x = xp-1
    y = yp
    for i in range (1, CountTable[3]+1):
        Board[y][x] = Turn
        x-=1

    #4
    x = xp - 1
    y = yp - 1
    for i in range (1, CountTable[4]+1):
        Board[y][x] = Turn
        x-=1
        y-=1

    #5
    x = xp + 1
    y = yp - 1
    for i in range (1, CountTable[5]+1):
        Board[y][x] = Turn
        x+=1
        y-=1

    #6
    x = xp + 1
    y = yp + 1
    for i in range (1, CountTable[6]+1):
        Board[y][x] = Turn
        x+=1
        y+=1

    #7
    x = xp - 1
    y = yp + 1
    for i in range (1, CountTable[7]+1):
        Board[y][x] = Turn
        x-=1
        y+=1


Turn = PlayerX
NewBoard()

while True:
    PrintBoard()
    print("\nPlayer ", Turn, ":\n")
    yInput = int(input("Please enter row: "))
    xInput = int(input("Please enter col: "))

    if ((xInput>=0) and (xInput<Count)) and  ((yInput>=0) and (yInput<Count)):
        if Board[yInput][xInput] == Empty:
            if CalculateGained(yInput, xInput)>0:
                Board[yInput][xInput] = Turn
                ChangeColor(yInput, xInput)
                if Turn == PlayerX: Turn = PlayerO
                else: Turn = PlayerX
    if (xInput>Count) and (yInput>Count):
        break
