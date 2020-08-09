def solution(nums):
    answer = []
    for n in nums :
        if n not in answer : 
            answer.append(n)
    l_a, l_n = len(answer), len(nums)
    return l_n//2 if l_a >= l_n//2 else l_a

'''

링크 : https://programmers.co.kr/learn/courses/30/lessons/1845

N/2 마리의 몬 선택하는 방법을 찾아야 함

입력 : N마리의 몬 종류 번호가 담긴 배열 NUMS, 배열 길이는 1이상 10000이하이고 항상 짝수
출력 : 몬 종류 번호의 개수를 반환

'''

i_n = [3,1,2,3]
print(solution(i_n)) # 2

i_n = [3,3,3,2,2,4]
print(solution(i_n)) # 3

i_n = [3,3,3,2,2,2]
print(solution(i_n)) # 2