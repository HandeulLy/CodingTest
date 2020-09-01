import sys

arr, n = [0]*10001, sys.stdin.readline()

for i in range(int(n)) :
    arr[int(sys.stdin.readline())] += 1

for i, a in enumerate(arr) :
    if a > 0 : [print(i) for _ in range(a)]