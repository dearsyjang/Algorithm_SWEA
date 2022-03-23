import sys
sys.stdin=open('1240_input.txt','r')

num = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}
# 힌트: 각 줄이 다 같으므로, 한 줄만 해도 가능하다 / 암호는 항상 1로 끝난다

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input()))for _ in range(N)]

    # 1. 암호 코드 부분만 추출
    # 행 자르기
    def find_row_idx(arr):
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 1:
                    return i
    start_row = find_row_idx(arr)

    # 열 자르기: 마지막이 1로 끝나기 때문에, 뒤에서부터 탐색
    def find_col_idx(arr):
        for j in range(M-1, -1, -1):
            if arr[start_row][j] == 1:
                return j
    end_col = find_col_idx(arr)

    secret_code = arr[start_row][end_col-55:end_col+1]

    # 2. 7자리 단위로 잘라서 숫자 변환
    result = []
    for i in range(0, len(secret_code), 7):
        temp = ''
        for j in range(i, i+7):
            temp += str(secret_code[j])
        result.append(num[temp])



    # 3. 검증 코드 계산: "(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드" 가 10의 배수
    # 홀수와 짝수 자리 합
    odd = 0
    even = 0
    for i in range(7):
        # i는 인덱스이기 때문에 0부터 시작하지만, 코드 자리는 1부터 시작하기 때문에 반대로 해주기!!
        if i % 2 == 1:
            even += result[i]
        else:
            odd += result[i]


    # 정상적인 암호코드, 비정상적인 암호코드
    if (odd*3 + even + result[7]) % 10 == 0:
        total = odd + even + result[7]
        print(f'#{tc} {total}')
    else:
        print(f'#{tc}', 0)






