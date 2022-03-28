import sys
sys.stdin=open('carrotfarm_input.txt','r')

def eat(n, ni, nj, d, x, farm):
    # 토끼 수를 초과하면 리턴
    if n+1 > M:
        return
    # 범위 내에 있을 때 이동 및 피해 표시
    if 0 <= ni < N and 0 <= nj < N:
        ni = ni + di[d] * x
        nj = nj + dj[d] * x
        if 0 <= ni < N and 0 <= nj < N:
            farm[ni][nj] = i+1
            eat(n+1, ni, nj, d, x, farm)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    farm = [[0] * N for _ in range(N)]
    rabbit = [list(map(int, input().split())) for _ in range(M)]

    # 방향: 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(M):
        # 토끼 시작점
        si = rabbit[i][0]
        sj = rabbit[i][1]
        farm[si][sj] = i + 1

        # 토끼 이동 방향 및 거리
        d = rabbit[i][2]
        x = rabbit[i][3]

        eat(0, si, sj, d, x, farm)

    # 피해 입은 구역의 수 count
    cnt = 0
    for i in range(N):
        for j in range(N):
            if farm[i][j] != 0:
                cnt += 1

    print(f'#{tc} {cnt}')








