import sys
from time import time
sys.setrecursionlimit(10**6)

inputs= sys.argv[1:][1::2]
inputs= list(map(int, inputs))
a = inputs[0] - 1
b = inputs[1] - 1
m = inputs[2]
n = m

def init_board(board, m, n):
    for i in range(m): 
        row = [] 
        for j in range(n): 
            row.append(-1) 
        board.append(row) 

def is_able_to_move(board, tmp_x, tmp_y, m, n):
    return ((tmp_x>=0 and tmp_x< n and tmp_y>=0 and tmp_y<m and board[tmp_x][tmp_y]==-1))

def step(board, a, b, m, n, x, y):
    min_deg_index = -1
    min_deg = 9
    for i in range(8):
        tmp_x = a + x[i]
        tmp_y = b + y[i]
        tmp_degree = degree_of(board, tmp_x, tmp_y, m, n, x, y)
        if(is_able_to_move(board, tmp_x, tmp_y, m, n)):
            if(tmp_degree < min_deg):
                min_deg = tmp_degree
                min_deg_index = i
    if(min_deg_index != -1):
        return a + x[min_deg_index], b + y[min_deg_index], True
    return -1, -1, False

def knight_tour_warnsdorff_heuristics(board, a, b, m, n, x, y):
    init_board(board, m , n)
    board[a][b] = 1
    position = 2
    knight_tour_warnsdorff_heuristics_solution(board, a, b, m, n, x, y, position)
    print_board(board, m , n)

def knight_tour_warnsdorff_heuristics_solution(board, a, b, m, n, x, y, position):           
    if(position == m * n + 1):
        return True
    x_tmp, y_tmp, isFound = step(board, a, b, m, n, x, y)
    if(isFound):
        board[x_tmp][y_tmp] = position;
        knight_tour_warnsdorff_heuristics_solution(board, x_tmp, y_tmp, m, n, x, y, position + 1)
    else:
        board[x_tmp][y_tmp] = -1
   

def back_track_knight_tour(board, a, b, position, m, n, x, y):
    if(position == m * n + 1):
        return True
    for i in range(8):
            tmp_x = a + x[i]
            tmp_y = b + y[i]
            if(is_able_to_move(board, tmp_x, tmp_y, m, n)):
                board[tmp_x][tmp_y] = position
                if(back_track_knight_tour(board, tmp_x, tmp_y, position + 1, m, n, x, y)):
                    return True
                else:
                    board[tmp_x][tmp_y] = -1
    return False

def degree_of(board, tmp_x, tmp_y, m , n, x, y):
    count = 0
    for i in range(8):
        next_x = tmp_x + x[i]
        next_y = tmp_y + y[i]
        if(is_able_to_move(board, next_x, next_y, m, n)):
            count +=1
    return count        

def print_board(board, m , n):
    count = 0
    for i in range(0, m):
        for j in range(0, n):
            if(board[i][j] != -1):
                count +=1
            if(board[i][j] <= 9):
                print(board[i][j], end='    ')
            elif(board[i][j] >= 10 and board[i][j] <= 99):
                print(board[i][j], end='   ')
            elif(board[i][j] >= 100 and board[i][j] <= 999):
                    print(board[i][j], end='  ')
            else:
                print(board[i][j], end=' ') 

        print(end='\n')
    print('\n')    
    print('Number of steps: ', count)
    print('\n\n')

def back_track_solution(board, a, b, m, n, x, y):
    init_board(board, m , n)
    board[a][b] = 1
    position = 2
    if(back_track_knight_tour(board, a, b, position, m, n, x, y)):
        print_board(board, m , n)
    else:
        print("Not found solution")

def main():  
    x = [2, 1, -1, -2, -2, -1, 1, 2]; 
    y = [1, 2, 2, 1, -1, -2, -2, -1];
    board = [] 
    print('Knight Tour Warnsdorff Heuristics: \n')
    print("The solution: \n")
    start = time()
    knight_tour_warnsdorff_heuristics(board, a, b, m, n, x, y)
    end = time()
    print("Knight Tour Warnsdorff Heuristics have run %s (milliseconds)\n" % ((end-start)*1000))
    print('---------------------------------------------------/\---------------------------------------------------|')
    print('Knight Tour Backtracking: \n')
    print("The solution: \n")
    start = time()
    back_track_solution(board, a, b, m, n, x, y)
    end = time()
    print("Knight Tour Backtracking have run %s (milliseconds)" % ((end-start)*1000))

if __name__ == "__main__":
    main()
