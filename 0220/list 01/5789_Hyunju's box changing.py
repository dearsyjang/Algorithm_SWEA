T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * (N+1) # 인덱스 값 문제와 맞춰주기 위함

    for i in range(1, Q+1): # 1부터 Q
        L, R = map(int, input().split())
        for j in range(L, R+1):
            arr[j] = i


    print(f'#{tc}', *arr[1:])


