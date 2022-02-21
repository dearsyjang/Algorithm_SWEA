T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]

    # 최장 길이 찾아 범위 지정
    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    # 세로 읽기
    word = ''
    for i in range(max_len):
        for j in range(5):
            if i < len(arr[j]):
                word += arr[j][i]

    print(f'#{tc} {word}')