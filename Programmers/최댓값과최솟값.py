'''

문자열 s에는 공백으로 구분된 숫자들이 저장되어 있다.
이 숫자 중 최소/최대 값을 찾아 "min max"의 형태로 반환하는 프로그램을 작성하라.

'''

def solution(s):
    a = s.split()
    a_i = [int(i) for i in a]
    return str(min(a_i))+" "+str(max(a_i))