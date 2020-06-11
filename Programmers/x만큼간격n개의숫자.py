# 입력 : 정수 x, 자연수 n
# 목표 : x부터 시작해서 x씩 증가하는 숫자 n개를 원소로 갖는 리스트 반환

def solution(x, n):
    return [ x*i for i in range(1, n+1) ]