# 입력 : 문자열 s(알파벳 대/소문자와 공백으로 이루어짐), 자연수(1이상 25이하)
# 출력 : 문자열 s를 n만큼 민 암호문을 반환
# 조건 : 각 문자들을 확인할 때 스페이스(공백)이면 그대로 출력해야 함
​
# 파이썬에서 아스키코드를 사용하는 방법
# 문자형을 정수형으로 : ord() 이용
# 정수형을 문자형으로 : chr() 이용
​
# 입력받은 문자가 소문자인지 대문자인지에 따라서 연산을 각각 수행해야함
# 문자의 ord() 값이 소문자 영역(a=97 ~ z=122) / 대문자 영역(A=65 ~ Z=90)
# ord() + n 의 값이 다시 영역 값에 들어오도록 연산을 해줘야 함

def solution(s, n):
    answer = ''
    for i in range(len(s)) :
        if s[i] == ' ' : # 공백인 경우
            answer += ' '
        elif 97 <= ord(s[i]) <= 122 : # 소문자인 경우
            answer += chr(((ord(s[i])+n-97) % 26 + 97))
        else : # 대문자인 경우
            answer += chr( (ord(s[i])+n-65) % 26 + 65)                
    return answer