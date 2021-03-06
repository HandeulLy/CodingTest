
'''
# 문제
    - 구명보트는 한 번에 최대 2명만 탈 수 있다
    - 사람들의 몸무게를 담은 배열 people과 구명보트의 최대 하중 무게 limit가 매개변수로 주어진다
    - 모든 사람을 구출하기 위해 필요한 구명보트의 최솟값을 반환하라

# 제한조건
    - 사람은 1명 이상 50,000명 이하
    - 각 사람의 몸무게는 40 이상 240 이하
    - 구명보트의 무게 제한은 40 이상 240 이하
    - 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최대값보다 크게 주어지기 때문에 구출할 수 없는 경우는 없다
'''

'''
투 포인터로 해결하면 되지 않을까?
people을 정렬한 뒤, 가장 가벼운 사람과 가장 무거운 사람을 가리킨다.

먼저, 제일 무거운 사람은 무조건 태운다.
그리고 여기에 가장 가벼운 사람 몸무게를 더해서 limit 보다 작으면 같이 태우고,
limit을 초과하면 그냥 가장 무거운 사람 혼자만 태운다.
무거운 사람은 탔으니 그 다음으로 무거운 사람한테 포인터를 이동한다.

위 과정을 반복한다.
'''

##########################################

def solution(people, limit):
    answer = 0
    people = sorted(people)
    i, j = 0, len(people)-1
    print(people)
    while i <= j : 
        if people[j] + people[i] > limit : 
            pass
        else : 
            i += 1
        j -= 1
        answer += 1

        print(i, j, answer)
    return answer
    
##########################################

p1 = [70, 50, 80, 50]
l1 = 100
solution(p1, l1) # return 3

p2 = [70, 80, 50]
l2 = 100
solution(p2, l2) # return 3