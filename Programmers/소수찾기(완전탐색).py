
'''
# 문제
    - 문자열 numbers가 주어질 때, 숫자로 만들 수 있는 소수의 개수를 return

# 제한조건
    - numbers : 길이가 1이상 7이하인 문자열
    - numbers의 원소는 0~9까지의 숫자만으로 이루어짐
'''

'''
크게 2 단계로 나누어진다고 생각.
먼저, numbers 안의 문자열들을 조합해서 가능한 모든 숫자의 조합을 찾는 것.
그리고 그 숫자들이 소수인지 아닌지 판단하는 것.

각 문자들의 조합을 통해 만들 수 있는 숫자를 리스트에 저장하고,
그 리스트 안에 원소들을 int로 변환하면서 '가능한 숫자'들만 남긴다.
여기서 17과 71이 모두 가능하다고 했기 때문에 '순열'의 개념으로 접근했다.

각 숫자들이 소수인지 판별하기 위해서 숫자 하나마다 체크하지말고,
가장 큰 숫자까지의 소수들을 모두 구한 다음 한번에 확인하면 되지 않을까?

'''

##########################################
'''
import itertools

def solution(numbers):
    answer = 0
    nums = []

    for i in range(1, len(numbers)+1) : 
        nums += list(itertools.permutations(numbers, i))
    print(nums)

    for j in range(len(nums)) : 
        nums[j] = int("".join(nums[j]))
    print(nums)

    m = max(nums)+1
    sosu = set(range(3, m+1, 2))
    for i in range(3, m+1, 2) :
        if i in sosu :
            sosu = sosu - set(range(i*2, m+1, i))
    print(sosu)

    for n in set(nums) :
        if n in sosu : answer+=1
    print(answer)
    
    return answer
'''

##########################################

'''
import itertools

def solution(numbers):
    answer = 0
    tmp, nums = [], []

    for i in range(1, len(numbers)+1) : 
        tmp += list(itertools.permutations(numbers, i))
        for t in tmp : 
            if int("".join(t)) not in nums : nums.append(int("".join(t)))
    
    def s(m) : 
        for i in range(2, int(m**0.5+1)) :
            if m%i==0 : return False
        return True
    
    nums = set(nums)
    m = max(nums)+1
    sosu = [2]
    for i in range(3, m, 2) :
        if s(i) : sosu.append(i)
    
    for n in nums :
        if n in sosu : answer+=1
    
    return answer
'''
    
##########################################

import itertools

def solution(numbers):
    answer = 0
    tmp, nums = [], []

    for i in range(1, len(numbers)+1) : 
        tmp += list(itertools.permutations(numbers, i))
        for t in tmp : 
            if int("".join(t)) not in nums : nums.append(int("".join(t)))
    
    def s(m) : 
        for i in range(2, int(m**0.5+1)) :
            if m%i==0 : return False
        return True
    
    nums = set(nums)
    m = max(nums)
    s = [False, False] + [True]*(m)
    sosu = []
    for i in range(2, m+1) :
        if s[i] :
            sosu.append(i)
            for j in range(2*i, m+1, i) :
                s[j] = False
    
    for n in nums :
        if n in sosu : answer+=1
    
    return answer
    
##########################################

print("\n#### CASE1 ####")
n1 = "17"
solution(n1) # answer : 3

print("\n#### CASE2 ####")
n2 = "011"
solution(n2) # answer : 2

print("\n#### CASE3 ####")
n3 = "9999999"
solution(n3) # answer : 

##########################################