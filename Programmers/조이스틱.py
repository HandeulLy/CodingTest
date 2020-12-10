
'''
# 문제
    - 맨 처음에는 A로만 이루어진 이름을 조이스틱으로 완성
    - 조이스틱 조작 방법
        1) ▲ - 다음 알파벳
        2) ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
        3) ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
        4) ▶ - 커서를 오른쪽으로 이동
    - 만들고자 하는 name이 매개변수로 주어질 때, 조이스틱 조작 횟수의 최소값을 return

# 제한조건
    - name은 알파벳 대문자로만 이루어짐
    - name의 길이는 1이상 20이하
'''

'''
먼저, 이름의 각 문자가 갖는 아스키코드를 'A'랑 비교해야 한다
이 때 두 번을 비교해야 하는데, (문자)-(A)와 (A)-(문자) 이다.
왜냐하면 (문자) - (A)은 ▲ 조작을 통해 A에서부터 B-C-D-... 순서대로 다음 알파벳을 찾는 것
(A)-(문자)는 ▼ 조작을 통해 (문자)에서 시작해서 이전 알파벳을 탐색하며 A까지 오는 것
여기서 필요한 것은 ord()와 chr().


다음으로, 여기에 이름의 다음 칸으로 이동하는 조작 횟수도 더해야 한다.
주어진 문자가 'A'이면 건들지 않아도 되기 때문에 'A'의 유무와 그 위치를 고려해야 한다.

고려할 위치는 두번쨰와 마지막으로 생각했다.
첫 문자를 완성한 뒤 다음 문자를 두번쨰로 가는지(▶ 조작) 마지막으로 가는지(◀ 조작) 선택하기 때문이다.
한쪽만 A가 있다면 그 반대로 선택해야 최소의 조작 횟수를 가질 수 있다.
JABCD를 생각하면 두번째에 A가 있기 때문에 J-D-C-B 순서로 조작하면 된다.
JBCDA를 생각하면 마지막에 A가 있기 때문에 J-B-C-D 순서로 조작하면 된다.

여기서 또 확인해야 할 것은 두번째와 마지막에 A가 모두 있는 경우.
그리고 두번째로부터 또는 마지막으로부터 연속된 A가 몇 개인지 체크한다.
예를 들어서, JAAABCDA와 JABCDAAA를 보면 둘다 두번째와 마지막에 A가 있다.
조금 더 자세히 살펴보면 JAAABCDA는 두번째부터 3개의 A가 있고, 마지막에는 1개가 있기 때문에 마지막부터 역으로 조작해야 한다.
JABCDAAA는 두번째의 A가 더 적기 때문에 J에서 오른쪽 방향으로 조작해야 최소 조작 횟수를 가질 수 있다.

두번째와 마지막에 연결되어 있지 않고 중간에 있는 A는 최소 횟수에 영향을 주지 않는다고 생각했다.
'''

##########################################

# def solution(name):
#     answer = 0
#     for n in name : 
#         answer += min(ord(n)-65, 90-ord(n)+1)
#         #print(n, min(ord(n)-65, 90-ord(n)+1), ord(n)-65, 90-ord(n)+1, answer)

#     a_second, a_last = 0, 0
#     i, j = 1, len(name)-1
#     while i < j : 
#         if name[i] == 'A' : a_second += 1
#         else : break
#         i+=1
#     while j > 1 : 
#         if name[j] == 'A' : a_last += 1
#         else : break
#         j-=1
#     print(answer + (len(name) - max(a_second, a_last) -1))        
#     return answer + (len(name) - max(a_second, a_last) -1)

##########################################

def solution(name):
    answer, move = 0, 0
    i, l_n = 0, len(name)

    while name.count('A') != l_n : 
        answer += min(ord(name[i])-65, 90-ord(name[i])+1)
        name = name[:i] + 'A' + name[i+1:]

        l, r = i, i
        for m in range(1, l_n) : 
            r = (r+1)%l_n
            l = (l-1)%l_n

            if name[r] != 'A' :
                i = r
                move += m
                break
            if name[l] != 'A' :
                i = l
                move += m
                break
        
        print(name, i, answer, move, l, r)

        # if l<=r : 
        #     i = i+l
        #     answer += 1
        # else : 
        #     i = l_n-(i+r)
        #     answer += 1
        # i = i+l if l<=r else l_n-(i+r)
        #i = l_n-(i+r) if r >= l else i+l

        #move += 1
    print("end")

    print(answer, move)

    return answer

##########################################

n1 = "JEROEN"
solution(n1) # answer : 56

n2 = "JAN"
solution(n2) # answer : 23

n3 = "ABAAAAABAB"
solution(n3) # answer : 8

n4 = "ABABAAAAAB"
solution(n4) # answer : 8

##########################################