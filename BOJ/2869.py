# 달팽이는 올라가고 싶다

# 달팽이는 높이가 Vm(미터)인 나무 막대를 올라간다
# 낮에는 Am 올라가고 밤에 자는 동안 Bm 미끄러진다(단, 정상에 올라간 후에는 미끄러지지 않는다)
# 달팽이가 나무 막대를 모두 올라가는데 걸리는 일 수를 계산하는 프로그램 작성

# 입력 : 세 정수 A, B, V가 공백으로 구분( 1<= B <= A <= V <= 1,000,000,000)
# 출력 : 달팽이가 나무를 모두 올라가는데 며칠이 걸리는지 출력

# V // (A-B) + 1 ... ?

#############################################################

#############################################################

# VSCode 확인용 코드
# def solution(a, b, v) :
#     result = 1
#     h = a
#     while True : 
#         print('{} - {}'.format(result, h))
#         result, h = result+1, h+a-b
#         if h >= v : 
#             break
#     print(result)

# A, B, V = map(int, input().split())
# solution(A, B, V)


#############################################################

#############################################################

# 내가 제출한 코드 -- 시간초과 오답
# A, B, V = map(int, input().split())
# result, height = 1, A
# while True : 
#     result, height = result+1, height+A-B
#     if height >= V : 
#         break
# print(result)

# while 반복문을 사용하면 시간초과로 안되기 때문에 
# 수식적 계산을 해야 함... 단순히 반복하는 솔루션이 아닐 것


#############################################################

#############################################################

# # 내가 제출한 코드2 -- 오답
# A, B, V = map(int, input().split())
# print( ((V - A) // (A - B)) + 1)


#############################################################

#############################################################

#249 125 500 - 4
# 2 1 5 - 4
# 3 1 8 - 4

# 위 경우의 차이점을 생각해보자...
# A - B의 값이 1인지 아닌지? 
    
# 내가 제출한 코드3 -- 
# A, B, V = map(int, input().split())
# print(int((V-A)/(A-B)+2)) if A-B!=1 else print(int((V-A)/(A-B)+1))


#############################################################

#############################################################

# 내가 제출한 코드2_2

A, B, V = map(int, input().split())
print("{}".format((V-B)//(A-B)+2 if (V-A)%(A-B)!=0 else (V-B)//(A-B)+1))


#############################################################

#############################################################

#249 125 500 - 4
    # 249 - 124 | 373 - 248 | 497 - 372 | 621
# 2 1 5 - 4
    # 2 - 1 | 3 - 2 | 4 - 3 | 5
# 3 1 8 - 4
    # 3 - 2 | 5 - 4 | 7 - 6 | 9
# 6 4 6 - 30
    # 6
# 100 90 101 - 2
    # 100 - 10 | 110

# def sol(A, B, V) :
#     print((V-B)//(A-B)+1) if A-B!=1 and A!=V else print((V-B)//(A-B))

# sol(2, 1, 5) # 4
# sol(3, 1, 8) # 4
# sol(6, 4, 6) # 1
# sol(100, 90, 101) # 2
# sol(249, 125, 500) # 4
# sol(6, 3, 12)