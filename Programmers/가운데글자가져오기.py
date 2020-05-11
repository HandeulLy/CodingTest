def solution(s):
    answer = ''
    size = len(s) # 문자열의 길이를 저장

    if size%2 == 0 : # 단어의 길이가 짝수라면 가운데 두글자
        answer = s[int(size/2-1):int(size/2+1)]
    else : # 홀수라면 가운데 한글자
        answer += s[int((size-1)/2)]
    
    return answer

def solution2(s):
    return s[(len(s)-1)//2:len(s)//2+1]

print(solution("abc"))
print(solution2("abc"))