import sys
sys.stdin=open('5202_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    Start = []
    End = []

    for i in range(N):
        s, e = map(int, input().split())
        Start.append(s)
        End.append(e)

    time = 0
    cnt = 0
    for i in range(N):
        # 가장 빠른 작업(가장 작은 값)부터 시작
        min_idx = End.index(min(End))
        if time <= Start[min_idx]:
            time = min(End)
            cnt += 1

        del Start[min_idx]
        del End[min_idx]

    print(f'#{tc} {cnt}')
