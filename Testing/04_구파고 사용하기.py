# 4. [대학] 구파고 사용하기

import sys

sys.stdin = open("./test1.txt", "r") 

n, k = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
arr.sort(key=len)
print(arr[k-1])