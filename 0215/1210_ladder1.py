#import sys
#sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # X에서 거꾸로 올라가서 당첨 출발점 찾기
    # 1. X 표시 위치 찾기
    for i in range(100):
        if arr[99][i] == 2:
            y = i
            break
    x = 99

    # 현재 위치 arr[x][y]

    # 2. 이동하기
    while x >= 0 and y >= 0:
        # 2-1. 왼쪽 이동
        if y > 0 and arr[x][y-1] == 1:
            # 왼쪽으로 갈 수 있을 때까지 이동
            while y > 0 and arr[x][y-1] == 1:
                y -= 1
            # 갈 수 없으면 위로 이동
            else:
                x -= 1

        # 2-1. 오른쪽 이동
        elif y < 99 and arr[x][y+1] == 1:
            # 오른쪽으로 갈 수 있을 때까지 이동
            while y < 99 and arr[x][y+1] == 1:
                y += 1
            # 갈 수 없으면 위로 이동
            else:
                x -= 1

        # 왼쪽, 오른쪽 둘 다 길이 없다면, 위로 이동
        else:
            x -= 1

    print(f'#{tc} {y}')
