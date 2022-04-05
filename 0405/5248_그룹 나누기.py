import sys
sys.stdin=open('5248_input.txt','r')

# 서로소 집합: 서로소 또는 상호배타 집합들은 서로 중복 포함된 원소가 없는 집합들(교집합이 없다)
# 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분

# x를 포함하는 집합
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])

# a와 b를 포함하는 두 집합을 통합
def union(a, b):
    parent[find_set(a)] = find_set(b)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    # 처음은 각각의 노드들이 스스로 부모가 되도록 배열 생성
    parent = [x for x in range(N+1)]
    # 2개씩 통합
    for i in range(M):
        a = arr[i*2+1]
        b = arr[i*2]
        union(a, b)

    result = []
    # 부모 노드로 집합의 루트를 설정하도록 정리
    for i in range(1, N+1):
        result.append(find_set(i))
    answer = len(set(result))

    print(f'#{tc} {answer}')





