import sys
sys.stdin = open('5185_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N, data = input().split()
    lst = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
           'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    # 1. 10진수로 변환
    num_lst = []
    for i in data:
        num = lst[i]
        num_lst.append(num)

    # 2. 10진수로 바꾼 num 2진수로 바꾸기
    result=''
    for i in range(len(num_lst)):
        temp = num_lst[i]
        binary = ''
        # 16진수는 4자리이기 때문에 4번 반복
        for _ in range(4):
            binary = str(temp%2) + binary
            temp = temp // 2
        result += binary
    print(f'#{tc} {result}')