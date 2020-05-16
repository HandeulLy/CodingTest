# sol1
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
print((a+b)%c)
print((a%c+b%c)%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

# sol2
a, b, c = map(int, input().split())
print("{}\n{}\n{}\n{}".format((a+b)%c, (a%c+b%c)%c, (a*b)%c, ((a%c)*(b%c))%c))