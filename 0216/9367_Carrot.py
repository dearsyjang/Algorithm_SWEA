T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = list(map(int, input()))

    cnt = 1
    maxV = 1

    for i in range(1, N):
        if arr[i-1] < cnt:
            cnt += 1
            if maxV < cnt:
                maxV = cnt

    print(f'#{tc} {maxV}')