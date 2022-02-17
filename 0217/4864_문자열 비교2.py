T = int(input())
for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    result = 0

    if str1 in str2:
        result = 1
    else:
        result

    print(f'#{tc} {result}')

