# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

from random import choice

class RandomizedSet:

    def __init__(self):
        self.index_map = {}
        self.values_list = []
        

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        else:
            self.index_map[val] = len(self.values_list) # map values to the index in the array
            self.values_list.append(val)

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        else:
            # get the index we want to remove
            index_to_remove = self.index_map[val]
            # get the current last element
            last_element = self.values_list[-1]
            # conduct a swap with the last element i.e. swap value of index to remove with the current last element in the list
            self.values_list[index_to_remove], self.values_list[len(self.values_list) - 1] = self.values_list[len(self.values_list) - 1], self.values_list[index_to_remove]

            #update the index of the swapped last element to map to the index we want to remove.
            self.index_map[last_element] = index_to_remove

            # del the current last element which is the element we have swapped from the map
            del self.index_map[self.values_list[-1]]

            # pop it from the list
            self.values_list.pop()

            return True
        

    def getRandom(self) -> int:
        # return a random value with the choice function from the random module which operates in 0(1) time
        return choice(self.values_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()