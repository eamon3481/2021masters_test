from os import close
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

def upperL(c):
    tem = c[0]
    for x in range(1,3):
        print(x)
        c[0][x-1] = tem[x] 
    c[0][2] = tem[0] 
    print(c[0])


upperL(cube)
print(cube)