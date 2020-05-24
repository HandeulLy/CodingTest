# 마지막 4개를 제외하고는 모두 *로 변경해서 반환
 
def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]