import sys 
sys.stdin=open("test1\input.txt","rt")

word, b, direction = input().split()

num = int(b)

print(word[0])

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

print(swich(word,num))