
'''
# 문제
    - 두 정수 배열 a, b
    - a와 b는 길이가 같은 1차원 정수 배열
    - a와 b의 내적을 반환하는 함수 작성
    - 이 때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]의 결과 값

# 제한조건
    - a, b의 길이는 1이상 1,000이하
    - a, b의 모든 수는 -1,000이상 1,000이하
'''

def solution(a, b):
    answer = 0
    
    for i, j in zip(a, b) : 
        answer += i*j

    return answer

def solution2(a, b):
    
    return sum([x*y for x, y in zip(a, b)])

##########################################

# ex1
a1 = [1,2,3,4]
b1 = [-3,-1,0,2]
solution(a1, b1)
    # result : 3

# ex2
a2 = [-1,0,1]
b2 = [1,0,-1]
solution(a2, b2)
    # result : -2