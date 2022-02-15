import sys
sys.stdin = open("input.txt")

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    # 1. 행의 합
    for i in range(100):
        row_sum = 0
        for j in range(100):
            # 합계
            row_sum += arr[i][j]
            # 최대값
        if max_sum < row_sum:
            max_sum = row_sum

    # 2. 열의 합
    for i in range(100):
        column_sum = 0
        for j in range(100):
            # 합계
            column_sum += arr[j][i]
            # 최대값
        if max_sum < column_sum:
            max_sum = column_sum

    # 3-1. 대각선의 합 (/)
    diagonal_sum1 = 0
    for i in range(100):
        diagonal_sum1 += arr[i][i]
            # 최대값
    if max_sum < diagonal_sum1:
        max_sum = diagonal_sum1

    # 3-2. 대각선의 합 (\)
    diagonal_sum2 = 0
    for i in range(100):
        diagonal_sum2 += arr[i][99-i]
    if max_sum < diagonal_sum2:
        max_sum = diagonal_sum2

print(f'#{tc} {max_sum}')

