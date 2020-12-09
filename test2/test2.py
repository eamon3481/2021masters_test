import sys 
##f=open("test2\input.txt","rt")

##cube = [list(map(str,input().split())) for x in range(3)]
cube = [["R","R","W"],["G","C","W"],["G","B","B"]]
def printCube(a):
    for x in a:
        for b in x:
            print(b, end=" ")
        print("")

printCube(cube)

#order = input().split()

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
 

def upper(c):
    tem = []
    for x in c:
        tem.append(x[0])
    print(tem) 
    Left(tem)
    print(tem)
    for x in range(3):
        c[x][0] = tem[x]
    print(c)

printCube(cube)
upper(cube)
printCube(cube)