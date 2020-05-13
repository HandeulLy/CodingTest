def solution(a, b):
    answer, temp = 0, 0
    if a>b : # a가 더 작은 값을 갖도록
        temp = a
        a = b
        b = temp
    for i in range(a, b+1) :
        answer += i

    return answer

def solution2(a, b):
    answer = 0
    if a > b : # a가 더 작은 값을 갖도록
        a , b = b, a       
    answer = sum(range(a, b+1))
    
    return answer