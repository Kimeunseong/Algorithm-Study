# 10816번 : 숫자 카드2

n = int(input())
cards = [int(input()) for i in range(n)]
for i in range(int(input())):
    card = int(input())
    print(cards.count(card))