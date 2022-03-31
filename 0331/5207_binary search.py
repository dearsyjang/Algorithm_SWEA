import sys
sys.stdin = open('5207_input.txt','r')

def binary_search(arr, num):
    global cnt

    start = 0
    end = N-1
    flag = 0 # 1: 왼쪽, 2: 오른쪽

    while start <= end:
        mid = (start+end)//2
        # 탐색 성공!
        if num == arr[mid]:
            cnt += 1
            return
        # 왼쪽
        elif num < arr[mid]:
            if flag == 1:
                break
            end = mid-1
            flag = 1
        # 오른쪽
        elif num > arr[mid]:
            if flag == 2:
                break
            start = mid+1
            flag = 2


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst_A = sorted(list(map(int, input().split()))) # 정렬한 상태
    lst_B = list(map(int, input().split()))

    cnt = 0

    for i in lst_B:
        binary_search(lst_A, i)

    print(f'#{tc} {cnt}')