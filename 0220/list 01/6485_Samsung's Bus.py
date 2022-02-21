T = int(input())
for tc in range(1, T+1):
    N = int(input())

    bus_stop = [0] * 5001  # 문제 인덱스 값 맞춰주기 위함

    # 해당 정류장에 지나는 버스 누적 수
    for i in range(1, N+1):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            bus_stop[j] += 1

    # 버스 정류장 번호
    P = int(input())
    result = []
    for i in range(1, P+1):
        C = int(input())
        result.append(bus_stop[C])

    print(f'#{tc}', *result)



