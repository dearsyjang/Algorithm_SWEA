import sys
sys.stdin = open('1226_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    # 출발점 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                x = i
                y = j

    # 방향: 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    stack = []
    stack.append((x, y))

    result = 0
    while stack:
        cx, cy = stack.pop()
        # 탐색
        for d in range(4):
            nx = cx + dr[d]
            ny = cy + dc[d]
            # 범위 내
            if 0 <= nx < 16 and 0 <= ny < 16:
                # 길
                if arr[nx][ny] == 0:
                    stack.append((nx, ny))
                    arr[nx][ny] = 1
                # 도착!
                elif arr[nx][ny] == 3:
                    result = 1
                    break

    print(f'#{tc} {result}')










