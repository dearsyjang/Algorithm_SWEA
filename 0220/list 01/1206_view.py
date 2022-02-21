T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    view = 0

    for i in range(2, N-2):
        max_floor = 0
        for j in range(i-2, i+3):
            if i != j and max_floor < arr[j]:
                max_floor = arr[j]


        if arr[i] - max_floor > 0:
            view += (arr[i] - max_floor)


    print(f'#{tc} {view}')