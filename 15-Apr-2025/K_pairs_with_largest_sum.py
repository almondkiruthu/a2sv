import heapq

def find_k_largest_pairs(nums1, nums2, k):
  result = []
  # TODO: Write your code here
  maxHeap = []
  if len(nums1) == len(nums2):
    n = len(nums1)
    for i in range(n):
      for j in range(n):
        sum = nums1[i] + nums2[j]
        heapq.heappush(maxHeap, (-sum, (nums1[i], nums2[j])))
  else:
    n = 0
    if len(nums1) > len(nums2):
      n = len(nums1)
      for i in range(n):
        j = 0
        while j < len(nums2):
          sum = nums1[i] + nums2[j]
          heapq.heappush(maxHeap, (-sum, (nums1[i], nums2[j])))
          j += 1
    else:
      n = len(nums2)
      for i in range(n):
        j = 0
        while j < len(nums2):
          sum = nums2[i] + nums1[j]
          heapq.heappush(maxHeap, (-sum, (nums2[i], nums1[j])))
          j += 1
    

  while k > 0:
    sum, pair = heapq.heappop(maxHeap)
    i, j = pair
    result.append([i, j])
    k -= 1
  
  
  return result

print(find_k_largest_pairs([9,8,2], [6,3,1], 3))
print(find_k_largest_pairs([5,2,1], [2, -1], 3))
