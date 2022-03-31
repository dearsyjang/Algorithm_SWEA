import sys
sys.stdin = open('5208_input.txt','r')

def charge(position):
    global result, cnt
    if cnt > result:
        return
    # 도착!
    if position >= N:
        if cnt < result:
            result = cnt
        return

    for i in range(position+battery[position], position, -1):
        cnt += 1
        charge(i)
        cnt -= 1


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0] # 정류장 수
    battery = [0] + arr[1:]

    result = 123456789
    cnt = 0

    charge(1)
    result = result-1 # 출발지에서 배터리 장착이므로, 충전X

    print(f'#{tc} {result}')


