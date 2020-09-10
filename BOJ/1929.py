# 19291 - 소수 구하기

'''
M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하는 것이 목표다.

입력 : 첫째 줄에 M과 N이 빈칸을 사이에 두고 주어ㅣ는데, 1 ≤ M ≤ N ≤ 1,000,000의 범위를 갖는다.
출력 : 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

'''


#####################################################
#####################################################

'''
M, N = map(int, input().split())
for m in range(M, N+1) :
    if m == 1 or m % 2 == 0 : continue
    sosu = True
    for i in range(2, m) :
        if m % i == 0 : sosu = False
    if sosu : print(m)
'''

# 시간 초과 오류


#####################################################
#####################################################

# 소수를 빠르게 구하는 방법을 고민해야 한다
# 매번 2부터 for loop를 수행하지말고, 그 전에 저장한 소수로만 검색하면 연산이 줄어들지 않을까?

# 여기 참고
# https://ggodol.tistory.com/entry/%EC%86%8C%EC%88%98-%EA%B5%AC%ED%95%98%EB%8A%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

'''
M, N = map(int, input().split())

def sosu(num) :
    S, n = [2], 3
    while n <= num :
        for s in S :
            if n % s == 0 : break
            elif s == S[-1] : S.append(n); print(n); break
        n+=1
    return S
'''

# #print(sosu(N)[1:]) if M > 2 else print(sosu(N))
# sosu(N)

# 이거도 시간 초과...
# 어차피 출력 형태가 다르긴 하네 -- 수정하긴 함(그래도 느림) + 그리고 틀림(1부터 뽑으니까...M이 아니라)


#####################################################
#####################################################

'''
M, N = map(int, input().split())
numSet, S, m = set(range(M, N+1)), [], M

for i in range(2, N) :
    delSet = {j for j in numSet if j%i==0}
    if len(delSet) : S.append(min(delSet))
    print(i, " --- ", numSet, " & ", delSet, " == ", S)
    numSet -= delSet

for i in S : print(i)
'''

# S = [2]
# numSet = set(range(1, 11))
# nums = {i for i in numSet if i%S[0]==0 }

# print(S, numSet)
# print(nums, len(nums))


#####################################################
#####################################################

def sosu(n) :
    if n == 1 : return False
    for i in range(2, int(n**0.5+1)) :
        if n % i == 0 : return False
    return True

a, b = map(int, input().split())
p = []

for i in range(a, b+1) :
    if sosu(i) : print(i)

# for i in range(a, b+1) :
#     if i in p : print(i)