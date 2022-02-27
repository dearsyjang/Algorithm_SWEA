# import sys
# sys.stdin = open('1860_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    # arr.sort()

    result = 0
    for i in range(N):
        # arr[i] : i+1번째 손님이 도착한 시간
        # arr[i] // M * K : 시간의 생산량
        if (arr[i] // M) * K < i+1: # 생산량보다 손님이 많으면
            result = 'Impossible'
            break
        else:
            result = 'Possible'

    print(f'#{tc} {result}')