import sys
sys.stdin = open('input_sudoku.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    def sudoku(arr):
        for i in range(9):
            row_lst = [0] * 10
            col_lst = [0] * 10
            for j in range(9):
                # 가로 검사
                row_lst[arr[i][j]] += 1
                if row_lst[arr[i][j]] == 2:
                    return 0

                # 세로 검사
                col_lst[arr[j][i]] += 1
                if col_lst[arr[j][i]] == 2:
                    return 0

            # 3*3 검사
            for x in range(0, 9, 3):
                for y in range(0, 9, 3):
                    square_lst = [0] * 10
                    for i in range(3):
                        for j in range(3):
                            square_lst[arr[x+i][y+j]] += 1
                            if square_lst[arr[x+1][y+j]] == 2:
                                return 0
        return 1

    result = sudoku(arr)
    print(f'#{tc} {result}')
