'''

[좌표 정렬하기 1]
- 링크 : https://www.acmicpc.net/problem/11650

문제
- 2차원 평면 위 점 N개가 주어진다.
- 좌표를 X 좌표가 증가하는 순서, X 좌표가 같으면 Y 좌표가 증가하는 순서로 정렬하라

입력
- 첫 줄에 점의 개수 N(1이상 10만 이하)
- 둘째 줄부터 N개의 줄에는 i번점의 x, y 좌표가 주어진다
- x,y의 값은 -10만 ~ 10만의 정수이다
- 위치가 같은 두 점은 없다

출력
- 첫째 줄부터 N개의 줄에 점을 정렬한 결과 출력

'''

'''
딕셔너리로 풀면 되지 않을까?
x를 키로, y를 벨류로 두고.
'''

import sys

n, points = int(input()), dict()
for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    if x not in points.keys() : points[x] = [y]
    else : points[x].append(y)

points = sorted(points.items(), key=lambda x:x[0])
for x in points :
    for y in sorted(x[1]) :
        print(x[0], y)
