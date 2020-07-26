'''

    주어진 수가 1이 될 때까지 아래의 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측

    1-1. 입력된 수가 짝수라면 2로 나눈다.
    1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다.
    2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.

    예를 들어, 6을 입력 받은 경우,
    [6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1]
    총 8번의 작업 후 1이 된다.

    1이상 8,000,000미만인 정수 num이 입력될 때, 몇 번의 작업을 수행하는지 반환하는 함수 solution을 완성한다.
    단, 작업을 500번 수행해도 1이 되지 않는다면 -1을 반환한다.

'''

def solution(num):
    answer = 0
    while num != 1 and answer <= 500 : 
        if num % 2 == 0 : num /= 2
        else : num = num*3 + 1
        answer += 1
    #answer = answer if answer<=500 else -1
    print(answer)
    return answer

solution(1)
solution(6)
solution(16)
solution(626331)