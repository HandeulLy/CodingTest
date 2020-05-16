'''
https://blog.naver.com/handuelly/221682684980

일곱 난장이의 키 합은 100이다
입력 : 9번 진행되고, 각 값은 서로 다르고(중복 없음) 100을 넘지 않는 자연수이다.
출력 : 가능한 일곱 난장이의 키를 오름차순 정렬한 리스트 형식
못 찾는 경우는 없음(항상 정답이 있다)

예) 20 7 23 19 10 15 25 8 13 => 7 8 10 13 19 20 23

완전 탐색(또는 브루트 포스) 문제를 연습하기 위해 이 문제를 선택
'무식한' 풀이... 그래도 시간/공간의 효율을 생각한 '(덜) 무식한' 풀이를 해보자
전체 중에서 7개를 선택해서 총 합이 100이면 그 리스트를 정렬해서 출력
7개를 선택하는 것 보다는 2개를 선택해서 9개의 합에서 빼는게 낫지 않을까?
'''

heights = [int(input()) for i in range(9)]
heights.sort()
sum_heights = sum(heights)
for i in heights :
    for j in heights :
        if i != j and sum_heights - (i + j) == 100 :
            heights.remove(i)
            heights.remove(j)
            break
    if len(heights) == 7 : break
for a in heights :
    print(a)
