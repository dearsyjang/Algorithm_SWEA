T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_len = 0
    cnt = 0

    # 가로
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                if cnt > max_len:
                    max_len = cnt
            else:
                cnt = 0

    # 세로
    for j in range(M):
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if cnt > max_len:
                    max_len = cnt
            else:
                cnt = 0

    print(f'#{tc} {max_len}')


