# 입력 : 자연수를 담은 배열 arr, 자연수 divisor
# 목표 : arr 원소들 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열 반환
# 예외 : divisor로 나누어 떨어지는 원소가 하나도 없다면 [-1]을 반환
 
def solution(arr, divisor):
    answer = []
    
    for i in arr :
        if i % divisor == 0 : answer.append(i)
    
    if answer == [] : return [-1]
    else : return sorted(answer)