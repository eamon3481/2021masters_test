
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

