import sys
sys.stdin = open('2105_input.txt','r')

def DFS(n, ci, cj, v, cnt):
    global si, sj, result
    if n > 3: # 종료
        return
    if n == 3 and ci == si and cj == sj and result < cnt:
        result = cnt
        return

    di = [1, 1, -1, -1]
    dj = [-1, 1, 1, -1]

    for d in range(n, n+2): # n 직진, n+1 방향 바꾸기
        if d < 4:
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
                DFS(d, ni, nj, v+[arr[ni][nj]], cnt+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = -1 # 최대값 구해야하기 때문에 임의의 작은 수 지정

    for si in range(N):
        for sj in range(N):
            DFS(0, si, sj, [], 0)

    print(f'#{tc} {result}')