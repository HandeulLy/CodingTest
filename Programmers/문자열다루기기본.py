# 입력 : 길이가 1이상 8이하인 문자열
# 출력 : 문자열이 숫자로만 된거면 True, 문자가 섞여 있으면 False
​
# 처음에는 간단하게 s == int(s) 의 결과를 반환하면 되지 않을까 생각했다
# 하지만 문자/문자열을 정수형으로 형변환 할 수 없기 때문에 다른 아이디어가 필요하다
​
# s의 각 원소들이 숫자인지 확인해야한다
# 숫자가 아니라면 그 순간 False를 반환하고, s의 마지막 원소까지 확인했을 때도 문제가 없다면 True를 반환


# Sol 1
def solution(s):
    integers = [str(i) for i in range(0, 10)]
    if len(s) != 4 and len(s) != 6 : return False
    for i in range(len(s)) :
        if s[i] not in integers : return False
    return True

# Sol 2
def solution(s):
    integers = [str(i) for i in range(0,10)]
    
    if len(s) != 4 and len(s) != 6 : return False
    
    if sorted(s)[-1] not in integers : return False
    return True