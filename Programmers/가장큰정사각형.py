'''
# 문제
- 1과 0으로 채워진 board
- board의 1칸은 1x1 정사각형
- board 에서 1로 이루어진 가장 큰 정사각형의 넓이를 return
# 제한사항
- board는 2차원 배열
- board의 행과 열의 크기는 1000이하의 자연수
- board의 값은 1 또는 0으로만 채워짐
'''

'''
baord의 영역에서 (0,0)부터 마지막 칸까지 for 루프를 반복하면서 탐색한다.
이 때 현재 칸의 값이 0이면 다음 칸으로 이동, 1이면 사각형 넓이를 체크한다.
현재 칸을 사각형의 좌측 상단 꼭지점으로 잡고, 사각형의 가로세로 길이를 1씩 늘려가면서 해당 영역의 모든 칸의 값들이 1인지 확인한다.
모든 칸의 값들이 1이라면 answer의 기존 값과 비교해서 update 여부를 결정한다.
더이상 진행할 수 없는 조건일 때까지 위 과정들을 반복한다.
'''

##########################################

# def solution(board):
#     answer = 0
#     r, c = len(board), len(board[0])
    
#     for i in range(r) : 
#         for j in range(c) : 
#             if board[i][j] == 1 : 
#                 k = 0
#                 while (j+k <= r) and (i+k <= c): 
#                     # isBreak = False
#                     # for y in range(j, j+k) :
#                     #     for x in range(i, i+k) : 
#                     #         print((i, j), x, y)
#                     #         if board[y][x] == 0 : isBreak = True
#                     #     answer = max(answer, k**2)
#                     #     #print(i, j, board[i][j], answer)
#                     #     if isBreak : break
#                     # k+=1    
#                     b = [[board[x][y] for y in range(j, j+k)] for x in range(i, i+k)]
#                     print(i, j, board[i][j], b)
#                     answer = max(answer, k**2)
#                     k += 1
#     print( board, answer)
#     return answer

def solution(board):
    answer = board[0][0]
    r, c = len(board), len(board[0])
    
    for i in range(1, r) : 
        for j in range(1, c) : 
            if board[i][j] == 1 : 
                board[i][j] = min( board[i-1][j-1], board[i-1][j], board[i][j-1] ) + 1
            answer = max(answer, board[i][j])

    print(answer**2)
    return answer**2

##########################################

b1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
solution(b1) # answer = 9

b2 = [[1, 0], [1, 0], [1, 1], [1, 1]]
solution(b2) # answer = 4

b3 = [[0,0,1,1],[1,1,1,1]]
solution(b3) # answer = 4

b4 = [[1]]
solution(b4) # answer = 4

##########################################
##########################################
##########################################

'''
def solution(board):
    # 문제의 핵심은 효율성을 확보하는 것(시간복잡도 낮게!)이라고 생각
    
    answer = 0
    
    row = len(board[0]) # 행, 표의 가로 길이
    col = len(board) # 열, 표의 세로 길이

    longest_row = 0
    #longest_col = 0

    print("{} - {}".format(row, col))
    for i in range(col) :
        x1, x2 = 0, 0 # 사각형의 가로 길이를 저장할 변수 선언
        for j in range(row) :
            if board[i][j] == 1 : # 1인 경우 사각형의 오른쪽 x좌표 값을 지정 
                x2 = j
            else : # 0인 경우 사각형의 왼쪽 x좌표 값을 지정
               x1 = j+1
            longest_row = max(longest_row, x2-x1+1)
        print("{} - {} : {}~{} = {} // {}".format(i, j, x1, x2, x2-x1, longest_row))
        #longest_row = max(longest_row, x2-x1)
        #print("{} - {} : {}".format(i, j, longest_row))

    return answer

input_board = [[0,1,0,1],[1,1,1,1]]
solution(input_board)
'''