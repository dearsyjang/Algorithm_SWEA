T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 파스칼의 삼각형을 담을 배열
    arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            # 양 끝 = 1
            if j == 0 or j == i:
                arr[i][j] = 1
            # 가운데 = 왼쪽 + 오른쪽 위
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    # 테스트케이스 출력
    print(f'#{tc}')
    # 배열 출력: 0은 출력X
    for x in range(N):
        for y in range(N):
            if arr[x][y] != 0:
                print(arr[x][y], end=' ')
        print()

