class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = [(-1, 0),(0, 1), (1, 0), (0, -1)]
        def helper(instructions):
            nonlocal currPos
            for ins in instructions:
                if ins == "L":
                    dd = (currPos[1] - 1) % 4
                    currPos = (currPos[0], dd)

                elif ins == "R":
                    dd = (currPos[1] + 1) % 4
                    currPos = (currPos[0], dd)
                else:
                    mx, my = d[currPos[1]]
                    x, y = currPos[0]
                    newX, newY = x + mx, y + my
                    currPos = ((newX, newY), currPos[1])
            return False  
        
        currPos = ((0, 0), 1)
        
        helper(instructions)
        return currPos[0] == (0, 0) or currPos[1] != 1
        
