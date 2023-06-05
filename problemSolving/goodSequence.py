# https://atcoder.jp/contests/arc087/tasks/arc087_a
from collections import defaultdict
   
mp = defaultdict(int)
   
# L = [3, 3, 3, 3]
# L = [2, 4, 1, 4, 2]
# L = [1, 2, 2, 3, 3, 3]
# L = [1000000000]
L = [2, 7, 1, 8, 2, 8, 1, 8]

for i in L:
    mp[i] += 1

sum = 0
for key, value in mp.items():
    if value < key:
        sum += value
    elif value > key:
        sum += value - key

print(sum)