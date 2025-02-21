# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

x2, y2 = 0, 0

for i in range(5):
  row = [int(_) for _ in input().split()]
  if 1 in row:
    x2, y2 = i, row.index(1) # get row index and column index
    break
  
moves = abs(x2 - 2) + abs(y2 - 2)
print(moves)