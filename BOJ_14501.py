N = int(input())
tasks = [ list(map(int, input().split())) for i in range(N)]
maxPay = 0

def solve(day, pay) :
    global maxPay
    if day == N : # 마지막날 신청된 상담
        if pay > maxPay : maxPay = pay
        return
    elif day > N : # 퇴사 후 상담은 못하니까 연산 종료
        return

    solve(day + tasks[day][0], pay + tasks[day][1]) # 해당 일의 상담을 시작하면 다음 상담은 지금 상담 끝난 후
    solve(day + 1, pay) # 해당 일 상담 안하고 다음 날 상담

solve(0, 0)
print(maxPay)