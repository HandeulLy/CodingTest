a = int(input())

for i in range(a) :
    x, y = input().split()
    print("Case #{}: {} + {} = {}".format(i+1, int(x), int(y), int(x)+int(y)))