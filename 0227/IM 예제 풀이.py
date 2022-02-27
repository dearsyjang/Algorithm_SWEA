import sys
sys.stdin = open('IM_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N+1)]

    # 기지국 찾기
    for i in range(N):
        for j in range(N):
            k = 0
            if arr[i][j] == 'A':
                k = 1
            elif arr[i][j] == 'B':
                k = 2
            elif arr[i][j] == 'C':
                k = 3

            for x in range(1, k+1):
                # 오른쪽
                if j+x <= N-1 and arr[i][j+x] == 'H':
                    arr[i][j+x] = 'O'
                # 왼쪽
                if j-x >= 0 and arr[i][j-x] == 'H':
                    arr[i][j-x] = 'O'
                # 위쪽
                if i-x >= 0 and arr[i-x][j] == 'H':
                    arr[i-x][j] = 'O'
                # 아래쪽
                if i+x <= N-1 and arr[i+x][j] == 'H':
                    arr[i+x][j] = 'O'

    # 카운트
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1


    print(f'#{tc} {cnt}')



