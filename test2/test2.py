import sys 
sys.stdin=open("test2\input.txt","rt")

cube = [list(map(str,input().split())) for x in range(3)]
print(cube)