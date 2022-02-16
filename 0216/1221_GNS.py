
T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    arr = list(input().split())
    atoi = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    itoa = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    num = [0]*N
    # 숫자 변환
    for i in range(N):
        num[i] = atoi[arr[i]]

    # 정렬
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if num[minIdx] > num[j]:
                minIdx = j
        num[i], num[minIdx] = num[minIdx], num[i]

    # 영문 변환
    for i in range(N):
        arr[i] = itoa[num[i]]

    print(f'{tc}')
    print(*arr)