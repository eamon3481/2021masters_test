import sys 
cube = [["R","R","W"],["G","C","W"],["G","B","B"]]
def printCube(a):
    for x in a:
        for b in x:
            print(b, end=" ")
        print("")
    print("")

printCube(cube)

"""
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
 
"""

"""remove duplicate code"""
def Left_Right(dection,c):
    tem = tuple(c)
    for x in range(1,3):
        if dection == "L":
            c[x-1] = tem[x]
        elif dection == "R":
            c[x+1] = tem[x]
    c[2] = tem[0] 

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
        
def main(order):
    if order == "U":
        Left_Right(order,cube[0])
    elif order == "U'":
        Right(cube[0])
    elif order == "B'":
        Left(cube[2])
    elif order == "B":
        Right(cube[2])
    elif order == "L":
        LowerL(cube)
    elif order == "L'":
        upperL(cube)
    elif order == "R":
        upperR(cube)
    elif order == "R'":
        LowerR(cube)

def orderslist(a):
    orderslist = []
    tem = ""
    for x in a:
        if x == "'":
            orderslist.pop()
            orderslist.append(tem+x)
        else:
            orderslist.append(x)
        tem = x
    return orderslist


while True:
    orders = input("cube>")
    orders = orderslist(orders)
    
    if "Q" in orders:
        print("bye~")
        break
    else:
        for order in orders:
            main(order)
            print("\n", order)
            printCube(cube)
