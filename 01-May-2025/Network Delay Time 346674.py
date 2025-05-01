# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create our adjacency list
        adj_list = defaultdict(list)

        for source, destination, weight in times:
            adj_list[source].append((destination, weight))

        min_time = {}
        min_heap = [(0, k)]

        while min_heap:
            distance_from_k_to_node, node = heapq.heappop(min_heap)

            if node in min_time:
                continue
            else:
                min_time[node] = distance_from_k_to_node
                for nei, nei_weight in adj_list[node]:
                    if nei not in min_time:
                        heapq.heappush(min_heap, (distance_from_k_to_node + nei_weight, nei))


        if len(min_time) == n:
            return max(min_time.values())
        else:
            return -1
            