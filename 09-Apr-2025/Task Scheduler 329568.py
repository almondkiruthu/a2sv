# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        interval_count = 0
        task_frequency = Counter(tasks)

        maxHeap = []

        for char, frequency in task_frequency.items():
            heapq.heappush(maxHeap, (-frequency, char))

        while len(maxHeap) > 0:
            wait_list = []
            k = n + 1 # execute as many as "k + 1" tasks from the max-heap

            while k > 0 and len(maxHeap) > 0:
                interval_count += 1
                frequency, char = heapq.heappop(maxHeap)

                if -frequency > 1:
                    # decrement the frequency and add it to the waitlist
                    wait_list.append((frequency + 1, char))

                k -= 1
            
            # put everything in the wait list back to the maxHeap to be executed
            for frequency, char in wait_list:
                heapq.heappush(maxHeap, (frequency, char))

            # we'll have 'k' idle intervals for the next iteration

            if len(maxHeap) > 0:
                interval_count += k

        return interval_count