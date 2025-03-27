from collections import Counter, deque
import heapq


def reorganize_string(str, k):
  counter = Counter(str)
  maxHeap = []

  for char, frequency in counter.items():
    heapq.heappush(maxHeap, (-frequency, char))

  queue = deque()
  prev_char, prev_frequency = None, 0
  res = []
  while len(maxHeap) > 0:
    frequency, char= heapq.heappop(maxHeap)
    res.append(char)
   
    # decrement frequency and append char to queue
    queue.append((char, frequency + 1 ))
    if len(queue) == k:
      prev_char, prev_frequency = queue.popleft()
      if -prev_frequency > 0:
        heapq.heappush(maxHeap, (prev_frequency, prev_char))


  if len(res) == len(str):
      return "".join(res)
  else:
    return "Can't form the K distance character rearrangement"
    
print(reorganize_string("mmpp", 2))
print(reorganize_string("Programming", 3))
print(reorganize_string("aappa", 3))
