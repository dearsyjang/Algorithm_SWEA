import sys
sys.stdin = open('12172_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = 0

    # +
    # 상하좌우
    d1i = [-1, 1, 0, 0]
    d1j = [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            # 중심
            total = arr[i][j]
            # 스프레이 세기
            for k in range(1,M):
                # 방향과 이동
                for l in range(4):
                    ni = i + d1i[l] * k
                    nj = j + d1j[l] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]
            if result < total:
                result = total

    # X
    d2i = [-1, -1, 1, 1]
    d2j = [-1, 1, -1, 1]
    for i in range(N):
        for j in range(N):
            # 중심
            total = arr[i][j]
            # 스프레이 세기
            for k in range(1, M):
                # 방향과 이동
                for l in range(4):
                    ni = i + d2i[l] * k
                    nj = j + d2j[l] * k
                    if 0 <= ni < N and 0 <= nj < N:
                        total += arr[ni][nj]
            if result < total:
                result = total

    print(f'#{tc} {result}')


