import sys 
sys.stdin=open("test2\input.txt","rt")

cube = [list(map(str,input().split())) for x in range(3)]

def printCube(a):
    for x in a:
        for b in x:
            print(b, end=" ")
        print("")

printCube(cube)