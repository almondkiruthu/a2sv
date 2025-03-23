# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        minHeap = []

        heapq.heappush(minHeap, (nums1[0]+nums2[0], 0, 0))
        visited_indices = set()

        while k > 0 and len(minHeap) > 0:
            pair_sum, i, j = heapq.heappop(minHeap)
            res.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i+1, j) not in visited_indices:
                heapq.heappush(minHeap, (nums1[i+1] + nums2[j], i+1, j))
                visited_indices.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j+1) not in visited_indices:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j+1))
                visited_indices.add((i, j + 1))

            k -= 1

        return res

        