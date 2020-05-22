# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)
# list1 = [a, b, c]
# list1.sort()
# print(list1[1])

############################

a, b, c = map(int, input().split())
print(sorted([a, b, c])[1])