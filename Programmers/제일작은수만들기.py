# 먼저 제일 작은 수를 리스트에서 삭제하고
# 리스트 길이에 따라서 반환 값을 다르게


def solution(arr):
    arr.remove(min(arr))
    return [-1] if len(arr)==0 else arr