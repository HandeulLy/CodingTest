import math

def solution(progresses, speeds):
    answer = []
    size = len(progresses) # 입력 리스트 크기
    point = 0 # 리스트 요소를 가리키는 인덱스 역할
    count = 0

    for i in range(size) :
        progresses[i] = math.ceil((100 - progresses[i]) // speeds[i])
        # 완료까지 필요한 기간을 구해서 올림으로 저장

    while point+count < size :
        if progresses[point] >= progresses[point+count] :
            # 앞에 있는 기능을 구현하는데 필요한 기간이 뒤에 보다 크다는 것
            # 더 오래 걸리기 때문에 구현 완성됐을 때 함께 배포 가능하다는 것
            count += 1 # 함께 배포되는 기능의 수 증가
        else : # 뒤에 기능이 더 오래걸린다면
            answer.append(count) # 이미 완성해서 배포 가능한 기능의 수를 리스트에 추가
            point += count # 더 오래 걸리는 기능으로 인덱스 수정
            count = 0 # 같이 배포하는 기능의 수는 0으로 리셋
            
    answer.append(count) # while 문 마지막에 count를 추가하지 못해서 한번 더 수행
    print(answer)
    return answer

input_progresses = [5, 5, 5]
input_speeds = [21, 25, 20]
solution(input_progresses, input_speeds)
