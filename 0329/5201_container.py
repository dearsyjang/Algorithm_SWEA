import sys
sys.stdin=open('5201_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)

    result = 0
    i = j = 0

    while True:
        if i >= len(truck) or j >= len(weight):
            break
        elif truck[i] >= weight[j]:
            result += weight[j]
            i += 1
            j += 1
        else:
            j += 1

    print(f'#{tc} {result}')