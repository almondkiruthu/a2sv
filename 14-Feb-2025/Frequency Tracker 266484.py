# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.num_count = defaultdict(int)
        self.frequency_count = defaultdict(int)
        

    def add(self, number: int) -> None:
        if self.frequency_count[self.num_count[number]] > 0:
            self.frequency_count[self.num_count[number]] -= 1
        
        self.num_count[number] += 1
        self.frequency_count[self.num_count[number]] += 1

    def deleteOne(self, number: int) -> None:
        # if number isn't there do nothing
        if self.num_count[number] == 0:
            return

        self.frequency_count[self.num_count[number]] -= 1
        self.num_count[number] -= 1

        # if the new count is not zero, increment the frequency count of the new count
        if self.num_count[number] > 0:
            self.frequency_count[self.num_count[number]] += 1
    
    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency_count[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)