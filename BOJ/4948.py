# 4948 - 베르트랑 공준

# 베르트랑 공준은 임의의 자연수 n에 대하여 n보다 크고, 2n 이하의 소수는 적어도 하나 존재한다는 내용이다
# n이 주어질 때, 2보다 크고 2n 이하의 범위에 있는 소수 개수를 구하라

# 입력
# - 입력은 여러 테스트 케이스로 이루어져 있다
# - 각 케이스는 n을 포함하며, 한 줄로 이루어져 있다(n은 123456 이하)
# - 마지막 입력에는 0이 주어진다.

# 출력
# - 각 테스트 케이스에 대해 조건에 맞는 소수 개수를 출력

#################################################

'''
우선, 소수 구하는 함수를 작성하고 while문을 반복하면서 프로그램 진행.


0이 들어오면 break, 0이 아닌 수가 들어오면 소수 구하는 함수 호출
함수에서 소수를 찾으면, cnt 변수 증가 시키고, 결과 출력
'''

'''
def sosu(n) :
    if n == 1 : return False
    for i in range(2, n) :
        if n % i == 0 : return False
    return True

while True : 
    n = int(input())
    cnt = 0
    if n : 
        for i in range(n+1, 2*n + 1) : 
            if sosu(i) :
                cnt += 1
    else : break
'''

# 위 코드, 시간 초과 에러

#################################################

'''
import sys

while True : 
    n = int(sys.stdin.readline())
    if n : 
        a = set(i+1 for i in range(n, 2*n))
        for j in range(2, n+1) :
            m = (2*n) // j
            b = set( (k+1) * j for k in range(m))
            a -= b
        print(len(a))
    else : break
'''

# 위 코드 역시 시간 초과 에러...

#################################################

'''
import sys

a = set(i for i in range(1, 2*123456+1))

while True : 
    n = int(sys.stdin.readline())
    if n : 
        for j in range(2, n+1) :
            m = (2*123546) // j
            # b = set( (k+1) * j for k in range(m))
            a -= set( (k+1) * j for k in range(m))
        c = set(i for i in range(n, n*2))
        print(len(a), len(c), len(a & c))
    else : break
'''
    
# 위 코드도 시간 초과 에러....!!!

#################################################

# import sys

# def sosu(n) :
#     for i in range(2, int(n**0.5+1)) :
#         if n % i == 0 : return False
#     return True

# a = []
# for i in range(2, 123456*2) : 
#     if sosu(i) : a.append(i)

# while True : 
#     n, cnt = int(sys.stdin.readline()), 0
#     if n : 
#         for i in a :
#             if n < i <= 2*n : cnt += 1
#         print(cnt)
#     else : break

#################################################

import sys

def sosu(n) :
    for i in range(2, int(n**0.5+1)) :
        if n % i == 0 : return False
    return True

a = set()
for i in range(2, 123456*2+1) : 
    if sosu(i) : a.add(i)

while True : 
    n = int(sys.stdin.readline())
    if n : 
        b = set(i for i in range(n ,n*2))
        print(len(a & b))
    else : break