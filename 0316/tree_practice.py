# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

# 높이 = 4
# 배열 = 2 ^ (4+1)

E = int(input())
arr = arr = list(map(int, input().split()))
tree = [([0] * 14) for _ in range(2)]

for i in range(len(arr)):
    if i % 2 == 0:
        x = arr[i]
        if tree[0][x] == 0:
            tree[0][x] = arr[i+1]
        else:
            tree[1][x] = arr[i+1]
print(tree)
