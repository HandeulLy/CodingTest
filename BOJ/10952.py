import sys

while True :
    a, b = sys.stdin.readline().split()
    a, b = int(a), int(b)
    if a !=0 or b != 0 :
        print(a+b)
    else : 
        break