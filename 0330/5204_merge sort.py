import sys
sys.stdin=open('5204_input.txt','r')

# 분할
def merge_sort(a):
    # 하나 남을 때까지
    if len(a) <= 1:
        return a

    # 가운데를 기준으로 나누기
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# 병합
def merge(left, right):
    global cnt

    if right[-1] < left[-1]:
        cnt += 1

    # pop은 시간이 많이 걸린단다...
    result = []
    i = j = 0

    # left, right에 원소가 남아있으면 반복
    while i < len(left) or j < len(right):
        # left, right 둘 다 남아 있을 때
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i]) # left가 작으니까 left 값 추가
                i += 1 # left 다음으로 이동
            else:
                result.append(right[j]) # right가 작으니까 right 값 추가
                j += 1 # right 다음으로 이동

        # left만 남아 있을 때
        elif i < len(left):
            result.append(left[i])
            i += 1

        # right만 남아 있을 때
        elif j < len(right):
            result.append(right[j])
            j += 1

    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    cnt = 0
    result = merge_sort(arr)
    midV = result[N//2] # 중간값

    print(f'#{tc} {midV} {cnt}')

