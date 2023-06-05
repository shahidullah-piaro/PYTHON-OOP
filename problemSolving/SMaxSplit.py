# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s
value = input()
arr = [['' for j in range(1000)] for i in range(1000)]
row, column, r, l, counter = 0, 0, 0, 0, 0
for i in range(len(value)):
    if value[i] == 'R':
        arr[row][column] = value[i]
        r += 1
    else:
        arr[row][column] = value[i]
        l += 1
    column += 1
    if r == l and r > 0:
        row += 1
        column = 0
        counter += 1
        r = 0
        l = 0
print(counter)
for i in range(1000):
    if arr[i][0] != 'R' and arr[i][0] != 'L':
        continue
    print(''.join(arr[i]))
