import sys
sys.stdin = open('11315_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list((input())) for _ in range(N)]

    # '.' : 돌이 없는 칸, 'o' : 돌이 있는 칸
    # 오른쪽, 오른쪽아래대각선, 아래쪽, 왼쪽아래대각선으로 연속 5개나와야함

    # arr에 오목이 존재하면 'YES', 존재하지 않으면 'NO' return
    def check(arr):
        # 우,하,우하대,좌하대
        dr = [0, 1, 1, 1]
        dc = [1, 0, 1, -1]
        for start_r in range(N):
            for start_c in range(N):
                if arr[start_r][start_c] == 'o':
                    for d in range(4):
                        r = start_r
                        c = start_c
                        # 각 방향으로 연속적으로 오목이 존재하는가?
                        cnt = 0
                        # 파이썬만 0 <= r <= N-1 허용
                        # 다른 언어는 r >= 0 and r <= N-1
                        while 0 <= r <= N - 1 and 0 <= c <= N - 1 and arr[r][c] == 'o':
                            cnt += 1
                            r += dr[d]
                            c += dc[d]
                        # 각 방향으로 오목이 존재?하는가
                        if cnt >= 5:
                            return 'YES'
        return 'NO'

    result = check(arr)

    print(f'#{tc} {result}')