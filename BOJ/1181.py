'''
1181번, 단어 정렬
링크 : https://www.acmicpc.net/problem/1181


문제 : 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래 조건에 따라 정렬하는 프로그램 작성

조건 : 길이가 짧은 것 부터, 길이가 같으면 사전 순으로

입력
- 첫째 줄에 단어의 개수 N(1이상 20,000이하)
- 둘째 줄부터 한 줄에 하나씩 N개의 단어(각 문자열의 길이는 50을 넘지 않음)

출력
- 조건에 따라 정렬한 단어 출력
- 단, 같은 단어가 여러번 입력된 경우 한 번만 

'''

'''

단순히 사전 순으로 정렬하는 것이면 리스트에 저장하고 sort() 하면 될 것이다
하지만, 정렬 우선순위에서 단어의 길이가 높기 때문에 길이를 신경 써야한다.
이를 반영하기 위해 딕셔너리를 생각했다.

딕셔너리 하나를 생성하고, N개의 단어를 저장한다.
이 때, key는 단어의 길이이고, values는 단어이다.
이후 key 값을 기준으로 먼저 정렬한 후, value를 기준으로 정렬하면 될 것이다.

'''

import sys

words, word = dict(), ""

for _ in range(int(input())) :
    word = sys.stdin.readline()[:-1]
    if len(word) in words.keys() : 
        if word in words[len(word)] : pass
        else : words[len(word)].append(word)
    else : words[len(word)] = [word]

words = sorted(words.items(), key = lambda x : x[0])
print(words)
for wds in words : 
    #print(sorted(wds[1]))
    #wds[1] = sorted(wds[1])
    [print(w) for w in sorted(wds[1])]