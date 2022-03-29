import sys
sys.stdin=open('5203_input.txt','r')

def babygin(player):
    i = 0
    while i < 8:
        # triplet
        if player[i] >= 3:
            return True
        if player[i] and player[i+1] and player[i+2]:
            return True
        i += 1


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0

    # 카드 나눠주기
    for i in range(0,12):
       if i % 2 == 0:
           p1[cards[i]] += 1
           if babygin(p1):
               winner = 1
               break
       else:
           p2[cards[i]] += 1
           if babygin(p2):
               winner = 2
               break

    print(f'#{tc} {winner}')

