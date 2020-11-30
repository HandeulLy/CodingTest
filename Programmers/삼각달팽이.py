
'''
# 문제
    - 정수 n
    - 아래 그림과 같이  밑변의 기링와 높이가 n인 삼각형
    - 맨 위 꼭지점부터 반시계 방향으로 숫자 채우기
    - 첫 행부터 마지막 행까지 모두 순서대로 담은 새로운 배열을 return

# 제한조건
    - n은 1이상 1,000이하
'''

# T1
def solution(n):
    answer = [[0]*n for _ in range(n)]
    
    num = 0
    mode = [[1, 0], [0, 1], [-1, -1]]
    x, y, m = -1, 0, 0

    while n > 0 :
        for i in range(n) :
            x += mode[m%3][0]
            y += mode[m%3][1]
            num += 1
            answer[x][y] = num
        m += 1
        n -= 1

    ans = []
    for i, a in enumerate(answer) : 
        ans += a[:i+1]

    return ans


##########################################

# ex1
n = 4
solution(n)
    # result : [1,2,9,3,10,8,4,5,6,7]

# ex2
n = 5
#solution(n)
    # result : [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]

# ex3
n = 6
#solution(n)
    # result : [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]