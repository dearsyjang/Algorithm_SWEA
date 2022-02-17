T = int(input())
for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    M = len(str1)
    N = len(str2)
    result = 0

    # 고지식한 패턴 검색 알고리즘
    i = 0  # str2의 인덱스
    j = 0  # str1의 인덱스

    # 인덱스에서 벗아나지 않았으면
    while i < N and j < M:
        # i는 다음 시작점으로 이동, j는 원점으로
        if str2[i] != str1[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1

    if j == M: # 검색 성공
        result = 1
    else: # 검색 실패
        result = 0


    print(f'#{tc} {result}')

