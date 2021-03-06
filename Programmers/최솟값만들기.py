'''

길이가 같은 두 배열, A와 B. 각 배열은 자연수로 이루어졌다.
A와 B에서 각각 하나의 숫자를 뽑아 두 수를 곱하고, 곲한 값을 누적하여 더한다.
이 때, 최종 누적 값이 최소가 되도록 만드는 프로그램을 작성하라.​

제한사항 : A와 B의 크기는 1,000 이하 + 각 원소의 크기는 1,000 이하의 자연수

'''

'''

제일 작은 값과 제일 큰 값을 곱해야 최종 결과가 최소일 것이라 생각했다.
그래서, A와 B를 정렬하고, A에서 최소 x B에서 최대를 곱한다.

'''

def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    sum = 0
    
    for i in range(len(A)) :
        sum += A[i] * B[i]
    
    return sum