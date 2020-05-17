'''
곱셈

(세 자리 수) x (세 자리 수)

입력 : 세 자리 수 자연수가 2번 들어옴
출력 : 각 단계의 결과 값을 4줄로 출력
'''

#############################################################

# ver1

# a = int(input())
# b = int(input())
# b100 = b//100
# b10 = (b%100)//10
# b1 = b%10
# print(b1*a)
# print(b10*a)
# print(b100*a)
# print(b1*a+b10*a*10+b100*a*100)

#############################################################

# ver2 - 4 cases

# import sys
# x = sys.stdin.readline()
# y = sys.stdin.readline()
# [print(int(x)*int(y[2-i])) for i in range(3)]
# print(int(x)*int(y))
# # 56ms 127B

#############################################################

# import sys
# x, y = sys.stdin.readline(), sys.stdin.readline()
# [print(int(x)*int(y[2-i])) for i in range(3)]
# print(int(x)*int(y))
# # 56ms 127B

#############################################################

# import sys
# a = [sys.stdin.readline() for i in range(2)]
# [print(int(a[0])*int(a[1][2-i])) for i in range(3)]
# print(int(a[0])*int(a[1]))
# # 56ms 134B

#############################################################

# a, b = int(input()), input()
# [print(a*int(b[2-i])) for i in range(3)]
# print(a*int(b))
# # 52ms 85B

#############################################################