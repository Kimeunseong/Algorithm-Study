# 3. [대학] 행복은 성적순이 아니잖아요.

import sys

sys.stdin = open("./test1.txt", "r") 

def rank(l, s, n):
    return 1 if s < l*(n/100) else 0
    
def test(k, m, v):
    return 1 if min(v) >= m else 0
    
for i in range(int(sys.stdin.readline())):
    arr = [*map(int, sys.stdin.readline().split())]
    result = rank(arr[0], arr[1], arr[2])
    if result == 0:
        break
    result = test(arr[3], arr[4], arr[5:])
    if result == 0:
        break
        
print(result)