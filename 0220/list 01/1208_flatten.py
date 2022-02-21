T = 10
for tc in range(1, T+1):
    N = int(input()) # 덤프 횟수
    arr = list(map(int, input().split()))

    for i in range(N):
        # 최대값, 최소값 구하기
        max_idx = 0
        min_idx = 0
        for j in range(100):
            if arr[max_idx] < arr[j]:
                max_idx = j
            if arr[min_idx] > arr[j]:
                min_idx = j

        # 덤프 작업
        arr[max_idx] -= 1
        arr[min_idx] += 1

    # 최종 최대값, 최소값 차이
    max_idx = 0
    min_idx = 0
    for j in range(100):
        if arr[max_idx] < arr[j]:
            max_idx = j
        if arr[min_idx] > arr[j]:
            min_idx = j


    result = arr[max_idx] - arr[min_idx]

    print(f'#{tc} {result}')
