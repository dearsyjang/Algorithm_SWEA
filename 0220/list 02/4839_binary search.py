T = int(input())
for tc in range(1, T+1):
    # 전체 쪽수, A가 찾을 쪽, B가 찾을 쪽
    P, A, B = map(int, input().split())

    l = 1
    r = P
    c = int((l+r)/2)

    def binarysearch(page, key):
        start = 1
        end = page
        cnt = 0
        while start <= end:
            middle = (start + end) / 2
            if middle == key:
                return cnt
            elif middle < key:
                end = middle
                cnt += 1
            elif middle > key:
                start = middle
                cnt += 1

    if binarysearch(P, A) > binarysearch(P, B):
        result = 'A'
    elif binarysearch(P, A) < binarysearch(P, A):
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')




