'''

[소트 인사이드]
- 링크 : https://www.acmicpc.net/problem/1427


문제 : 수가 주어질 때, 그 수의 각 자리수를 내림차순으로 정렬하라
입력 : 정렬하고자 하는 수 N(1,000,000,000 이하의 자연수)
출력 : 자리수를 내림차손으로 정렬한 값 반환

'''

'''

수를 문자열처럼 생각하고 원소 하나하나 정렬하는 방법이 있을 것이다.
하지만, 이는 아마도 극한의 상황(10억)이 들어올 때 조건에 걸릴 듯 한 느낌이다.
따라서 나는 count를 해보려고 한다

'''

# so1
# n, cnt, ans = input(), [0]*10, ""
# for i in n :
#     cnt[int(i)] += 1
# for i in range(9,-1,-1) :
#     ans = ans + str(i)*cnt[i]
# print(ans)


'''
문자열로 생각해서 sort하는 방법 코드
'''

# sol2 (try)
print("".join(sorted(list(input()), reverse=True)))
