import sys
sys.stdin=open('5251_input.txt','r')

def DFS(c, total):
    global result
    # 가지치기
    if result < total:
        return

    # 종료 조건
    if c == N:
        if result > total:
            result = total

    # 이동: 연결이 되어 있고 방문한 적이 없다면
    for j in range(N+1):
        if arr[c][j] != 0 and visited[j] == 0:
            DFS(j, total+arr[c][j])
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())

    # 2차원 배열로 만들어주기
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s][e] = w

    # 방문 표시
    visited = [0] * (N+1)

    result = 123456789

    DFS(0,0)

    print(f'#{tc} {result}')
