'''

[수 정렬하기]
- 링크 : https://www.acmicpc.net/problem/2751

- 문제 : N개의 수가 주어질 때, 이를 오름차순으로 정렬하는 프로그램 작성
- 입력 : 처음에 1이상 1,000,000이하의 N을 입력 받고, 둘째 줄부터 N개의 숫자를 입력 받음(각 숫자는 절대값이 1,000,000 이하의 정수이고 중복 없음)
- 출력 : 첫째 줄부터 N번 줄까지, 입력받은 숫자를 오름차순으로 정렬하여 출력

'''

# 시간 초과
# [print(i) for i in sorted([int(input()) for _ in range(int(input()))])]

import sys
[print(i) for i in sorted([int(sys.stdin.readline())
          for _ in range(int(sys.stdin.readline()))])]