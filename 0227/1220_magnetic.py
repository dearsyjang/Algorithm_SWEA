import sys
sys.stdin = open('1220_input.txt','r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for i in range(100):
        isRed = False
        for j in range(100):
            if not isRed and arr[j][i] == 1:
                isRed = True
            if isRed and arr[j][i] == 2:
                cnt += 1
                isRed = False


    print(f'#{tc} {cnt}')

