import sys
sys.stdin = open('1952_input.txt','r')

def DFS(n, total):
    global result
    if n > 12:
        if total < result:
            result = total
        return
    DFS(n+1, total+lst[n]*day)
    DFS(n+1, total+mon)
    DFS(n+3, total+mon3)
    DFS(n+12, total+year)

T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int,input().split())
    lst = [0] + list(map(int, input().split()))
    result = 123456789 # 최소값 구하기 위해 임의의 큰 수 지정

    DFS(1, 0)

    print(f'#{tc} {result}')
