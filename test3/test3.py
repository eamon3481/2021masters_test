
U= [["B","B","B"],["B","B","B"],["B","B","B"]]
F= [["O","O","O"],["O","O","O"],["O","O","O"]]
R= [["G","G","G"],["G","G","G"],["G","G","G"]]
L= [["W","W","W"],["W","W","W"],["W","W","W"]]
B= [["Y","Y","Y"],["Y","Y","Y"],["Y","Y","Y"]] 
D= [["R","R","R"],["R","R","R"],["R","R","R"]]

def printcube():
    for x in U:
        for b in x:
            print(b, end=" ")
        print("")
    print("\n")
    for i in range(3):
        for x in F[i]:
            print(x,end=" ")
        print(" ", end="")
        for x in R[i]:
            print(x,end=" ")
        print(" ", end="")
        for x in L[i]:
            print(x,end=" ")
        print(" ", end="")
        for x in B[i]:
            print(x,end=" ")
        print(" ")
    print("\n")
    for x in D:
        for b in x:
            print(b, end=" ")
        print("")
    print("\n")


printcube()