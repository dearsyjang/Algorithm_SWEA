import sys
sys.stdin=open('input_ex3.txt','r')

def subset(idx, total):
    global cnt
    if idx == N:
        if total == 0:
            cnt += 1
        return
    else:
        subset(idx+1, total+arr[idx])
        subset(idx+1, total)

T = 1
for i in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0

    subset(0, 0)
    print(cnt)
