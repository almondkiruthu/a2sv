# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)

        maxHeap = []

        for char, frequency in d.items():
            heapq.heappush(maxHeap, (-frequency, char))

        prev_char, prev_frequency = None, 0

        res = []

        while len(maxHeap) > 0:
            frequency, char = heapq.heappop(maxHeap)

            if prev_char and -prev_frequency > 0:
                heapq.heappush(maxHeap, (prev_frequency, prev_char))
            
            res.append(char)
            prev_char = char
            prev_frequency = frequency + 1

        if len(res) == len(s):
            return "".join(res) 
        else:
            return ""