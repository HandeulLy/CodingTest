'''

[좌표 정렬하기 2]
- 링크 : https://www.acmicpc.net/problem/11651

문제
- 2차원 평면 위에 점 N개
- 좌표를 Y좌표가 증가하는 순, Y가 같으면 X좌표가 증가하는 순서로 정렬

입력
- 첫 줄에 점의 개수 N개(1이상 10만 이하)
- 둘째 줄부터는 N개의 점에 해당하는 x, y좌표
- 각 좌표는 -10만~10만 사이의 정수
- 위치가 같은 두 점은 없다

출력
- N개의 줄에 점을 정렬한 결과 출력

'''

'''
11650 번과 동일한 프로세스지만, 정렬 우선순위를 y좌표에 먼저 둔다
그러기 위해서, 딕셔너리의 key-value 쌍의 위치를 바꿨다
'''

import sys

n, points = int(input()), dict()

for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    if y in points.keys() : points[y].append(x)
    else : points[y] = [x]

for y in sorted(points.items(), key=lambda x:x[0]) :
    for x in sorted(y[1]) :
        print(x, y[0])
