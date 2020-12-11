import time
import datetime
import random

ture_cube= [[["B","B","B"],["B","B","B"],["B","B","B"]] , [["W","W","W"],["W","W","W"],["W","W","W"]],
[["O","O","O"],["O","O","O"],["O","O","O"]] ,[["G","G","G"],["G","G","G"],["G","G","G"]]
,[["Y","Y","Y"],["Y","Y","Y"],["Y","Y","Y"]] ,[["R","R","R"],["R","R","R"],["R","R","R"]]]


cube= [[["B","B","B"],["B","B","B"],["B","B","B"]] , [["W","W","W"],["W","W","W"],["W","W","W"]],
[["O","O","O"],["O","O","O"],["O","O","O"]] ,[["G","G","G"],["G","G","G"],["G","G","G"]]
,[["Y","Y","Y"],["Y","Y","Y"],["Y","Y","Y"]] ,[["R","R","R"],["R","R","R"],["R","R","R"]]]


def printcube():
    for x in cube[0]:
        print(" "*10, end=" ")
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
        print(" "*10, end=" ")
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
        cube[5][x][0] = cube[4][x][2]
        cube[4][x][2] = cube[0][x][0]
        cube[0][x][0] = tem[x]
    CClockWise_surface(cube[1])

def ClockWise_R():
    tem = ( cube[2][0][2], cube[2][1][2], cube[2][2][2])
    for x in range(3):
        cube[2][x][2] = cube[5][x][2]
        cube[5][x][2] = cube[4][x][0]
        cube[4][x][0] = cube[0][x][2]
        cube[0][x][2] = tem[x]
    ClockWise_surface(cube[3])

def ClockWise_L():
    tem = ( cube[2][0][0], cube[2][1][0], cube[2][2][0])
    for x in range(3):
        cube[2][x][0] = cube[0][x][0]
        cube[0][x][0] = cube[4][x][2]
        cube[4][x][2] = cube[5][x][0]
        cube[5][x][0] = tem[x]
    ClockWise_surface(cube[1])

def CClockWise_R():
    tem = ( cube[2][0][2], cube[2][1][2], cube[2][2][2])
    for x in range(3):
        cube[2][x][2] = cube[0][x][2]
        cube[0][x][2] = cube[4][x][0]
        cube[4][x][0] = cube[5][x][2]
        cube[5][x][2] = tem[x]
    CClockWise_surface(cube[3])

def Clockwise_F():
    tem = tuple(cube[0][2])
    for x in range(3):
        cube[0][2][x] = cube[1][x][2]
        cube[1][x][2] = cube[5][0][x]
        cube[5][0][x] = cube[3][x][0]
        cube[3][x][0] = tem[x]
    ClockWise_surface(cube[2])

def CClockwise_F():
    tem = tuple(cube[0][2])
    for x in range(3):
        cube[0][2][x] = cube[3][x][0]
        cube[3][x][0] = cube[5][0][x]
        cube[5][0][x] = cube[1][x][2]
        cube[1][x][2] = tem[x]
    CClockWise_surface(cube[2])

def Clockwise_B():
    tem = tuple(cube[0][0])
    for x in range(3):
        cube[0][2][x] = cube[3][x][2]
        cube[3][x][2] = cube[5][2][x]
        cube[5][2][x] = cube[1][x][0]
        cube[1][x][0] = tem[x]
    ClockWise_surface(cube[4])

def CClockwise_B():
    tem = tuple(cube[0][0])
    for x in range(3):
        cube[0][2][x] = cube[1][x][0]
        cube[1][x][0] = cube[5][2][x]
        cube[5][2][x] = cube[3][x][2]
        cube[3][x][2] = tem[x]
    CClockWise_surface(cube[4])

def main(order):
    if order == "U":
        ClockWise_U()
    elif order == "U'":
        counterClockWise_U()  
    elif order == "D":
        ClockWise_D()
    elif order == "D'":
        counterClockWise_D()
    elif order == "L":
        ClockWise_L()
    elif order == "L'":
        CClockWise_L()
    elif order == "R":
        ClockWise_R()
    elif order == "R'":
        CClockWise_R()
    elif order == "F":
        Clockwise_F()
    elif order == "F'":
        CClockwise_F()
    elif order == "B":
        Clockwise_B()
    elif order == "B'":
        CClockwise_B()

def orderslist(a):
    orderslist = []
    tem = ""
    for x in a:
        if x == "'":
            orderslist.pop()
            orderslist.append(tem+x)
        elif x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x=="8" or x=="9":
            orderslist.pop()
            for i in range(int(x)):
                orderslist.append(tem)
        else:
            orderslist.append(x)
        tem = x
    return orderslist

def randomcube():
    randomorder = ["F","F'","D","D'","L","L'","R","R'","B","B'","U","U'"]
    num = 50
    for i in range(num):
        main(random.choice(randomorder))

randomcube()        
printcube()


def printtime(st):
    sec = time.time()-st
    times = str(datetime.timedelta(seconds=sec)).split(".")
    times = times[0]
    print("경과 시간: ", times)

start = time.time()
cnt = 0
while True:
    orders = input("cube>")
    orders = orderslist(orders)
    if "Q" in orders:
        print("조작개수:", cnt)
        printtime(start)
        print("이용해 주셔서 감사합니다. 뚜뚜뚜.")
        break
    else:
        for order in orders:
            main(order)
            print("\n", order)
            printcube()
            cnt = cnt+1
            if ture_cube == cube:
                print("조작개수:", cnt)
                printtime(start)
                print("맞췄습니다 축하드려요. 뚜뚜뚜.")
                break
        



    
         
