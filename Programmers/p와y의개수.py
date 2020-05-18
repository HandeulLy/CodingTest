def solution(s):
    
    return s.count('p') + s.count('P') == s.count('y') + s.count('Y')

input_s = "pPoooyY"
print(solution(input_s))
input_s = "Pyy"
print(solution(input_s))