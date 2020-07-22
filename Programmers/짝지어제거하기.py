# def solution(s):
#     k = 0
#     while 1 :
#         if s[k] == s[k+1] : 
#             s = s[:k] + s[k+2:]
#             k = max(0, k-1)
#         else : k += 1
#         print(k, s)

#         if len(s) == 0 or k+1 >= len(s) : break

#     return 0 if len(s) else 1

# #s = 'baabaa'
# s = 'cdcd'
# print(solution(list(s)))
    
'''
인덱스를 잘 조절해야 함

k번 인덱스와 k+1번의 문자를 비교
    동일하면 문자열을 리셋해야 함, s = s[:k] + s[k+2:]
    + k의 값을 새로 지정해야 하는데 한칸 뒤로 가야하기 때문에 k-1
    다르면 k를 1증가시켜서 다시 문자 비교

이 과정을 반복문으로 넣고, 끝까지 진행
종료 조건은 ... k가 s의 길이만큼 되거나 0인 경우

길이가 0이면 모든 문자가 삭제된 것이기 때문에 1을 반환 아니면 0을 반환

'''

###################################################

# def solution(s):
#     s, k, l, c = list(s), 0, 1, 0
#     while l < len(s) :        
#         if s[k] == s[l] :
#             # s = s[:k] + s[k+2:]
#             # k, l, c = max(0, k-1), l+1, c+2
#             if k == 0 : k, l, c = l+1, l+2, c+2
#             else : k, l, c = max(0, k-1), l+1, c+2
#         else : k, l = k+1, l+1
        

#         #if len(s) == 0 or k+1 >= len(s) : break

#     return 1 if c==len(s) else 0

# s = 'baabaa'
# #s = 'cdcd'
# #s = 'a'

# print(solution(list(s)))

###################################################

def solution(s):
    a = list()

    for i in s :
        if len(a) > 0 and a[-1] == i : a.pop()
        else : a.append(i)
    print(a)
    return 0 if len(a) else 1

s = 'baabaa'
s = 'cdcd'
s = 'a'

print(solution(list(s)))