def solution(prices):
    # 이중 for문을 이용해서 비교하면 되지 않을까?
    # O(n^2)이기는 하지만 가능하다고 확신되는 옵션이다
    
    size = len(prices) # 입력 받은 리스트의 길이 저장
    answer = [0] * size # 반환 할 리스트 선언

    for i in range(size) :
        for j in range(i+1, size) :
            answer[i] += 1 # 1초 동안은 변화가 없으니까 1 증가
            if prices[i] > prices[j] : # 가격이 떨어지면 증가 연산 중단
                break
            
        print(answer)
    return answer

    
input_prices = [1, 2, 3, 2, 3]
solution(input_prices)
