# 2581 - 소수

'''

자연수 M과 N이 주어질 때, M이상 N이하의 자연수 중 소수인 것을 모두 고르고,
이 소수들의 합과 최소값을 찾는 프로그램을 작성하는 것을 목표로 한다.

예를 들어, M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.


입력 : 첫째 줄에 M, 둘째 줄에 N이 주어진다(M, N은 10,000이하의 자연수이고, M은 N보다 작거나 같다)
출력 : M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최소값을 출력한다. 단, M이상 N이하의 범위에 소수가 없다면 -1을 출력한다

'''

#####################################################
#####################################################

M = int(input())
N, s = int(input()), []

def sosu(num) : 
    if num == 1 : return False
    for i in range(2, num) :
        if num % i == 0 : return False
    return True

for m in range(M, N+1) :
    if sosu(m) : s.append(m)

if len(s) : print(sum(s));print(s[0])
else : print(-1)