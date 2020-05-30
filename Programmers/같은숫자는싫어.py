def solution(arr):
    answer = []
    i, j = 0, 1
    
    while True : 
        if arr[i] == arr[j] : # i번째와 j번째 원소가 같으면
            j += 1 # 다음 원소를 비교
        else : # 다르면
            answer.append(arr[i]) # i번쨰 원소를 추가하고
            i, j = j, j+1 # i는 j번째 원소를 가리키고, j는 다음 원소를
        
        if j >= len(arr) : # arr 리스트의 마지막까지 순회 했으면
            answer.append(arr[i]) # 값을 추가하고 반환 
            return answer