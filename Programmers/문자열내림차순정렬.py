def solution(s):
    # 문자가 갖는 아스키코드 값을 이용해서 정렬하면 된다고 생각
    # 문자열 변수에는 sort() 메소드를 사용할 수 없는 것 같다

    s = sorted(s, reverse=True)
    print("s = {} \t type of s = {}".format(s, type(s)))
    return ''.join(sorted(s, reverse=True))


input_s = "Zbcdefg"
solution(input_s)