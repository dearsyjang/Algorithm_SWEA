# + 모양 분사
def cross(lst):
    # 최종 max값 저장
    result1 = 0
    # 좌표 구분
    di = [-1, 1, 0, 0]
    dj = [0, 0, 1, -1]
    # 행렬 안의 모든 인자들의 합을 구해야 하기 때문에 전체 순회
    for i in range(len(lst)):
        for j in range(len(lst)):
            total = lst[i][j]  # 자기 자신 포함해야 함.
            for l in range(4):  # 좌표 방향 순회
                ni = i + di[l]
                nj = j + dj[l]
                cnt = 1  # 스프레이 범위 초기값
                while 0 <= ni < N and 0 <= nj < N and cnt < M:  # 인덱스 벗어나지 않고 스프레이 값 전까지 반복
                    total += lst[ni][nj]
                    ni += di[l]  # 범위 확장
                    nj += dj[l]
                    cnt += 1
            if result1 < total:  # 최댓값 구하기
                result1 = total
    return result1


# x 모양 분사 (위와 동일)
def x(lst):
    result2 = 0
    dx = [1, -1, 1, -1]
    dy = [1, 1, -1, -1]
    for i in range(len(lst)):
        for j in range(len(lst)):
            total = lst[i][j]
            for l in range(4):
                nx = i + dx[l]
                ny = j + dy[l]
                cnt = 1
                while 0 <= nx < N and 0 <= ny < N and cnt < M:
                    total += lst[nx][ny]
                    nx += dx[l]
                    ny += dy[l]
                    cnt += 1
            if result2 < total:
                result2 = total

    return result2


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N은 행렬, M은 스프레이 분사 길이(자신 포함)
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum1 = cross(arr)  # +자 최대값 호출
    max_sum2 = x(arr)  # x자 최대값 호출

    if max_sum1 < max_sum2:  # 최대값 구분
        print(f'#{tc} {max_sum2}')
    else:
        print(f'#{tc} {max_sum1}')