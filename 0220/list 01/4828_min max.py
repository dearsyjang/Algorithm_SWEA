T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    def GetMax(lst):
        max_value = lst[0]
        for i in range(len(lst)):
            if max_value < lst[i]:
                max_value = lst[i]
        return max_value

    def GetMin(lst):
        min_value = lst[0]
        for i in range(len(lst)):
            if min_value < lst[i]:
                min_value = lst[i]
        return min_value

    result = GetMax(arr) - GetMin(arr)

    print(f'#{tc} {result}')