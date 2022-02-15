T = int(input())
for tc in range(1, T+1):
    # N개의 영역
    N = int(input())
    # 10 * 10 격자 만들기
    area = [[0] * 10 for _ in range(10)]
    # 겹치는 부분: 보라색
    purple = 0

    # 각 색칠 구역 좌표 및 색깔 추출
    for i in range(1, N+1):
        row1, col1, row2, col2, color = map(int, input().split())

        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                # 빨간색 color1
                if color == 1:
                    # 빈 영역, 빨간색 영역은 빨간색으로 칠하기
                    if area[row][col] == 0:
                        area[row][col] = 1
                    # 파란색 영역, 겹치는 영역은 보라색으로 칠하기
                    elif area[row][col] == 2:
                        area[row][col] = 3
                        # 보라색 영역 count
                        purple += 1

                # 파란색 color2
                elif color == 2:
                    # 빈 영역, 파란색 영역은 파란색으로 칠하기
                    if area[row][col] == 0:
                        area[row][col] = 2
                    # 빨간색 영역, 겹치는 영역은 보라색으로 칠하기
                    elif area[row][col] == 1:
                        area[row][col] = 3
                        # 보라색 영역 count
                        purple += 1

    print(f'#{tc} {purple}')




