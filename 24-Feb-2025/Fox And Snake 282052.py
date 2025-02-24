# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

rows, cols = [int(_) for _ in input().split()]

for row in range(rows):
    # note that it's a zero based index language
    # odd rows for zero based index
    if row % 2 == 0:
        print("#" * cols)
    # even row that follow an odd row, put # at the rightmost
    elif row % 4 == 1:
        print("." * (cols - 1) + "#")
    # even row that follows another even row, put # at the leftmost
    else:
        print("#" + "." * (cols - 1))
