import sys

n, x = input().split()
n, x = int(n), int(x)
xlist = [None] * n
xlist = sys.stdin.readline().split()
alist = []

for i in range(n) :
    if int(xlist[i]) < x :
        alist = alist + [xlist[i]]

print(" ".join(str(i) for i in alist))