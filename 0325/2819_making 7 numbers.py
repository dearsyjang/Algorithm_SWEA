import sys
sys.stdin = open('2819_input.txt','r')

def DFS(n, ci, cj, num):
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 숫자 일곱 자리(6번 이동)
    if n >= 7:
        result.add(num)
        return
    # 범위 내
    elif 0 <= ci < N and 0 <= cj < N:
        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                DFS(n+1, ni, nj, num*10+arr[ni][nj])

T = int(input())
for tc in range(1, T+1):
    N = 4
    arr = [list(map(int,input().split())) for _ in range(4)]
    result = set()

    # 시작
    for si in range(4):
        for sj in range(4):
            DFS(0, si, sj, 0)

    print(f'#{tc} {len(result)}')
