def solution(s):
    answer = ''    
    point = 0 # 단어마다 인덱스를 구하기 위한 변수
    for i in range(len(s)) :
        if s[i] == ' ' : # 공백일 떄 공백을 추가하고, 포인트 값 수정
            answer += s[i]
            point = -1
        else : # 문자일 때 포인트의 짝/홀수에 따라서 대/소문자 추가
            if point % 2 == 0 : answer += s[i].upper()
            else : answer += s[i].lower()
        point += 1 # 인덱스 번호 1 증가
        print(answer)
    return answer

input_s = "try hello world"
solution(input_s)

aaa = ['5', '4', '0']
print(aaa)
bbb = list(map(int, aaa))
print(bbb)
ccc = 13524
print(ccc)
print(type(ccc))
ccc = str(ccc)[:]
print(ccc)
print(type(ccc))
ccc = list(map(int, ccc))
ccc.reverse(True)
print(ccc)