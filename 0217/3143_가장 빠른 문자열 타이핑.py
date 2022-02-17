T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    N = len(A)
    M = len(B)

    # A의 글자 수를 세면서 B가 나오면 B만큼 넘어가기

    cnt = 0 # 타이핑
    i = 0 # 인덱스
    while i < N:
        # 첫 글자와 B의 첫 글자가 같으면 비교하기
        if A[i] == B[0]:
            # B가 있으면 타이핑 +1, B만큼 넘어가기
            if A[i:i+M] == B:
                i += M
                cnt += 1
            # 아니면, 타이핑 +1, 다음 글자로 넘어가기
            else:
                i += 1
                cnt += 1
        # 첫 글자가 B가 아니면 타이핑 +1, 다음 글자로 넘어가기
        else:
            i += 1
            cnt += 1


    print(f'#{tc} {cnt}')

