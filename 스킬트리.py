def solution(skill, skill_trees):
    # skill_trees의 각 아이템을 순회하면서 skill 순서에 어긋나는지 확인

    # skill_trees의 i번째 아이템 j번째 스킬이 skill에 있는지 확인 - in 사용
    # 있으면 선행 스킬이 있는지 봐야하고, 없으면 j+1번째로 넘어가서 확인

    point = 0 # j번째 스킬의 위치를 skill 리스트 속 인덱스 값으로 저장
    answer = 0 # 가능한 스킬트리의 개수를 저장
    
    for skills in skill_trees :
        temp = [False] * len(skill) # 스킬을 순차적으로 배웠는지 확인할 수 있는 임시 리스트 선언

        for j in range(len(skills)) :
            if skills[j] in skill : # j번째 스킬이 skill 리스트 안에 있다면
                point = skill.index(skills[j]) # 그 인덱스를 point에 저장해서
                temp[point] = True # temp 리스트의 값을 True로 변경
                if False in temp[:point+1] : # 선행 스킬을 배우지 않았다면
                    break # 불가능한 스킬 트리이기 때문에 수행 중단
            if j == len(skills) - 1 : # i번째 아이템 스킬을 모두 확인할 때까지 break 안했으면
                answer += 1 # 가능한 스킬트리기 때문에 answer의 수를 증가

    print(answer)
    return answer

input_skill = "CBD"
input_skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(input_skill, input_skill_trees)