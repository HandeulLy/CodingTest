
'''
# 문제
    - 정수 배열 numbers가 주어질 때, 서로 다른 인덱스에 있는 두 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return
    
# 제한 조건
    - numbers의 길이는 2이상 100이하
    - numbers의 모든 수는 0이상 100이하
'''

# # T1
# def solution(numbers):
#     answer = []
#     n_len = len(numbers)
    
#     for i in range(n_len-1) : 
#         for j in range(i+1, n_len) : 
#             if numbers[i] + numbers[j] not in answer : 
#                 answer.append(numbers[i]+numbers[j])
    
#     answer.sort()
    
#     return answer

# T2
def solution(numbers):
    answer = set([])
    n_len = len(numbers)
    
    for i in range(n_len-1) : 
        for j in range(i+1, n_len) : 
            answer.add(numbers[i]+numbers[j])
    
    return sorted(list(answer))

###########################################################

# ex1
numbers1 = [2,1,3,4,1]
    # answer1 = [2,3,4,5,6,7]

# ex2
numbers2 = [5,0,2,7]
    # answer2 = [2,5,7,9,12]