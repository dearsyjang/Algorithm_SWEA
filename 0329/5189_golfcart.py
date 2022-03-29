import sys
sys.stdin=open('5189_input.txt','r')

def DFS(ci, total):
    global result
    if 0 not in visited:
        # total은 모든 곳을 방문 / so 시작점으로 돌아오는 값 더해줘야해!!
        if total+arr[ci][0] < result:
            result = total+arr[ci][0]
        return

    for ni in range(1, N):
        # 현재위치 -> 현재위치가 아니고, 방문한 적이 없으면
        if ci != ni and visited[ni] == 0:
            visited[ni] = 1
            DFS(ni, total + arr[ci][ni])
            visited[ni] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # [현재 위치][다음 위치]: 현재 위치 -> 다음 위치
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 방문 표시
    visited = [0] * N
    # 시작점 방문 표시
    visited[0] = 1

    result = 123456789

    DFS(0, 0)

    print(f'#{tc} {result}')

