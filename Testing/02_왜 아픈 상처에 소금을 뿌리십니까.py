# 2. [대학] 왜 아픈 상처에 소금을 뿌리십니까?

import sys

sys.stdin = open("./test1.txt", "r") 

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

n1 = []
n2  =[]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]== 1:
            n1.append(i)
            n2.append(j)
print((max(n1)-min(n1)+1)*(max(n2)-min(n2)+1))