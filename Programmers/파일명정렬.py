def solution(files):
    d = dict()
    
    for f_name in files :
        i_n, i_t = 0, len(files)
        for i, f in enumerate(f_name) :
            if f.isdigit() and not f_name[i-1].isdigit() : i_n = i
            if i_n and not f.isdigit() and f_name[i-1].isdigit() : i_t = i; break        
        d[f_name] = f_name[:i_n].lower(), int(f_name[i_n:i_t])
        print(d)
    answer = [f_n for f_n, f_i in sorted(d.items(), key=lambda x: (x[1][0], x[1][1]))]    
    return answer

'''

링크 : https://programmers.co.kr/learn/courses/30/lessons/17686

정렬 기준 : 단순한 문자 코드가 아니라 숫자를 반영한 정렬 기능 구현

파일명 기준
    - 100글자 이내
    - 영문 대소문자 + 숫자 + 공백(" ") + 마침표(".") + 빼기("-")로 구성
    - 영문자로 시작, 숫자를 하나 이상 포함
    - 크게 3부분으로 구성 됨 : Head, Number, Tail
    - H : 숫자가 아닌 문자, 최소 한 글자 이상
    - N : 한 글자에서 최대 다섯 글자 사이의 연속된 숫자(0~99999, 00000, 0101 모두 가능)
    - T : 나머지 부분, 숫자가 올 수도, 아무 글자가 없을 수도 있음

정렬 기준
    - 우선 Head 부분을 기준으로, 사전 순으로 정렬
      (대소문자는 구분하지 않음)
    - Head 부분이 대소문자 차이 외에 같은 경우, Number 부분의 숫자 순으로 정렬
      (숫자 앞의 0은 무시하기 때문에 012과 12는 같은 값으로 처리)
    - Head와 Number 부분이 같은 경우, 원래 입력된 순서를 유지
    
입력
    - 배열 files, 1000개 이하의 파일명을 포함한 문자열 배열
    - 각 파일명은 100글자 이하이며, 영문 대소문자, 숫자, 공백, 마침표, 빼기부호로 구성됨
    - 파일명은 영문자로 시작, 숫자를 하나 이상 포함
    - 중복된 파일명은 없으나, 대소문자나 숫자 앞 부분의 0 차이가 있는 경우는 존재
      (muzi1.txt, MUZI1.txt, muzi001.txt, muzi1.TXT는 함께 입력으로 주어질 수 있음)

출력
    - 위 기준을 따라 정렬된 배열 리턴

'''

i_f = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
#print(solution(i_f)) # ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

i_f = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
#print(solution(i_f)) # ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

i_f = ["foo9.txt", "foo010bar020.zip"]
#print(solution(i_f)) # ["foo9.txt", "foo010bar020.zip"]

i_f = ["f9", "f010bar020.zip"]
print(solution(i_f)) # ["foo9.txt", "foo010bar020.zip"]