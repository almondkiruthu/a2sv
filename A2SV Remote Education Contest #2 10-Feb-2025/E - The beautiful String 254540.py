# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E



T = int(input())
while (T > 0):
    s = list(input().strip())
    if len(s) > 0:
        queries = int(input())

        # track occurrences of "1100" in the string
        found_1100 = set()
        for i in range(len(s) - 3):
            if s[i:i + 4] == ["1", "1", "0", "0"]:
                found_1100.add(i)
        while queries > 0:
            index, query = input().split()
            index = int(index) - 1

            if s[index] == query:
                print("YES" if found_1100 else "NO")
            else:
                # Remove affected "1100" patterns
                for j in range(index - 3, index + 1):
                    if 0 <= j <= len(s) - 4 and s[j:j + 4] == ["1", "1", "0", "0"]:
                        found_1100.discard(j)

                # Apply the change
                s[index] = query

                # Remove affected "1100" patterns
                for j in range(index - 3, index + 1):
                    if 0 <= j <= len(s) - 4 and s[j:j + 4] == ["1", "1", "0", "0"]:
                        found_1100.add(j)

                print("YES" if found_1100 else "NO")

            queries -= 1
    T -= 1
