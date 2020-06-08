def solution(n):    
    # 시간복잡도가 n의 제곱인 아이디어
    # 1부터 (n+1)/2까지의 수를 원소로 가지는 리스트 생성
    # 이 리스트를 i, j인덱스를 사용해서 순회
    # i부터 j까지의 합과 n을 비교
        # i부터 j까지의 합이 n보다 작으면 j를 1증가해서 다시 비교
        # i부터 j까지의 합이 n과 같으면 count를 증가
        # i부터 j까지의 합이 n보다 크면 i를 1증가해서 다시 수행
    answer = 0
    numbers = [i for i in range(1, (n+1)//2+1)]
    
    for i in range(len(numbers)-1) :
        for j in range(i+1, len(numbers)) :
            if sum(numbers[i:j+1]) < n : pass
            elif sum(numbers[i:j+1]) == n : 
                answer += 1
            else : break
        
            
    
    return answer

input_n = 15
solution(input_n)