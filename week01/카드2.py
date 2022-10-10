# 2164번 : 카드2

from collections import deque

cards = deque(list(range(1,int(input())+1)))
while len(cards) != 1:
    cards.popleft()            # 1. 제일 위에 있는 카드를 바닥에 버린다.
    cards.append(cards[0])     # 2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
    cards.popleft()            # (옮기고 남은 흔적(?)은 삭제)

print(cards[0])  # 결과 출력