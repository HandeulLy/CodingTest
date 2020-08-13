'''

문제 : 두 수를 입력 받아 두 수의 최대공약수와 최소공배수를 반환하는 함수 작성
입력 : 두 수는 1이상 1,000,000이하의 자연수
출력 : 배열 맨 앞에 최대공약수, 두번째에 최소공배수 반환

'''

'''

소인수분해를 해야하지 않을까?
공통으로 갖는 부분이 최소공배수로 될 것이고
나머지를 다 곱하면 최대공약수가 될 것이다

'''

def solution(n, m):
    c, tmp = [1, 1], 2

    while tmp<=n and tmp<=m :
        
        if n%tmp==0 and m%tmp==0 :
            n //= tmp
            m //= tmp
            c[0] *= tmp
            c.append(tmp)
        else : tmp += 1
        print("tmp={}  n={}  m={}  c={}".format(tmp, n, m, c))

    return [c[0], c[0]*n*m]

i_n, i_m = 3, 12
#print(solution(i_n, i_m)) # [3, 12]

i_n, i_m = 2, 5
#print(solution(i_n, i_m)) # [1, 10]

i_n, i_m = 60, 48
print(solution(i_n, i_m)) # [12, 240]

i_n, i_m = 72, 126
print(solution(i_n, i_m)) # [1, 10]