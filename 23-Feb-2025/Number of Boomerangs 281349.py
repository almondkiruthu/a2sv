# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # intially set to zero
        boomerang_count = 0
        
        for vertex_point in points:
            # for each vertex point, create a counter to keep count of occurrences of distances. i.e. j - i, k - i
            distance_counter = Counter()

            # Now go over all points to calculate the squared distance from the vertex point
            for point in points:
                squared_distance = (vertex_point[0] - point[0])**2 + (vertex_point[1] - point[1])**2

                distance_counter[squared_distance] += 1

            # For each distance calculate potential boomerangs.
            # A boomerang is a set of 2 points at the same distance from the vertex
            # (n choose 2) pairs for each distance which is calculated through n*(n - 1)
            boomerang_count += sum(val * (val - 1) for val in distance_counter.values())

        return boomerang_count
        