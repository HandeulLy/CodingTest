def solution(n):
    # 삼진법 문제라고 생각하고 접근
    # 대신 0이 아니라 4를 사용해야 하고, 숫자를 계속 3으로 나눠서 낮춰야 함

    answer = ''
    number = ['4', '1', '2']
    

    while n != 0 :
        index = n % 3
        answer = number[index] + answer
        n -= 1 # 3으로 나누어 떨어지는 경우 몫이 생기기 때문에 낮춰야 함
        n //= 3
        
    return answer