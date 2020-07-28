'''

    2 이상 1,000,000 이하의 자연수 n
    1부터 n 사이에 있는 소수의 개수를 반환하는 함수를 작성한다

'''

# def solution(n):
#     s = []

#     for i in range(2, n+1) :
#         c = 0
#         for j in s :
#             if i % j == 0 : c += 1; break
#         if c == 0  : s.append(i)
#         print(i, c, s)

#     return len(s)

# solution(1000)

# ===========================================

def solution(n):
    s = set(range(3, n+1, 2))

    for i in range(3, n+1, 2) :
        if i in s :
            s = s - set(range(i*2, n+1, i))
            #print(i, s)

    return print(len(s) + 1)

solution(100000)