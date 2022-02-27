import sys
sys.stdin = open('1209_input.txt','r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    total = []

    # 가로
    for i in range(100):
        row = 0
        for j in range(100):
            row += arr[i][j]
        total.append(row)

    # 세로
    for i in range(100):
        col = 0
        for j in range(100):
            col += arr[j][i]
        total.append(col)

    # 대각선\
    diagonal = 0
    for i in range(100):
        diagonal += arr[i][i]
        total.append(diagonal)

    # 대각선/
    diagonal2 = 0
    for i in range(100):
        diagonal2 += arr[i][99-i]
        total.append(diagonal2)


    result = max(total)

    print(f'#{tc} {result}')
