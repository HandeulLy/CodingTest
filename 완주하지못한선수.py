def solution(participant, completion):
    # 완주한 선수들의 목록에서 이름 하나씩 가져와서
    # 참가자 목록 리스트에서 삭제하고
    # 하나 남은 이름을 출력하는 것으로 접근

    # 비교 또는 탐색을 하기 전에 주어진 리스트를 미리 정렬하면 되지 않을까?
    # 정렬된 리스트들을 순회하면서 다른 값을 발견하면 그때의 이름이 미완주 선수, 그 순간 작업 중지
    # 만약, 끝까지 간다면 마지막에 있는 이름이 미완주 선수

    participant.sort()
    completion.sort()
    
    answer = participant[-1]
    for i in range(len(completion)) :
        if participant[i] != completion[i] :
            answer = participant[i]
            break
        
    print(answer)
    return answer

input_participant = ['marina', 'josipa', 'josipa','nikola', 'vinko', 'vinko', 'filipa']
input_completion = ['josipa', 'filipa', 'marina', 'vinko','nikola', 'vinko']
solution(input_participant, input_completion)