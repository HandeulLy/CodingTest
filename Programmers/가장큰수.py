def solution(numbers):
    answer = ''

    numbers = sorted(numbers, reverse=True, key=lambda x : (str(x)*4)[:4])
    
    for i in numbers :
        answer += str(i)
    if answer[0] == '0':    #모두 0인 경우 -> 테스트11
        return '0'    
    print(answer)
    
    ''' =================== ver2
    size = len(numbers)
    temp, point = {}, [0]*size

    #print("\n - - - - -  - - - - ")
    # STEP 1 #
    for i in range(size) :
        point[i] = len(str(numbers[i])) # 원래 자리수를 저장하기 위한 리스트
        temp[i] = (str(numbers[i])*4)[:4] # 4번 반복하고 앞에 4개만 저장
    #print(temp)
    # STEP 2 #
    temp = sorted(temp.items(), key=lambda x:x[1], reverse=True) # 정렬(역순으로)
    #print(temp)
    # STEP 3 #
    for i in range(size) :
        answer += temp[i][1][:point[temp[i][0]]]
    if answer[0] == '0':    #모두 0인 경우 -> 테스트11
        return '0' 
    '''
    
    return answer

aaa = [[40,403], [40,405], [40,404], [12,121], [2,22,223], [21,212], [212,21], [41,415], [2,22],
        [70,0,0,0], [0,0,0,0], [12,1213], [0,0,0,100], [0,0,100,0], [0,100,0,0], [100,0,0,0], [998, 9, 999]]
for i in aaa :
    print("{} => ".format(i), end='')
    solution(i)