# 10816번 : 숫자 카드2

n = int(input())
cards = [int(input()) for i in range(n)] # n개의 숫자 카드를 입력받는다.
for i in range(int(input())):
    card = int(input())                   # 숫자를 입력받아,
    print(cards.count(card))                # 해당 숫자가 몇 개 있는지 확인후 출력한다.

# 미완성 코드ㅠㅜㅠ 입력 방식이 잘못됐음.. 다시 해보쟈..