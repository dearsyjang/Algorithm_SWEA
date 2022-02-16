T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = list(map(int, input()))

    cnt = 0
    maxV = 0

    for i in range(N):
        if arr[i] == 1:
            cnt += 1
            if cnt > maxV:
                maxV = cnt
        else:
            cnt = 0

    print(f'#{tc} {maxV}')

