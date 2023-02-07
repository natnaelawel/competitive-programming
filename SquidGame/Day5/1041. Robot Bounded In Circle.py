
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (-1, 0), (0, -1),  (1, 0) ]
        last_dir = 1
        last_pos = (0, 0)
        for _ in range(4):
            for inst in instructions:
                if inst == "L":
                    last_dir = (last_dir + 1) % 4
                elif inst == "R":
                    last_dir = (last_dir - 1) % 4
                else:
                    x, y = directions[last_dir]
                    nx, ny = last_pos[0] + x, last_pos[1] + y
                    last_pos = (nx, ny)
            if last_pos == (0, 0):
                break

        return last_pos == (0, 0)

