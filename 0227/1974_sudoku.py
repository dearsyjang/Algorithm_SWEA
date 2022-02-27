import sys
sys.stdin = open('1974_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    # 가로
    for i in range(9):
        row = [0] * 10
        for j in range(9):
            row[arr[i][j]] += 1
            if row[arr[i][j]] == 2:
                result = 0

    # 세로
    for j in range(9):
        col = [0] * 10
        for i in range(9):
            col[arr[i][j]] += 1
            if col[arr[i][j]] == 2:
                result = 0

    # 3 x 3
    for i in range(0,9,3):
        for j in range(0,9,3):
            square = [0] * 10
            for x in range(3):
                for y in range(3):
                    square[arr[i+x][i+y]] += 1
                    if square[arr[i+x][i+y]] == 2:
                        result = 0

    print(f'#{tc} {result}')

