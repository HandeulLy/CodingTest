'''

2798번, 블랙잭

문제
- N장의 카드, 숫자 M이 주어진다.
- N장의 카드 중 3장의 카드를 골라 M을 넘지 않으며 M과 최대한 가까운 수를 만든다.

입력
- 카드의 개수 N : 3이상 100이하
- 카드에 적힌 수 : 100,000이하
- 숫자 M : 10이상 300,000이하

출력
- M을 이하이면서 M과 최대한 가까운 카드 3장의 합

'''

'''

풀이
- 처음에는 리스트를 정렬하고, M을 3으로 나눈 값을 찾은 뒤 앞 뒤 숫자들을 더해보는 방식을 생각했다
- 예를 들어, M=21이고 카드는 [5, 6, 7, 8, 9]인 경우에 21을 3으로 나눈 값은 7이다.
- 7과 제일 가까운 카드 3개를 찾아서, 6 7 8을 선택한다.
- 하지만 이는 '모든 경우'에 해당되지 않을 것으로 판단했다.

- 그래서 그냥 3중 for loop를 구현하기로 했다.
- 조합을 지원하는 itertools 라이브러리가 있긴 하지만, 최대한 안쓰고 하려고 했다.

'''
N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
for i in range(N) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :
            tmp = nums[i] + nums[j] + nums[k]
            if tmp in range(answer, M+1) : answer = tmp
print(answer)