'''
https://programmers.co.kr/learn/courses/30/lessons/12949?language=python3

2차원 행렬 arr1과 arr2를 입력받아, 곱한 결과를 반환하는 코드를 작성

조건
1) 행렬 arr1, arr2의 행과 열의 길이는 2이상 100이하
2) 행렬 arr1, arr2의 원소는 -10이상 20이하인 자연수
3) 곱할 수 있는 배열의 형태만 주어짐
'''

'''
def solution(arr1, arr2):
    answer = [[0]*len(arr2[0])]*len(arr1)

    for i in range(len(arr1)) :
        for j in range(len(arr2[0])) :
            for k in range(len(arr1[0])) :
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer
    
def solution(arr1, arr2):
    answer = [[0]*len(arr2[0])]*len(arr1)

    for i in range(len(arr1)) :
        for j in range(len(arr2[0])) :
            temp = 0
            for k in range(len(arr1[0])) :
                temp += arr1[i][k] * arr2[k][j]
            #answer[i][j] = temp
            print(i, j, k, temp)
    return answer
'''

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)) :
        row = []
        for j in range(len(arr2[0])) :
            temp = 0
            for k in range(len(arr1[0])) :
                temp += arr1[i][k] * arr2[k][j]
            row.append(temp)
        answer.append(row)
    return answer

i_arr1 = [[1, 4], [3, 2], [4, 1]]
i_arr2 = [[3, 3], [3, 3]]
print(solution(i_arr1, i_arr2))
# [[15, 15], [15, 15], [15, 15]]

i_arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
i_arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(i_arr1, i_arr2))
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]


