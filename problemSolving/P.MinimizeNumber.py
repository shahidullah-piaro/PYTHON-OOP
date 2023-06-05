# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P
import sys

size = int(input())
arr = list(map(int, input().split()))

result = sys.maxsize
for i in range(size):
    counter = 0
    if arr[i] % 2 != 0:
        print(0)
        sys.exit()
    while arr[i] % 2 == 0:
        counter += 1
        arr[i] //= 2
    if i == 0 or counter < result:
        result = counter

print(result)