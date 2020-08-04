'''

문제 링크
- https://programmers.co.kr/learn/courses/30/lessons/12911

문제 설명
- 자연수 n이 주어질 때, 아래 조건을 가지는 숫자를 반환해야 함

조건
1) n의 다음 큰 숫자는 n보다 큰 자연수
2) n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같다
3) n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수

제한 사항
- n은 1,000,000 이하의 자연수

예시
- n=78, return=83
- n=15, return=23

'''

def solution(n):
    n, m = bin(n), n
    while True :
        m+=1
        if n[2:].count('1') == bin(m)[2:].count('1') : return m

i_n = 15
print(solution(i_n)) # 23

i_n = 78
print(solution(i_n)) # 83