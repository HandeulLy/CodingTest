def solution(priorities, location):
    answer = 0
    size = len(priorities) # 입력 리스트 크기
    temp = [0] * size # 출력되는 순서를 저장할 임시 리스트 선언
    point = 0 # 가장 높은 우선순위를 가지는 작업을 가리킬 인덱스
    count = 1 # 출력되는 순서

    while temp[location] == 0 : # 원하는 위치의 순서를 구할 때 까지 수행
        aaa = priorities[point:] + priorities[:point] # 높은 우선순위를 0번 인덱스로 갖는 임시 리스트 생성
        point = (aaa.index(max(priorities)) + point ) % size
        # 임시 리스트에서 새롭게 가져온 가장 높은 우선순위의 인덱스를 가져오고
        # 원래 리스트에서 사용할 수 있도록 간단한 연산 적용
        temp[point] = count # 출력되는 순서를 저장하고
        count += 1 # 순서 증가
        priorities[point] = -1 # 이미 출력한 문서는 다시 수행하지 않기 위해 값 변경
    
    answer = temp[location]
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
