# Problem: Presents - https://codeforces.com/problemset/problem/136/A

# ith number is Pi -- the number of a friend who gave a gift to friend i
# each friend received at least one gift
# possible that some friends don't give


T = int(input())
gifts = [int(i) for i in input().split()]
gift_map = {}
for giver in range(T):
    receiver = gifts[giver]
    gift_map[receiver] = giver + 1

sorted_givers = [gift_map[key] for key in sorted(gift_map)]
print(" ".join([str(giver) for giver in sorted_givers]))