import sys
sys.stdin=open('1865_input.txt','r')

def DFS(i):
    global result, total

    # 가지치기
    if total <= result:
        return

    if i == N: # 일 배분 끝
        if total > result:
            result = total
        return

    for j in range(N):
        if visited[j] == 0: # 배분받지 않았다면
            if arr[i][j] == 0:  # zerodivisionerror
                continue
            else: # 확률 * 0.01
                total *= (arr[i][j]*0.01)
                visited[j] = 1
                DFS(i+1)
                total /= (arr[i][j]*0.01)
                visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 직원 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    result = 0
    total = 1

    DFS(0)

    result = round(result*100, 6) # 퍼센트, 7번째 자리에서 반올림

    print(f'#{tc}',end=' ')
    print('{:.6f}'.format(result)) # 뒤에 0 표시해서 자릿수 맞추기...

