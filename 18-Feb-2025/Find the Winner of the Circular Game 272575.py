# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque()

        for i in range(1, n + 1):
            q.append(i)

        while len(q) > 1:
            for _ in range(k - 1):
                num = q.popleft()
                q.append(num)

            # delete the number to be deleted
            q.popleft()

        return q[0] 
