'''

2231번, 분해합
- 링크 : https://www.acmicpc.net/problem/2231

문제
- 어떤 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
- 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라고 한다.
ex) 245의 분해합은 245+2+4+5=256이기 때문에 245는 256의 생성자가 된다.
- 어떤 자연수의 경우에는 생성자가 없을 수도 있고, 생성자가 여러 개인 자연수도 있을 수 있다.
- 자연수 N이 주어질 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하라.

입력
- 1이상 1,000,000이하의 자연수

출력
- 조건에 맞는 답을 출력하되, 생성자가 없는 경우에는 0을 출력한다.

풀이
- 처음에는 방정식의 개념을 사용해서 접근해볼까 했다.
  하지만, 이는 2차 3차 이상으로 올라갈 수록 풀어낼 수 없다는 것을 발견했다.
  x y z...

- 단순히 반복문을 수행하면서 찾아내야 한다고 생각했다.
  일단, N은 (M 숫자 그대로) + (M을 이루는 각 자리 수)의 값이다.
- 그리고 M은 N의 절반보다 작은 숫자를 가질 수 없다.
- 따라서, N을 입력 받으면 N의 절반인 숫자부터 계산을 하면서 N을 만들 수 있는 최소의 수를 출력하기로 했다.

'''

def sol(n) : 
    for m in range(int(n/2), n) :
        if m + sum(map(int, str(m))) == N : return m
    return 0
N = int(input())
print(sol(N))