# solution 1
a, b = map(int, input().strip().split(' '))
for i in range(b) : print('*' * a)


#####


# solution 2
print(('*'*a +'\n')*b)