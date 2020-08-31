def solution(numbers, hand):
    answer = []
    pad = [1,2,3,4,5,6,7,8,9,'*',0,'#']
    p_r, p_l = [3,0], [3,2]

    for n in numbers :
        if n in [1, 4, 7] :
            i_n = pad.index(n)
            answer.append("L")
            p_l = [i_n//3, i_n%3]
        elif n in [3, 6, 9] :
            i_n = pad.index(n)
            answer.append("R")
            p_r = [i_n//3, i_n%3]
        else :
            i_n = pad.index(n)
            p_n = [i_n//3, i_n%3]
            d_r, d_l = abs(p_n[0]-p_r[0]) + abs(p_n[1]-p_r[1]), abs(p_n[0]-p_l[0]) + abs(p_n[1]-p_l[1])
            if d_r == d_l : 
                if hand == "right" :
                    answer.append("R")
                    p_r = p_n
                else : 
                    answer.append("L")
                    p_l = p_n
            elif d_r < d_l : 
                answer.append("R")
                p_r = p_n
            else : 
                answer.append("L")
                p_l = p_n
            
    return ''.join(answer)

i_n = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
i_h = "right"
#print(solution(i_n, i_h)) # "LRLLLRLLRRL"

i_n = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
i_h = "left"
#print(solution(i_n, i_h)) # "LRLLRRLLLRR"

i_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
i_h = "right"
#print(solution(i_n, i_h)) # "LLRLLRLLRL"