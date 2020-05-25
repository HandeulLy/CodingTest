# sol1
def solution(n):
    answer = list(map(int, str(n)[:]))
    return list(reversed(answer))

# sol2
def solution(n):
    return list(map(int, reversed(str(n))))

# sol3
def solution(n):
    return [int(i) for i in str(n)][::-1]