T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    num=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    # sum 함수 구현
    def GetSum(numbers):
        result = 0
        for i in range(len(numbers)):
            result += numbers[i]
        return result

    cnt = 0
    # 1. 부분집합 생성
    for i in range(1<<12):
        lst = []
        for j in range(12):
            if i & (1<<j):
                lst.append(num[j])
        # 2. 조건: 원소의 수 N, 부분집합의 합 K
        if len(lst) == N and GetSum(lst) == K:
            cnt += 1

    print(f'#{tc} {cnt}')



