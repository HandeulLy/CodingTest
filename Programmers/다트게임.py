'''

프로그래머스, 코딩테스트 연습, 2018 KAKAO BLIND RECRUITMENT, [1차] 다트 게임
https://programmers.co.kr/learn/courses/30/lessons/17682

다트 게임은 다트판에 다트를 세 차레 던져 그 점수의 합계로 실력을 겨루는 게임이다

다트 게임의 점수 계산 로직
    - 다트 게임은 총 3번의 기회로 구성
    - 각 기회마다 얻을 수 있는 점수는 0~10점
    - 점수와 함께 S(single), D(double), T(triple) 영역이 존재하고, 각 영역 당첨 시 점수에서 각각 1/2/3/제곱으로 계산, 점수마다 하나씩 존재
    - 옵션 *당첨 시 해당 점수와 바로 전에 얻은 점수를 2배
    - *가 첫 기회에서 나오면 첫 점수만 2배
    - 다른 * 효과와 중첩 가능(이 경우 중첩된 점수는 4배)
    - 옵션 #당첨 시 해당 점수는 마이너스
    - *의 효과는 #의 효과와 중첩 가능(이 경우 점수는 -2배)
    - *와 #은 점수마다 둘 중 하나만 존재, 존재하지 않는 경우도 존재

입력 : 0~10의 정수와 문자(S, D, T, *, #)로 구성된 문자열
입력 형식 : 점수|보너스|(옵션)의 문자열 3세트
출력 : 총 점수 반환

'''

##############################################

# def solution(dartResult):
#     operation = []
#     for d in dartResult :
#         l = len(operation)
#         if d.isdigit() : operation.append(int(d))
#         elif d.isalpha() :
#             if d == "S" : pass
#             elif d == "D" : operation[-1]**=2
#             else : operation[-1]**=3
#         elif d == "*" :
#             l = len(operation)
#             if l == 1 : operation[0] *= 2
#             else : operation[l-2], operation[l-1] = operation[l-2]*2, operation[l-1]*2
#         elif d == "#" : 
#             operation[-1]*=(-1)
#         else : pass
#         print(d, l, operation)
#     return sum(operation)

'''
    이렇게 하니까 10인 경우, 1과 0으로 받아들임
    2번 테스트 케이스를 통과하지 못함 - 사진 참고
'''

##############################################

'''
    10이 들어노는 경우에 대한 처리가 필요
    1) 1이 들어온 경우 다음 문자가 0인지 확인?
        - 어차피 다음 for 루프 때 0을 검사해서 0을 추가하게 됨
        - 이를 처리하려면 또 조건이 추가 됨
    2) 0이 들어온 경우 이전 문자가 1인지 확인?
        - 그럼 그냥 0일 때 이전 문자가 1인지 검사해보자
        - 이전 문자에 접근하려면? 인덱스가 필요
        - enumerate 활용해서 i로 인덱스 번호 받고
        - 이전 문자가 숫자 1이면, operation 마지막 숫자를 1에서 10으로 변경
        - 숫자 숫자인데, 1이 아닌 경우? 존재하지 않음
        - 문자인 경우, 그냥 pass

'''

def solution(dartResult):
    operation = []
    for i, d in enumerate(dartResult) :
        l = len(operation)
        if d.isdigit() :
            if d=="0" and dartResult[i-1]=="1" : operation[-1]=10
            else : operation.append(int(d))
        elif d.isalpha() :
            if d == "S" : pass
            elif d == "D" : operation[-1]**=2
            else : operation[-1]**=3
        elif d == "*" :
            l = len(operation)
            if l == 1 : operation[0] *= 2
            else : operation[l-2], operation[l-1] = operation[l-2]*2, operation[l-1]*2
        elif d == "#" : 
            operation[-1]*=(-1)
        else : pass
        print(d, l, operation)
    return sum(operation)


i_dR = '1S2D*3T'
print(solution(i_dR)) # 37

i_dR = '1D2S#10S'
print(solution(i_dR)) # 9

i_dR = '1D2S0T'
print(solution(i_dR)) # 3

i_dR = '1S*2T*3S'
print(solution(i_dR)) # 23

i_dR = '1D#2S*3S'
print(solution(i_dR)) # 5

i_dR = '1T2D3D#'
print(solution(i_dR)) # -4

i_dR = '1D2S3T*'
print(solution(i_dR)) #59