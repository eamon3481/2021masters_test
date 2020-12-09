
cube= [[["B","B","B"],["B","B","B"],["B","B","B"]] , [["O","O","O"],["O","O","O"],["O","O","O"]] 
,[["G","G","G"],["G","G","G"],["G","G","G"]],[["W","W","W"],["W","W","W"],["W","W","W"]] 
,[["Y","Y","Y"],["Y","Y","Y"],["Y","Y","Y"]] ,[["R","R","R"],["R","R","R"],["R","R","R"]]]

def printcube():
    for x in cube[0]:
        for b in x:
            print(b, end=" ")
        print("")
    print("\n")
    for i in range(3):
        for j in range(1,5):
            for x in cube[j][i]:
                print(x,end=" ")
            print(" ", end="")
        print(" ")
    print("\n")
    for x in cube[5]:
        for b in x:
            print(b, end=" ")
        print("")
    print("\n")






printcube()

def ClockWise_U():
    tem = cube[1][0]
    for i in range(3):
        cube[1+i][0] = cube[2+i][0]
    cube[4][0]= tem

def ClockWise_D():
    tem = cube[1][2]
    for i in range(3):
        cube[1+i][2] = cube[2+i][2]
    cube[4][2]= tem

def counterClockWise_U():
    tem = cube[4][0]
    for i in range(3):
        cube[4-i][0] = cube[3-i][0]
    cube[1][0]= tem

def counterClockWise_D():
    tem = cube[4][2]
    for i in range(3):
        cube[4-i][2] = cube[3-i][2]
    cube[1][2]= tem

counterClockWise_U()
printcube()