# sol 1
def solution(x):
    return True if x % sum([int(n) for n in str(x)]) == 0 else False

# ============================================
# sol 2
# 굳이 True/False를 명시하지 않아도, 이 등호 관계에서 T/F가 나오니까 이렇게 써도 괜찮음
return x % sum([int(n) for n in str(x)]) == 0