def solution(n,a,b):
    count = 1
    while True :
        if (a+1)//2 == (b+1)//2 and (a-b)**2 == 1 : return count
        else :
            a, b = (a+1)//2, (b+1)//2
            count += 1


input_n = 16
input_a = 14
input_b = 15
print(solution(input_n, input_a, input_b))