# 최소 heap
# if tree[child] < tree[parent]:
#   tree[child], tree[parent] = tree[parent], tree[child]
import sys
sys.stdin = open('5177_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] +list(map(int, input().split()))

    # 정렬
    for i in range(1, N+1):
        # 부모 idx = i // 2
        # 자식이 부모보다 작을 때까지 바꿔주기
        while tree[i] < tree[i//2]:
            tree[i], tree[i//2] = tree[i//2], tree[i]
            i = i // 2

    # 마지막 노드의 부모 노드 합
    total = 0
    parent_idx = N // 2
    while parent_idx > 0:
        total += tree[parent_idx]
        parent_idx = parent_idx // 2

    print(f'#{tc} {total}')


