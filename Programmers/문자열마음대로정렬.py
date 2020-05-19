def solution2(strings, n) :
    strings.sort()
    answer = sorted(strings, key = lambda x : x[n])
    print(answer)
    return answer
    
input_strings = ['sun', 'bed', 'car']
input_n = 1
solution2(input_strings, input_n)