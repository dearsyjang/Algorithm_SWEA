import sys
sys.stdin = open('5178_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    for i in range(N,0,-1):
        # 부모가 있으면, 부모 = 자식들 합
        if i // 2 > 0:
            tree[i//2] += tree[i]

    print(f'#{tc} {tree[L]}')
