def solution(n):
    answerList = []
    for i in range(1, n//2+1) : # n의 절반까지만 반복문 수행
        if n % i == 0 : # 약수이면
            if i not in answerList : answerList.append(i) # 리스트에 없으면 넣고
            else : return sum(answerList) # 리스트에 있으면 중단
            if n/i not in answerList : answerList.append(n//i) # 약수의 짝도 똑같이 수행
            else : return sum(answerList)   
    return sum(answerList)

for i in range(20) :
    print("{} : {}".format(i, solution(i)))