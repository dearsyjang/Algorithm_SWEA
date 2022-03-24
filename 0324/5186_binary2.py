import sys
sys.stdin=open('5186_input.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    # 10진수 소수를 2진수로 변환하는 방법 참고
    # 소수 * 2 값의 정수 부분들만 표기 (소수부분이 0이 될 때까지 반복)

    result = ''
    # 자릿수
    cnt = 0


    while N != 0:
        # 13자리 이상, overflow
        if cnt >= 13:
            result = 'overflow'
            break
        else:
            temp = int(N * 2)
            N = N*2 - temp
            result += str(temp)
            cnt += 1

    print(f'#{tc} {result}')
