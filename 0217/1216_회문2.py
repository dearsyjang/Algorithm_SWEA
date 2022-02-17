import sys
sys.stdin = open('input.txt','r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(100)]

    result = 1

    # 가로
    row = arr
    for i in range(100, 0, -1):
        for j in range(100):
            for k in range(100-i+1):
                if row[j][k:k+i] == row[j][k:k+i][::-1]:
                    if result < i:
                        result = i

    # 세로 = 가로 회전
    col = list(map(list, zip(*arr)))
    for i in range(100, 0, -1):
        for j in range(100):
            for k in range(100-i+1):
                if col[j][k:k+i] == col[j][k:k+i][::-1]:
                    if result < i:
                        result = i

    print(f'#{tc} {result}')