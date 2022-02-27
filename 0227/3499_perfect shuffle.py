import sys
sys.stdin = open('3499_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(input().split())

    middle = N//2
    result = []
    card1 = arr[0:middle]
    card2 = arr[middle:N]

    # 짝수
    if N % 2 == 0:
        for i in range(middle):
            result.append(card1[i])
            result.append(card2[i])

    # 홀수
    if N % 2 == 1:
        card1 = arr[0:middle]
        card2 = arr[middle+1:N]
        for i in range(middle):
            result.append(card1[i])
            result.append(card2[i])
        result.append(arr[middle])

    result = ' '.join(result)

    print(f'#{tc} {result}')

