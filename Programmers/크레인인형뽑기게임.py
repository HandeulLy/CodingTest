'''

# 문제
# 제한사항
- 블로그 링크 참고 : https://blog.naver.com/handuelly/222161282388

'''

'''

먼저, 크레인이 moves 리스트에 따라 뽑기를 진행하는 것에서 신경써야 할 것
1) 크레인은 해당 위치에서 가장 위에 있는 인형을 뽑는다.
2) 그 위치에 인형이 있으면 뽑아서 바구니에 넣고, 없다면 아무런 일도 일어나지 않는다.

그 다음, 바구니에 인형을 넣었을 때 신경써야 할 것
1) 방금 뽑은 인형과 바구니 마지막 원소 인형과 같은지 비교.
- 같다면 터뜨리면서 answer에 +2
- 다르다면 바구니 리스트에 방금 뽑은 인형 추가

'''

#############################################

def solution(board, moves):
    answer = 0
    tmp, box, l_b = [], [], len(board)

    for m in moves : 
        tmp = [b[m-1] for b in board]
        num = tmp[-(l_b-tmp.count(0))]
        board[tmp.count(0)%l_b][m-1] = 0

        if num == 0 :
            pass
        else : 
            if len(box) == 0 : 
                box.append(num)
            else : 
                if box[-1] == num : 
                    box.pop()
                    answer += 2
                else : 
                    box.append(num)

    return answer

#############################################

# board를 한번 T 변환 해서 각각 리스트로 사용하면 더 빠르지 않을까?

def solution2(board, moves):
    answer = 0
    box = []
    l_b = len(board)
    new_board = [[board[j][i] for j in range(l_b)] for i in range(l_b)]

    for m in moves : 
        idx = (new_board[m-1].count(0))%l_b
        num = new_board[m-1][idx]
        new_board[m-1][idx] = 0

        if num == 0 :
            pass
        else : 
            if len(box) == 0 : 
                box.append(num)
            else : 
                if box[-1] == num : 
                    box.pop()
                    answer += 2
                else : 
                    box.append(num)
    
    return answer

#############################################

b = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
m = [1,5,3,5,1,2,1,4]
#solution(b, m) # 4
solution2(b, m) # 4
