T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 빈 배열 만들기
    area = [[0] * 10 for _ in range(10)]
    # 겹치는 부분
    purple = 0

    for i in range(1, N+1):
        r1, c1, r2, c2, color = map(int,input().split())

        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                # 빨강
                if color == 1:
                    if area[row][col] == 0:
                        area[row][col] = 1
                    # 파랑과 겹치는 부분
                    elif area[row][col] == 2:
                        area[row][col] == 3
                        purple += 1
                # 파랑
                elif color == 2:
                    if area[row][col] == 0:
                        area[row][col] = 2
                    # 빨강과 겹치는 부분
                    elif area[row][col] == 1:
                        area[row][col] == 3
                        purple += 1

    print(f'#{tc} {purple}')
