T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    result = ''

    # 1. 가로
    for i in range(N):
        for j in range(N-M+1):
            row = []
            for k in range(M):
                row.append(arr[i][j+k])
            if row == row[::-1]:
                result = ''.join(row)

    # 2. 세로
    for i in range(N):
        for j in range(N-M+1):
            col = []
            for k in range(M):
                col.append(arr[j+k][i])
            if col == col[::-1]:
                result = ''.join(col)

    print(f'#{tc} {result}')