# 아이디어는 비슷한데 표현이 다르다
# sum()과 간편한 for문을 사용했다는 점에서 더 괜찮다고 생각한다
def solution_ver2(n):
    return sum([int(i) for i in str(n)])

# map()에 대해 자세히 학습하고, 잘 응용해야 할 필요성을 느꼈다
def solution_ver3(n):
    return sum(map(int, str(n)))

# 내가 작성한 것
def solution(n):
    answer = 0
    for i in range(1, 10) : answer += i * str(n).count(str(i))
    return answer

input_n = 987
solution(input_n)

s = "cdcd"
s = [i for i in s]
con = True
while con : 
    for i in range(len(s)-1) :
        if s[i] == s[i+1] : s[i], s[i+1] = 0, 0
    if len(s) != 0 and 0 not in s :
        print(1)
        con = False
    s = [i for i in s if i != 0]
    if len(s) == 0 :
        print(-1)
        con = False
    
print(s)

a = [1,2,3,4,5]
print( len([i for i in a if i >= 3]) )