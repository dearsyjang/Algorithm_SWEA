import sys
sys.stdin = open('1231_input.txt')

def inorder(v):
    if v <= N:
        inorder(v*2)
        print(alpha[v], end='')
        inorder(v*2+1)
    return

T = 10
for tc in range(1, 11):
    N = int(input())
    alpha = [0] * (N+1)
    for i in range(N):
        idx = list(input().split())
        alpha[i+1] = idx[1]

    print(f'#{tc}', end=' ')
    inorder(1)
    print()

