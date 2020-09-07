'''

10814번, 나이순 정렬
링크 : https://www.acmicpc.net/problem/10814

문제
- 나이와 이름이 가입한 순서대로 주어진다.
- 이 때, 회원들을 나이가 중가하는 순으로, 나이가 같으면 먼저 가입한 순서로 정렬하는 프로그램을 작성하라.

입력
- 첫째 줄에 회원 수 N(1이상 100,000이하)
- 둘째 줄부터 각 회원의 나이와 이름이 공백으로 구분되어서 주어짐
- 나이는 1이상 200이하의 정수
- 이름은 알파벳 대소문자로 이루어지고, 길이가 100 이하의 문자열
- 입력은 가입한 순서로

출력
- 나이 순, 가입 순, 으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력

'''

'''
딕셔너리를 이용하면 간단하게 풀 수 있다고 생각했다.
키를 나이로, 벨류에는 이름과 가입 순서를 포함하는 딕셔너리 구조를 만든다.
정렬할 때, 키를 1순위, 가입 순서를 2순위로 진행한다.
결과를 공백으로 구분지어서 출력하면 된다.
'''

########################################################

# solution ver 1

import sys

users, info = [], ""

for i in range(int(input())) :
    info = sys.stdin.readline().split()
    users.append([int(info[0]), i, info[1]])

users = sorted(users, key = lambda x : (x[0], x[1]))

[print(i[0], i[2]) for i in users]

########################################################

# solution ver 2

import sys

users, info = dict(), ""

for i in range(int(input())) :
    info = sys.stdin.readline().split()
    if int(info[0]) in users.keys() : users[int(info[0])].append([i, info[1]])
    else : users[int(info[0])] = [[i, info[1]]]

users = sorted(users.items(), key = lambda x : (x[0], x[1]))
[print(u[0], u[1][k][1]) for u in users for k in range(len(u[1]))]