'''

    게임 운영자 오렐리,
    신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 문제점 발견했다.
    이를 해결하기 위해 동적으로 게임 시간을 늘려 난이도 조절하려고 한다.

    실패율 = (스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수) / (스테이지에 도달한 플레이어 수)

    매개변수는 아래 2개
    1) 전체 스테이지의 개수 N
    2) 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages

    이 2개의 매개변수가 주어질 때, 
    실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열을 return 하도록 solution 함수를 작성한다.

    제한 조건
    - 스테이지 개수 N은 1이상 500이하의 자연수
    - stages의 길이는 1이상 200,000이하
    - stages에는 1이상 N+1 이하의 자연수가 담겨 있다.
        각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
        단, N+1은 마지막 스테이지(N번째 스테이지)까지 클리어 한 사용자를 나타낸다.
    - 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 한다.
    - 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의한다.

'''

#########################################

'''
def solution(N, stages):
    print(stages)
    # 입력 값 확인

    c = [stages.count(i) for i in range(1, N+1)]
    c += [len(stages) - sum(c)]
    print(c)
    # 각 스테이지 별 플레이어 수 확인 

    r = [c[i-1]/sum(c[i-1:]) for i in stages]
    print(r)
    # 각 스테이지 별 실패율 확인

    r = [r[stages.index(i)] if i in stages else 0 for i in range(1, N+1)]
    print(r)
    # 각 스테이지 별 실패율 확인 정리

    answer = []
    for i in range(N) :
        m = max(r) 
        answer.append(r.index(m)+1)
        r[r.index(m)] = -1
    print(answer)
    # 실패율 기준으로 정렬

    return answer
'''

#########################################

def solution(N, stages):
    c, p, r = 0, len(stages), {}
    for i in range(1, N+1) : 
        c = stages.count(i)
        r[i] = c/p if i in stages else 0
        p -= c
        print(c, p, r)

    r = sorted(r, key=lambda x:r[x], reverse=True)
    print(r)

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
solution(4,	[4, 4, 4, 4, 4])