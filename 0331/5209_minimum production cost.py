import sys
sys.stdin = open('5209_input.txt','r')

def DFS(i, total):
    global result

    # 시간초과 문제 해결하기 위해
    if total >= result:
        return

    if i == N: # 모든 제품 생산했다면,
        # 최소비용
        if total < result:
            result = total
        return

    for j in range(N):
        if visited[j] == 0: # j열 공장에서 생산한 적 없다면,
            visited[j] = 1
            DFS(i+1, total+arr[i][j]) # 다음 제품으로
            visited[j] = 0 # 원래대로 해주기


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = 123456789
    visited = [0] * N # 해당 공장에서 생산했다면, 방문 표시
    DFS(0,0)

    print(f'#{tc} {result}')


