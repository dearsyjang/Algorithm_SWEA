import sys
sys.stdin = open('2001_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    total = []

    for i in range(N):
        for j in range(N):
            square = 0
            for x in range(M):
                for y in range(M):
                    if i+x < N and j+y < N:
                        square += arr[i+x][j+y]
            total.append(square)

    result = max(total)

    print(f'#{tc} {result}')