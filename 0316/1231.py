import sys
sys.stdin = open('1231_input.txt')

def inorder(v):
    if v: # 0이 아니면
        inorder(left[v])
        print(alpha[v], end='')
        inorder(right[v])
    return

T = 10
for tc in range(1, T+1):
    N = int(input())
    # 안 바뀌는 값은 대부분 대문자로

    alpha = [''] * (N+1) # 알파벳
    left = [0] * (N+1) # 왼쪽 자식
    right = [0] * (N+1) # 오른쪽 자식

    for i in range(N):
        temp = list(input().split())
        idx = int(temp[0]) # 인덱스
        alpha[idx] = temp[1]

        if idx * 2 <= N: # 왼쪽자식 존재
            left[idx] = int(temp[2])
            if idx * 2 + 1 <= N: # 오른쪽자식 존재
                right[idx] = int(temp[3])

    print(f'#{tc}', end=' ')
    inorder(1)
    print()



