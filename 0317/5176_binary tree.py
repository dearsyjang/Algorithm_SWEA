import sys
sys.stdin = open('5176_input.txt','r')

# 중위
def makeTree(n):
    global num
    if n <= N:
        # 왼쪽 -> 현재 노드 번호 * 2
        makeTree(n*2)
        # 끝까지 가면 값 넣기
        tree[n] = num
        # 값 넣었으면 증가
        num += 1
        # 오른쪽 -> 현재 노드 번호 * 2 + 1
        makeTree(n*2+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 1
    makeTree(1)
    root = (N//2) + 1

    print(f'#{tc} {tree[1]} {root}')

