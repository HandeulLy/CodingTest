def combination(n, p) :
    # 이 아이디어는 아래 링크를 참고했습니다
    # https://smlee729.github.io/python/algorithm/2015/03/08/1-nchoosek.html
    a, b = 1, 1
    k = min(n-p, p) # 조합의 대칭성을 활용하여 효율적인 연산만 하기 위해서
    
    for i in range(1, k+1) :
        a *= n + 1 - i
        b *= i
    return a / b 

def solution(n):
    # 1과 2만을 더하는 연산을 n과 같아질 때까지 진행 - 반복문 조건
    # 2를 사용하는 횟수를 0번에서 x번까지 늘려가야 함
    # 2만 사용 횟수에 따라서 가능한 방법은 Combination으로 계산
    # 2만을 사용했는데 n보다 커지면 n을 한번 줄이고 1을 더함(n이 홀수인 경우)

    answer = 0
    n_count = 0 # 2칸 이동 하는 횟수를 저장하는 변수 선언
    while n_count * 2 <= n : # 2칸씩 이동해서 n을 넘어가면 작업 중지
        #one = n - (n_count*2)
        answer += combination(n-n_count, n_count)
        #answer += facorial(n - n_count) / (facorial(n_count) * facorial(one))
        # 컴비네이션 계산 : one C n_count 형식의 계산
        print("{} : {}".format(n_count, answer))
        

        if n - n_count < n_count :
            break
        n_count += 1
    
    answer = (answer) % 1234567
    # 2를 한번도 안쓴 경우는 항상 1가지 경우가 있기 때문에 1을 더하고
    # 문제의 조건에 따라 1234567를 나눈 나머지를 반환
    print(answer)
    return int(answer)

input_n = 100
for i in range(1, input_n) :
    print(" ========== {}".format(i))
    solution(i)

#print(combination(5,2))