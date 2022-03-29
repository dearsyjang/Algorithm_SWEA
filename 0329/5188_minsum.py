import sys
sys.stdin=open('5188_input.txt','r')

def DFS(ci, cj):
    global result, total
    # 제한시간 초과 문제 해결해주기_가지치기
    if total > result:
        return
    # 도착
    if ci == N-1 and cj == N-1:
        # 최소값 구하기
        if total < result:
            result = total
            return

    # 방향: 하, 우
    di = [1, 0]
    dj = [0, 1]

    for d in range(0, 2):
        ni = ci + di[d]
        nj = cj + dj[d]
        # 범위 내에 있을 때, 방문하지 않았을 때
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            total += arr[ni][nj]
            DFS(ni, nj)

            # 다 구했으면 원래대로 해주기
            total -= arr[ni][nj]
            visited[ni][nj] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 123456789

    # 시작 위치
    si = 0
    sj = 0

    # 방문 표시 = 시작점
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 1

    # 합계 = 시작점
    total = arr[0][0]

    DFS(si, sj)

    print(f'#{tc} {result}')
