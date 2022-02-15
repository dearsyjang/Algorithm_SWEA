T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 홀수 번째와 짝수 번째로 나누어 정렬
    # 결과는 10개까지만 정렬
    for i in range(10):
        # 1. 홀수 번째, 내림차순
        if i % 2:
            maxIdx = i
            for j in range(i + 1, N):
                if arr[maxIdx] > arr[j]:
                    maxIdx = j
            arr[i], arr[maxIdx] = arr[maxIdx], arr[i]

        # 2. 짝수 번째: 오름차순
        else:
            minIdx = i
            for j in range(i + 1, N):
                if arr[minIdx] < arr[j]:
                    minIdx = j
            arr[i], arr[minIdx] = arr[minIdx], arr[i]

    print(f'#{tc}', *arr[:10])

