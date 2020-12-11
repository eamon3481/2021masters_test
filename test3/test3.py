
cube= [[["B","B","B"],["B","B","B"],["B","B","B"]] , [["W","W","W"],["W","W","W"],["W","W","W"]],
[["O","O","O"],["O","O","O"],["O","O","O"]] ,[["G","G","G"],["G","G","G"],["G","G","G"]]
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


def ClockWise_surface(c):
    tem = tuple(c[0])
    c[0][1] = c[1][2]
    c[0][2] = c[2][2]
    c[1][2] = c[2][1]
    c[2][2] = c[2][0]
    c[2][1] = c[1][0]
    c[2][0] = tem[0]
    c[1][0] = tem[1]
    c[0][0] = tem[2]

def CClockWise_surface(c):
    tem = tuple(c[0])
    c[0][1] = c[1][0]
    c[0][0] = c[2][0]
    c[1][0] = c[2][1]
    c[2][0] = c[2][2]
    c[2][1] = c[1][2]
    c[2][2] = tem[2]
    c[1][2] = tem[1]
    c[0][2] = tem[0]



printcube()

def ClockWise_U():
    ClockWise_surface(cube[0])
    tem = cube[1][0]
    for i in range(3):
        cube[1+i][0] = cube[2+i][0]
    cube[4][0]= tem

def ClockWise_D():
    ClockWise_surface(cube[5])
    tem = cube[1][2]
    for i in range(3):
        cube[1+i][2] = cube[2+i][2]
    cube[4][2]= tem

def counterClockWise_U():
    CClockWise_surface(cube[0])
    tem = cube[4][0]
    for i in range(3):
        cube[4-i][0] = cube[3-i][0]
    cube[1][0]= tem

def counterClockWise_D():
    CClockWise_surface(cube[5])
    tem = cube[4][2]
    for i in range(3):
        cube[4-i][2] = cube[3-i][2]
    cube[1][2]= tem

def CClockWise_L():
    tem = ( cube[2][0][0], cube[2][1][0], cube[2][2][0])
    for x in range(3):
        cube[2][x][0] = cube[5][x][0]
        cube[5][x][0] = cube[4][x][0]
        cube[4][x][0] = cube[0][x][0]
        cube[0][x][0] = tem[x]
    CClockWise_surface(cube[1])

def ClockWise_R():
    tem = ( cube[2][0][2], cube[2][1][2], cube[2][2][2])
    for x in range(3):
        cube[2][x][2] = cube[5][x][2]
        cube[5][x][2] = cube[4][x][2]
        cube[4][x][2] = cube[0][x][2]
        cube[0][x][2] = tem[x]
    ClockWise_surface(cube[3])

def ClockWise_L():
    tem = ( cube[2][0][0], cube[2][1][0], cube[2][2][0])
    for x in range(3):
        cube[2][x][0] = cube[0][x][0]
        cube[0][x][0] = cube[4][x][0]
        cube[4][x][0] = cube[5][x][0]
        cube[5][x][0] = tem[x]
    ClockWise_surface(cube[1])

def ClockWise_R():
    tem = ( cube[2][0][2], cube[2][1][2], cube[2][2][2])
    for x in range(3):
        cube[2][x][2] = cube[0][x][2]
        cube[0][x][2] = cube[4][x][2]
        cube[4][x][2] = cube[5][x][2]
        cube[5][x][2] = tem[x]
    ClockWise_surface(cube[3])

printcube()