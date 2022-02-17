T = int(input())
for tc in range(1, T+1):
    N = str(input())
    M = str(input())

    cnt = 0
    max_cnt = 0
    # N의 문자가 M에 있으면 count + 1
    for i in N:
        for j in M:
            if i == j:
                cnt += 1
                # 최대값 찾기
                if max_cnt < cnt:
                    max_cnt = cnt
        else:
            cnt = 0

    print(f'#{tc} {max_cnt}')

