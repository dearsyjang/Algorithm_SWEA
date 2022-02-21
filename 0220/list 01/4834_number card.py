T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    # 카운트 배열
    lst = [0] * 10
    for i in range(len(arr)):
        lst[arr[i]] += 1

    # 최대값 찾기
    max_cnt = 0
    max_card = 0
    for i in range(len(lst)):
        if lst[i] > max_cnt:
            max_cnt = lst[i]
            max_card = i
        # 만약 개수가 같다면, 카드값이 큰 숫자로
        elif lst[i] == max_cnt:
            if max_card < i:
                max_card = i
                max_cnt = lst[i]

    print(f'#{tc} {max_card} {lst[max_card]}')


