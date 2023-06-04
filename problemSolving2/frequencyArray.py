import numpy as np

size, counter = map(int, input().split())
arr = np.zeros(1000001, dtype=int)
nums = [1, 2, 3, 4, 5, 3, 2, 1, 5, 3]

# for i in range(0, size):
#     ele = int(input())
#     nums.append(ele)

for i in range(size):
    num = nums[i]
    if arr[num] == 0:
        arr[num] = 1
    else:
        arr[num] += 1
for i in range(1, counter+1):
    print(arr[i])
