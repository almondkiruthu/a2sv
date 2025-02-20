# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

from collections import OrderedDict


testcases = int(input())


chat_list = OrderedDict()
for _ in range(testcases):
    friend = input()
    if friend in chat_list:
        chat_list.pop(friend)  # Remove from current position
    chat_list[friend] = None # Insert at the end (0(1))

for friend in reversed(chat_list):
    print(friend)
