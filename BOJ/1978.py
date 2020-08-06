# 1978 - 소수 찾기

# 주어진 N개 중에서 소수가 몇 개인지 출력하는 프로그램을 작성한다

# 입력 : 100 이하의 자연수 N이 입력되고, 다음으로 N개의 수가 주어지는데 각각은 1,000 이하의 자연수이다
# 출력 : 주어진 수들 중 소수의 개수를 출력한다


#####################################################
#####################################################


# N, a = int(input()), []
N = int(input())
a = input().split()

def sosu(num) : 
    if num == 1 : return False
    for i in range(2, num) :
        if num % i == 0 : return False
    return True

for idx, num in enumerate(a) :
    if sosu(int(num)) : a[idx] = -1

print(a)
print(a.count(-1))
