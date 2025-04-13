from heapq import *

def find_kth_smallest(lists, k):
  minHeap = []

  # put the 1st element of each list in the min heap, together with the index and the list or origin.
  # so that we can fetch the other elements.
  for i in range(len(lists)):
    heppush(minHeap, (lists[i][0], 0, lists[i]))

  number_count, number = 0, 0
  while len(minHeap) > 0:
    number, index, list = heappop(minHeap)
    numberCount += 1
    if numberCount == k:
      break
    # if the array of the top elementi.e of the list of the number we have popped from the heap
    # has more elements, add the next element to the heap
    if len(list) > k:
      heappush(minHeap, (list[i+1], i+1, list))

  return number
