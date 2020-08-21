'''
BOJ, 2523 - 별찍기 13(https://www.acmicpc.net/problem/2523)

문제 : 예제를 보고 규칙을 유추한 뒤에 별을 찍어보세요.
입력 : 첫째 줄에 1이상 100이하의 수 N이 주어진다.
출력 : 첫째 줄부터 2xN-1번째 줄까지 차례대로 별을 출력한다.

'''

n = int(input())
[print("*"*i) for i in range(1, n+1)]
[print("*"*i) for i in range(n-1, 0, -1)]
#print("*"*i for i in range(n))