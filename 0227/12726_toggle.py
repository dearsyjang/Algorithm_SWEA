import sys
sys.stdin = open('12726_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    for k in range(1, M+1):
        for i in range(N):
            for j in range(N):
                # (3) 전체 토글
                if M % k == 0 or k == M:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    elif arr[i][j] == 1:
                        arr[i][j] = 0
                # (2) 영역 토글
                elif i + 1 + j + 1 == k or (i + 1 + j + 1) % k == 0:
                        if arr[i][j] == 0:
                            arr[i][j] = 1
                        elif arr[i][j] == 1:
                            arr[i][j] = 0

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1

    print(f'#{tc} {cnt}')

    # T = int(input())
    # for tc in range(1, T + 1):
    #     N, M = map(int, input().split())
    #     arr = [list(map(int, input().split())) for _ in range(N)]
    #
    #     for k in range(1, M + 1):
    #         # (3) 전체 토글
    #         if M % k == 0 or k == M:
    #             for i in range(N):
    #                 for j in range(N):
    #                     if arr[i][j] == 0:
    #                         arr[i][j] = 1
    #                     elif arr[i][j] == 1:
    #                         arr[i][j] = 0
    #         # (2) 영역 토글
    #         else:
    #             for i in range(N):
    #                 for j in range(N):
    #                     if i + 1 + j + 1 == k or (i + 1 + j + 1) % k == 0:
    #                         if arr[i][j] == 0:
    #                             arr[i][j] = 1
    #                         elif arr[i][j] == 1:
    #                             arr[i][j] = 0
    #
    #     cnt = 0
    #     for i in range(N):
    #         for j in range(N):
    #             if arr[i][j] == 1:
    #                 cnt += 1
    #
    #     print(f'#{tc} {cnt}')