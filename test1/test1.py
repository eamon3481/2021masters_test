import sys 
sys.stdin=open("test1\input.txt","rt")
word, b, direction = input().split()
num = int(b)
direction.upper()

def swich(word,number):
    tem=[0]*(len(word)) 
    for i in range(len(word)):
        if 0 <= i+number< len(word):
            tem[i+number]=word[i]
        elif i+number < 0:
            tem[len(word) + i+number]=word[i]
        elif i+number >= len(word):
            tem[i+number - len(word)]=word[i]
    Newword = ""
    for t in tem:
        Newword = Newword + t
    return Newword

if -100<= num <= 100:
    if direction == "R":
        print(swich(word,num))    
    elif direction == "L":
        print(swich(word,num*(-1)))    
    else:
        print("direction should be L or R")
else:
    print("number is -100 ~ +100")

