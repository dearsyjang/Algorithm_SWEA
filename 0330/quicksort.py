arr = [11, 45, 23, 81, 28, 34]
arr2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
arr3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

def quicksort(arr):
    if len(arr) <= 1: # 원소가 하나 남았을 때, 리턴 (재귀 함수 종료 조건)
        return arr

    result = []
    pivot = arr[0]

    left = []
    right = []

    for i in range(1, len(arr)): # 자기자신 제외하고
        if pivot > arr[i]: # 작으면 왼쪽
            left.append(arr[i])
        else: # 크면 오른쪽
            right.append(arr[i])

    left = quicksort(left) # 나눈 왼쪽도 퀵정렬
    right = quicksort(right) # 나눈 오른쪽도 퀵정렬

    # result에 합치기
    result += left
    result += [pivot]
    result += right

    return result

# print(quicksort(arr))
# print(quicksort(arr2))
# print(quicksort(arr3))


def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end # 마지막점이기 때문에 len(arr) - 1
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

# quick_sort(arr, 0, len(arr)-1)
# print(arr)
#
# quick_sort(arr2, 0, len(arr2)-1)
# print(arr2)
#
# quick_sort(arr3, 0, len(arr3)-1)
# print(arr3)


def quick_sort2(a, left, right):
    if left >= right:
        return

    pivot = left
    i = left+1
    j = right-1
    while i <= j:
        while i <= j and a[pivot] >= a[i]:
            i += 1
        while i <= j and a[pivot] <= a[j]:
            j -= 1

        if i <= j:
            a[i], a[j] = a[j], a[i]

    a[pivot], a[j] = a[j], a[pivot]

    quick_sort(a, left, j)
    quick_sort(a, j+1, right)

quick_sort2(arr, 0, len(arr))







