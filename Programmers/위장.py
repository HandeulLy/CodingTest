'''
2차원 배열이 주어질 때, 서로 다른 옷의 조합 수를 반환하는 코드 작성

제한 조건
    - 각 행은 [이름, 종류]로 구성
    - 의상 수(배열의 길이)는 1개 이상 30개 이하
    - 같은 이름을 가진 의상은 없고
    - 리스트의 모든 원소는 문자열
    - 각 문자열의 길이는 1이상 20이하, 알파벳소문자 또는 _로만 구성
    - 하루에 최소 한 개는 입어야함(원소 한 개 선택)
'''

'''
'종류'를 key 값으로 딕셔너리 생성
그러면 종류마다 개수가 정해지기 때문에, 각 key의 items 수를 곱한다
단, 중복 제거 처리를 위해 딕셔너리 길이에서 -1을 해준다
'''

def solution(clothes):
    answer = 1
    dic = {}
    for c in clothes :
        if c[1] not in dic.keys() : dic[c[1]] = 1
        else : dic[c[1]] += 1
    
    for d in dic : 
        answer *= dic[d]        

    return len(clothes) + answer * (len(dic) - 1)

i_c = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(i_c)) # 5

i_c = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(i_c)) # 3