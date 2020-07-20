'''

# 입력 : number 리스트(원소의 값은 1이상 50이하, 길이는 2이상 20이하), 타겟 넘버(1이상 1000이하)
# 목표 : number 리스트 안에 있는 정수들에 적절히 +/- 연산으로 타겟 넘버 값을 만들어라
# 출력 : 타겟 넘버를 만들 수 있는 경우의 수를 반환

'''

#######################################################

'''

풀이
# 백준의 '일곱 난쟁이' 그리고 '퇴사' 문제랑 비슷한 방법으로 접근하면 될 것 같다
# 문제 카테고리는 BFS/DFS로 구분되긴 했는데 완전탐색이 필요하므로 브루트포스처럼 풀 수 있을 듯

'''

# answer = 0

# def solution(numbers, target):        
#     solve(numbers, target, 0, 0)    
#     return answer

# def solve(numList, value, indexPoint, sumValue) :
#     global answer
#     if indexPoint >= len(numList) :
#         if sumValue == value : answer += 1
#         return
    
#     solve(numList, value, indexPoint + 1, sumValue + numList[indexPoint])
#     solve(numList, value, indexPoint + 1, sumValue - numList[indexPoint])
#     solve(numList, value, indexPoint + 1, sumValue)

#######################################################

'''

이렇게 하니까 테스트케이스 5가 아니라 15 나옴

오류는 부분 집합의 합을 구하고 있다는 것
문제에서 요구하는 것은 전체 리스트에서 몇 개의 원소 부호를 바꿨을 때, 그 합이 target과 같은지 확인해야 함
(리스트에서 몇 개만 뽑아온 부분 집합의 합이 target과 같은지 구하는게 아님)

​
그러면 재귀함수로 보낼 때, +/- 두개를 구분할 필요가 없이 기존의 '부분 집합' 아이디어 그대로 가져가고
target과 같은지 비교하는 시점에서 (리스트 전체의 합) - (부분집합의 합)... 부분집합은 두번 빼야 함
예를 들어서, 전체는 [1, 1, 1, 1, 1] 인 리스트에서 [1]를 부분집합으로 뽑았다고 했을 때,
[1]을 한 번 빼면 [0, 1 , 1, 1, 1] 처럼 되고, 두 번 빼야 [-1, 1, 1, 1, 1]이다.

'''

answer = 0

def solution(numbers, target):
    solve(numbers, target, 0, 0)    
    return answer

def solve(numList, value, indexPoint, sumValue) :
    global answer
    if indexPoint == len(numList) :
        if sum(numList) - sumValue*2 == value : answer += 1
        return
    
    solve(numList, value, indexPoint + 1, sumValue + numList[indexPoint])
    solve(numList, value, indexPoint + 1, sumValue)