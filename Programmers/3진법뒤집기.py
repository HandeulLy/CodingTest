
'''
# 문제
    - 자연수 n
    - n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현

# 제한조건
    - n은 1이상 100,000,000이하
'''

def solution(n):
    ans = []
    while n>2 :
        n, m = n//3, n%3
        ans += [m]
    ans += [n]
        
    answer = 0
    for i in range(len(ans)) :
        answer += (3**i) * ans[-1-i]
    
    return answer

##########################################

# ex1
n = 45
solution(n)
    # result : 7

# ex2
n = 125
solution(n)
    # result : 229