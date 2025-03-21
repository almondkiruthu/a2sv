# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        maxHeap = []

        for char, frequency in counter.items():
            frequency = -frequency
            heapq.heappush(maxHeap, (frequency, char))

        res = ""
        while len(maxHeap):
            build_up = ""
            # get the current max character.
            freq_and_char_pair = heapq.heappop(maxHeap)
            # obtain the curr max character and it's frequency (n)
            curr_char = freq_and_char_pair[1]
            n = -freq_and_char_pair[0]

            # build the characters and append them
            build_up = curr_char * n

            res += build_up

        return res

        