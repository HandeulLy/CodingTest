def solution(n, words):
    for i in range(len(words)) :
        #if len(words[i]) == 1 : return [(i+1)%n+1, (i+1)//n, 2, i]
        for j in range(i) :
            #print("{} : {}".format(i, j))
            if words[i] == words[j] : return [(i)%n+1, (i)//n+1, 1, i]
        if len(words[i]) == 1 : return [(i+1)%n+1, (i+1)//n, 2, i]
        if i>0 and words[i][-1] != words[i+1][0] : return [(i+1)%n+1, (i+2)//n + 1, 3, i]
    
    return [0, 0, i , j]

def solution2(n, words):
    for i in range(len(words)-1) :
        if len(words[i]) == 1 : return [(i+1)%n+1, (i+1)//n]
        if words[i][-1] != words[i+1][0] : return [(i+1)%n+1, (i+2)//n + 1]
        for j in range(i) :
            if words[i+1] == words[j] : return [(i+1)%n+1, (i+1)//n+1]
    return [0, 0]

def solution3(n, words):
    for i in range(len(words)) :
        if words[i] in words[:i] : return [(i)%n+1, (i)//n+1] # 조건 1
        if len(words[i]) == 1 : return [(i+1)%n+1, (i+1)//n] # 조건 2
        if i>0 and words[i][0] != words[i-1][-1] : return [(i)%n+1, (i)//n + 1] # 조건 3
    return [0, 0]

input_n = 2
input_words = ["land", "dream", "mom", "mom", "ror"]
print(solution(input_n, input_words))