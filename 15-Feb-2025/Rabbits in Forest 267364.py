# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        result = 0

        for num_of_other_rabbits, count in count.items():
            # match groups with same answers they form a group
            # group size is num_of_other_rabbits + 1 i.e including itself
            group_size = num_of_other_rabbits + 1
            # calculate n.o. of full groups by count / group size and rounding it up
            # num of other rabbits with the same colour
            number_of_groups = math.ceil(count / group_size)

            result += number_of_groups * group_size
        return result