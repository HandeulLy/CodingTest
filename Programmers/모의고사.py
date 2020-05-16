def solution(answers):
    # 리스트 중 (정답) - (찍은번호) 가 0인 경우가 정답을 맞춘 것
    # 0의 경우가 가장 많은 사람을 출력
    
    answer = []
    score = [0] * 3
    patternA = [1,2,3,4,5]
    patternB = [2,1,2,3,2,4,2,5]
    patternC = [3,3,1,1,2,2,4,4,5,5]
    high = 0

    for i in range(len(answers)) :
        if answers[i] - patternA[i%5] == 0 : score[0] += 1
        if answers[i] - patternB[i%8] == 0 : score[1] += 1
        if answers[i] - patternC[i%10] == 0 : score[2] += 1
    
    high = max(score)
    for i in range(3) :
        if score[i] == high :
            answer.append(i+1)

    print(answer)
    return answer

input_answers = [1,2,3,4,5]
solution(input_answers)
input_answers = [1,3,2,4,2]
solution(input_answers)
input_answers = [4,4,4,5,1, 4,4,5,1,4, 4,5,1,2,3]
solution(input_answers)