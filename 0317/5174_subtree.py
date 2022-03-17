import sys
sys.stdin = open('5174_input.txt','r')

def inorder(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    inorder(child1[node])
    inorder(child2[node])

    # global 없이 하는 법
    # V L R (전위 순회)
    # def order(n):
    # if n == 0: 자식 없는 경우 할 필요 없음
    #   return 0
    # return order(ch1[n]) + order(ch2[n]) + 1

    # 첫번째 tc
    # 1. node = 1 -> inorder(child1[6])
    # 1로 node가 들어오면 node != 0이므로 cnt + 1, inorder(child1[node]) = 6
    # 재귀로 inorder(6) 실행 cnt + 1

    # 2. node = 6 -> inorder(child1[4])
    # inorder(6) = 4 = node
    #  재귀로 inorder(4) 실행 cnt + 1

    # 3. node = 4 -> 0
    # inorder(child1(4)) = 0 = node이므로 return으로 inorder(child1[node]) 빠져나옴

    # 2-2. node = 6 -> inorder(child2[4])
    # inorder(6) = 4 = node로 inrder(child2[node]) 실행
    # inorder(child2(6)) = 0이므로 return으로 inorder(child2[node]) 빠져나옴
    # inorder(6) 끝!

    # 1-2. node = 1 -> inorder(child2[1])
    # 다시 inorder(1)로서 inorder(child2[node]) 실행
    # inorder(child2[node]) = 0 으로 최종적으로 cnt 반환


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    child1 = [0] * (E+2)  # 자식1
    child2 = [0] * (E+2)  #자식2

    for i in range(len(arr)):
        if i % 2 == 0: # 부모 짝수 번, 자식 홀수 번
            parent = arr[i]
            child = arr[i+1]
            if child1[arr[i]] == 0:
                child1[arr[i]] = arr[i+1]
            else:
                child2[arr[i]] = arr[i+1]

    cnt = 0
    inorder(N)
    print(f'#{tc} {cnt}')

