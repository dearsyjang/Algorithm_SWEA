T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    # 이진검색 함수 정의
    def binarySearch(page, key):
        start = 1  # 문제 잘 읽자...
        end = page
        cnt = 0
        while start <= end:
            middle = (start + end) // 2
            if middle == key:
                return cnt
            elif middle > key:
                end = middle
                cnt += 1
            elif middle < key:
                start = middle
                cnt += 1

    # 결과 출력, 탐색 횟수가 적은 사람이 승자 / 탐색 횟수가 같을 경우, 0
    if binarySearch(P, Pa) > binarySearch(P, Pb):
        result = 'B'
    elif binarySearch(P, Pa) < binarySearch(P, Pb):
        result = 'A'
    else:
        result = 0

    print(f'#{tc} {result}')

