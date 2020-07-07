def solution(n):
    answer = ''
    n = sorted(str(n), reverse=True)[:]
    for i in n : answer += i
    return int(answer)

'''

추가 

다른 사람 코드 보기 참고
마지막 2줄을 아래처럼 줄일 수 있음

# ver1
for i in n : answer += i
return int(answer)

# ver2
return int("".join(n))

'''