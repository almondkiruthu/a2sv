# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions represent the movement of the robot:N, E, S, W
        directions = (0, 1, 0, -1, 0)
        obstacle_set = {(x, y) for x, y in obstacles}
        max_distance_squared, direction_index = 0, 0
        pos_x, pos_y = 0, 0
        
        for command in commands:
            if command == -2: # turn left
                direction_index = (direction_index + 3) % 4
            elif command == -1: # Turn right
                direction_index = (direction_index + 1) % 4
            else:
                # move the robot forward for the number of steps specified in the command
                for _ in range(command):
                    next_x, next_y = pos_x + directions[direction_index], pos_y + directions[direction_index + 1]

                    # check if new position is an obstacle
                    if (next_x, next_y) in obstacle_set:
                        break # stop if there's an obstacle found
                    
                    # update the robot's position
                    pos_x, pos_y = next_x, next_y

                    max_distance_squared = max(max_distance_squared, pos_x * pos_x + pos_y * pos_y)
        
        return max_distance_squared