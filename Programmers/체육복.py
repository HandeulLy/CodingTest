'''
# 출력 : 체육 수업을 들을 수 있는 학생의 최대 수
# 수업 들을 수 있는 조건 : 체육복을 가져야 함
# 체육복이 없다면, 바로 앞 또는 뒤 번호의 친구에게 빌릴 수 있음
# reserve를 활용해서 lost 원소 개수를 최대한 줄이는 것이 핵심

##############################
# 1st
# 1 : lost 원소보다 하나 작거나 큰 값(번호)이 reserve에 있는지 확인
# 2 : 있다면 그 원소들을 lost와 reserve에서 삭제(빌렸으니까 체육복이 있고, 빌려줬으니까 여분이 없어진 것)
# 3 : 이 과정을 lost의 원소 개수 만큼 반복
# 4 : lost 원소 개수를 n에서 뺀 값을 반환​

# 이 아이디어를 코드로 구현하려 했는데,
# 2번 단계에서 lost의 원소를 삭제하면 리스트 길이에 변화가 생기면서 list index out of range 에러가 발생했다
# 원소를 삭제하는 대신 원소의 값을 0으로 변경하고 lost에서 0이 아닌 원소의 개수를 n에서 뺐다

##############################
# 2nd
< 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다. >

​이 조건을 고려하지 않았기 때문에 테스트 케이스를 통과하지 못했다.
lost와 reserve에 중복된 값이 있다면 먼저 제거해줘야 한다
예를 들어, lost = [1, 2, 3, 5]이고 reserve = [1, 3, 4, 5]라고 했을 때 1, 3, 5번 학생들은 자신의 여분 체육복을 입으면 된다. 따라서 lost = [2] & reserve = [4]를 검사해야 하는 것이다.

##############################
# 3rd
temp를 사용하는 방법을 다르게 생각했다.
lost 리스트 복사해서 관리하는 방법으로 코드를 작성하면 lost, reserve에서 삭제하는 것도 간단해지고 마지막에 answer를 구할 때도 count(0)을 안해도 된다

이렇게 작성해도 테스트케이스 모두 통과한다.

개인적으로 이 코드가 깔끔해서 만족하지만, Step1과 Step2 과정 모두 조금 더 간결하게 할 수 있다.

​##############################
# 4th
Step1의 경우 lost와 reserve 리스트 원소를 상호 비교하면서 중복되지 않는 원소들만 다시 저장하면 된다.
Step2의 경우 lost 리스트의 인덱스를 사용하는 대신 reserve를 사용하면 된다
list index out of range 오류를 피하기 위해 temp나 lostCopy 처럼 임시 리스트를 사용했는데, reserver 인덱스를 활용해서 lost 원소만 삭제한다면 공간 효율성도 향상시킬 수 있다
이 아이디어를 코드로 작성하면 아래와 같다.

'''

def solution(n, lost, reserve):
    answer = 0

    reserveNew = [i for i in reserve if i not in lost]
    lostNew = [j for j in lost if j not in reserve]

    for i in reserveNew :
        if (i+1) in lostNew :
            lostNew.remove(i+1)
        elif (i-1) in lostNew :
            lostNew.remove(i-1)
        else :
            pass
        print("{}\t{}".format(lost, reserve))
    '''
    answer = n - len(lost)
    for i in lostCopy :
        if (i-1) in reserve :
            lost.remove(i)
            reserve.remove(i)
    print("{}\t{}\t{}".format(lost, lostCopy, reserve))
    
    lostCopy = lost[:]
    for i in lostCopy :
        if (i-1) in reserve :
            reserve.remove(i-1)
            lost.remove(i)
        elif (i+1) in reserve :
            reserve.remove(i+1)
            lost.remove(i)
        else :
            pass
        print("{}\t{}\t{}".format(lost, lostCopy, reserve))
    
    answer = n - len(lost)
    
    temp = []
    for i in range(len(lost)) :
        if lost[i] in reserve : # lost가 reserve에 있으면
            reserve.remove(lost[i]) # reserve에서 제거
        else :
            temp.append(lost[i]) # lost에서 제거하는 것과 동일한 연산
    
    for i in range(len(temp)) :
        if (temp[i] - 1) in reserve :
            reserve.remove(temp[i]-1) # 여분을 빌려줬으니 reserve에서 삭제
            temp[i] = 0 # 체육복을 빌렷으니까 lost에서 삭제
        elif (temp[i] + 1) in reserve :
            reserve.remove(temp[i]+1)
            temp[i] = 0
        else :
            pass
    
    answer = n - (len(temp) - temp.count(0)) # temp 리스트 중 0은 체육복을 빌린 학생들의 수
    '''    
    return answer

input_n = 7
input_lost = [1,2,3,5]
input_reserve = [1,3,4,5]
solution(input_n, input_lost, input_reserve)