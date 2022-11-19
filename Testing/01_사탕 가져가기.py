# 1. [대학] 사탕 가져가기

import sys

sys.stdin = open("./test1.txt", "r") 

k = int(sys.stdin.readline())
candy = list(map(int, sys.stdin.readline().split()))
win = 0

for i in candy:
    if i % 2 == 1:
        win += 1
        
if win == (k - win) :
    print('tie')
elif win > (k - win):
    print(win)
else:
    print(k-win)