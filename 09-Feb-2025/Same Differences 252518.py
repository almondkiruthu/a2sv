# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

T = int(input())


while (T > 0):
    n = int(input())
    if n > 0:
        count = 0
        freq_map = {}
        nums = [int(_) for _ in input().split()]
        for i in range(n):
            num = nums[i]
            diff = num - i
            if diff in freq_map:
                # take the prev count
                prev_count = freq_map[diff]
                count += prev_count
                freq_map[diff] += 1
            else:
                freq_map[diff] = 1
        print(count)
    T -= 1
