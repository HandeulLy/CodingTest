'''

[골드바흐의 추측]
- 링크 : https://www.acmicpc.net/problem/9020

문제
- 골드바흐 수 : 2보다 큰 모든 짝수는 두 소수의 합이다.
- 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라 한다.
- 10,000보다 작거나 같은 모든 짝수 n에 대해 골드바흐 파티션은 존재한다.
- 2보다 큰 짝수 n이 주어질 때, n의 골드바흐 파티션을 출력하라.
- 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우, 두 소수의 차이가 가장 작은 것을 출력하라.

입력
- 첫 줄에 테스크 케이스 개수가 주어진다.
- 각 테스트 케이스는 한 줄로 이루어져 있고, 짝수 n(4이상, 10000이하)이 주어진다.

출력
- 각 테스트 케이스에 대해 주어진 n의 골드바흐 파티션 출력
- 출력하는 소수는 작은 것 먼저, 공백으로 구분

'''

'''

풀이
먼저, 10000의 절반인 5000까지의 소수를 구하고 저장해 둔다.

임시 리스트, n의 절반
1부터 절반까지 ... i를 반복
n-i가 리스트에 있는지 조회, 있으면 갱신 없으면 그대로.
for 문을 ㄷ다 돌면 출력

'''

import sys

def sosu(n) :
    for i in range(2, int(n**0.5+1)) :
        if n % i == 0 : return False
    return True

p = []
for i in range(2, 10000) :
    if sosu(i) : p.append(i)

for _ in range(int(input())) :
    n = int(sys.stdin.readline())
    for i in range(n//2, 1, -1) :
        if i in p and n-i in p :
            a, b = i, n-i
            break
        else : pass
    print(a, b)