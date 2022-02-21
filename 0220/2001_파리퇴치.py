T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    fly = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for x in range(M):
                for y in range(M):
                    total += arr[i+x][j+y]
            fly.append(total)

    max_fly = 0
    for i in range(len(fly)):
        if fly[i] > max_fly:
            max_fly = fly[i]


    print(f'#{tc} {max_fly}')