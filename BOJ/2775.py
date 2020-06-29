# 2775 - 부녀회장이 될테야

# 아파트 거주 조건 : a층 b호에 살기 위해서는 (a-1)층에 1호부터 b호까지 사람들의 수 합 만큼 사람들을 데려와 살아야 한다
# 아파트에 빈 집은 없고, 모든 거주민들이 계약 조건을 지키고 있다고 가정한다
# 양의 정수 k와 n에 대해서 k층, n호에는 몇 명이 살고 있는지 출력하는 프로그램 작성

# 단, 아파트의 층수는 0층부터, 호수는 1호부터 시작한다
# 또한 0층의 i호에는 i명이 산다

# 입력 : Test case의 수 T(층수), 정수 k, 정수 n(호수) - (1 <= k <= 14, 1 <= n <= 14)
# 출력 : 각 Test case에 대한 거주민 수 출력


#############################################################

# 1. 입력에 대한 처리
    ## 빠르게 하기 위해서 sys.stdin.readline()으로 처리

# 2. 문제 풀이
    ## 간단하게는 2차원 배열을 만들어서 처리하면 될 것이다
    ## 시간 초과가 걱정되긴 하지만


#############################################################

# 여기는 의미 없음
'''
import sys, numpy as np

K = int(sys.stdin.readline())
N = int(sys.stdin.readline())
arr_2 = np.ones((K, N), dtype=int) # 아파트 모양 짓고
print(arr_2)
arr_2[0] = [(n+1) for n in range(N)] # 1층 설정하고
print(arr_2)


arr = [[n for n in range(N)] for k in range(K)]
print(arr)
'''
# T = int(sys.stdin.readline()) # 더 빠른 입력 방법
# for i in range(T) :
#     k = int(sys.stdin.readline())
#     n = int(sys.stdin.readline())
#     arr = [x for x in range(14)][14]
#     print(arr)
#     print(i, k, n)    


#############################################################

#############################################################

# 3. 규칙 탐색
    ## 덧셈의 연속, 결국 시간 복잡도를 해결해야 하는 문제라고 생각
    ## 단순 연산의 반복 문제는 규칙을 제대로 찾아야 한다
    ## 규칙 파악을 위해서 층 수와 사람 수를 계산해보자

    ## 0층 : 1 | 2 | 3  | 4  | ... | n-1 | n
    ## 1층 : 1 | 3 | 6  | 10 | ... | ... | n(n+1)/2
    ## 2층 : 1 | 4 | 10 | 20 | ... | ...  




#############################################################

#############################################################


# import sys

# T = int(sys.stdin.readline()) # 더 빠른 입력 방법
# for i in range(T) :
#     k = int(sys.stdin.readline())
#     n = int(sys.stdin.readline())
#     print(i, k, n)

'''
#############################################################

#############################################################

#############################################################
'''

# 집에서

#####################################
# 만들어 나가는 코드

# # import sys

# K = int(sys.stdin.readline())
# N = int(sys.stdin.readline())
# print(K, N)

# arr = [[x+1 for x in range(N)] for y in range(2)]
# print(arr)

# h = 0

# arr[1] = [sum(arr[0][:x+1]) for x in range(N)]
# print(arr)

# while K != 1 and h != K :
#     h += 1
#     print(h, arr)
#     arr[0], arr[1] = arr[1], [sum(arr[0][:x+1]) for x in range(N)]

# print(arr[0])
# print(K, N, arr[0][N-1])

#####################################
# 확인용 코드 ... 

# import sys

# T = int(sys.stdin.readline())
# for t in range(T) :
#     K = int(sys.stdin.readline())
#     N = int(sys.stdin.readline())

#     arr = [[x+1 for x in range(N)] for y in range(2)]
#     h = 0
#     while K != 1 and h != K :
#         print(h, arr)
#         #arr[0], arr[1] = arr[1], [sum(arr[0][:x+1]) for x in range(N)]
#         arr = [arr[1], [sum(arr[0][:x+1]) for x in range(N)]]
#         h += 1

#     print(K, N, arr[0][N-1])

#####################################

# 예제 케이스는 다 돌아감 // 하지만 틀렸다고 함

# import sys
# T = int(sys.stdin.readline())
# for t in range(T) :
#     K = int(sys.stdin.readline())
#     N = int(sys.stdin.readline())
#     h, arr = 0, [[x+1 for x in range(N)] for y in range(2)]
#     while K != 1 and h != K :
#         h += 1
#         arr[0], arr[1] = arr[1], [sum(arr[0][:x+1]) for x in range(N)]
#         print(h, arr)
#     print(arr[1][N-1])

# 반례가 뭐가 있을까 ....

# 3
# 4
# 1 [[1, 2, 3, 4], [1, 3, 6, 10]]
# 2 [[1, 3, 6, 10], [1, 3, 6, 10]]
# 3 [[1, 3, 6, 10], [1, 4, 10, 20]]
# 4 [[1, 4, 10, 20], [1, 4, 10, 20]]
# 5 [[1, 4, 10, 20], [1, 5, 15, 35]]

# 왜 두번씩 돌까?????

#####################################

#
# import sys
# T = int(sys.stdin.readline())
# for t in range(T) :
#     K = int(sys.stdin.readline())
#     N = int(sys.stdin.readline())
#     h, arr = 0, [[x+1 for x in range(N)] for y in range(2)]
#     while K != 1 and arr[1][1]-2 != K :
#         h += 1
#         #arr[0], arr[1] = arr[1], [sum(arr[0][:x+1]) for x in range(N)]
#         arr = [arr[1], [sum(arr[0][:x+1]) for x in range(N)]]
#         print(h, arr)
#     print(arr[1][N-1]) 

# import sys
# T = int(sys.stdin.readline())
# for t in range(T) :
#     K = int(sys.stdin.readline())
#     N = int(sys.stdin.readline())
#     h, arr = 0, [[x+1 for x in range(N)] for y in range(2)]
#     while K >= 1 and int(h-0.5) != K :
#         h += 0.5
#         arr = [arr[1], [sum(arr[0][:x+1]) for x in range(N)]]
#         print(h, arr)
#     print(arr[0][N-1]) 

#####################################

#####################################

#####################################

# 배열에 층수를 입력
import sys
T = int(sys.stdin.readline())
for t in range(T) :
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    h, arr = 0, [[x+1 for x in range(N)]+[y] for y in range(2)]
    while K >= 1 and int(arr[1][-1]) <= K :
        h += 1
        arr[0] = arr[1]
        arr[1] = [sum(arr[0][:x+1]) for x in range(N)]+[h+1]
    print(arr[1][N-1])