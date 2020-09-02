'''
    2108번, 통계학

    문제
    - N개(홀수)의 수가 주어질 때, 4가지 기본 통계값을 구하는 프로그램 작성
    - 산술평균 : N개의 수들의 합을 N으로 나눈 값
    - 중앙값 : N개의 수들을 증가하는 순서로 나열했을 때 그 중앙에 위치하는 값
    - 최빈값 : N개의 수들 중 가장 많이 나타나는 값
    - 범위 : N개의 수 중 최댓값과 최솟값의 차이

    입력
    - 첫째 줄 : N(1이상 500,000이하)의 개수
    - 다음 줄부터 : N개의 정수, 정수의 절대값은 4,000을 넘지 않는다

    출력
    - 산술평균(소수점 첫째 자리에서 반올림), 중앙값, 최빈값(여러개 있는 경우, 두번로 작은 값), 범위

'''

#############################################

# using [List] + {Dictionary}

import sys

arr, n = [], int(input())

for _ in range(n) :
    arr.append(int(sys.stdin.readline()))
arr.sort()

arr_dic = {}
for a in arr :
    if a in arr_dic : arr_dic[a] += 1
    else : arr_dic[a] = 1
arr_dic = sorted(arr_dic.items(), key=lambda x:(-x[1], x[0]))

print(round(sum(arr)/n))
print(arr[n//2])
if len(arr_dic) > 1 : 
    print(arr_dic[0][0] if arr_dic[0][1] != arr_dic[1][1] else arr_dic[1][0])
else : 
    print(arr_dic[0][0])
print(arr[-1]-arr[0])