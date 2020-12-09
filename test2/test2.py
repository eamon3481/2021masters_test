import sys 
cube = [["R","R","W"],["G","C","W"],["G","B","B"]]
def printCube(a):
    for x in a:
        for b in x:
            print(b, end=" ")
        print("")
    print("")

printCube(cube)

def Left(c):
    tem = tuple(c)
    for x in range(1,3):
        c[x-1] = tem[x] 
    c[2] = tem[0] 

def Right(c):
    tem = tuple(c) 
    for x in range(0,2):
        c[x+1] = tem[x] 
    c[0] = tem[2] 
 

def upperL(c):
    tem = []
    for x in c:
        tem.append(x[0])
    Left(tem)
    for x in range(3):
        c[x][0] = tem[x]

def upperR(c):
    tem = []
    for x in c:
        tem.append(x[2])
    Left(tem)
    for x in range(3):
        c[x][2] = tem[x]

def LowerL(c):
    tem = []
    for x in c:
        tem.append(x[0])
    Right(tem)
    for x in range(3):
        c[x][0] = tem[x]

def LowerR(c):
    tem = []
    for x in c:
        tem.append(x[2])
    Right(tem)
    for x in range(3):
        c[x][2] = tem[x]
        
def main(orders):
    for order in orders:
        if order == "U":
            print("\n", order)
            Left(cube[0])
            printCube(cube)
        elif order == "U'":
            print("\n", order)
            Right(cube[0])
            printCube(cube)
        elif order == "B'":
            print("\n", order)
            Left(cube[2])
            printCube(cube)
        elif order == "B":
            print("\n", order)
            Right(cube[2])
            printCube(cube)
        elif order == "L":
            print("")
            print("\n", order)
            LowerL(cube)
            printCube(cube)
        elif order == "L'":
            print("\n", order)
            upperL(cube)
            printCube(cube)
        elif order == "R":
            print("\n", order)
            upperR(cube)
            printCube(cube)
        elif order == "R'":
            print("\n", order)
            LowerR(cube)
            printCube(cube)
    

while True:
    orders = input("cube>").split()
    if "Q" in orders:
        print("bye~")
        break
    else:
        main(orders)
