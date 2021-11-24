from __future__ import annotations
from collections import Counter
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pos = position 
        
        # fleet_dict = dict()
        # for i in range(len(pos)):
        #     p = pos[i]
        #     while p + speed[i] <= target:
        #         p += speed[i]
        #         print(fleet_dict, ' before insertion', p in fleet_dict, 'p is', p)
        #         if p in fleet_dict:
        #             fleet_dict[p].append(i)
        #         else:
        #             fleet_dict[p] = [i]
        #         print(fleet_dict, ' after insertion')
        #     print(fleet_dict, i, ' is i')
        
        
        # method 2 
        
        for i in range(len(position)):
            p = position[i]
            
                
        
        
        
        
        # pos = position
        # index = 0 
        # if not len(pos) or not len(speed):
        #     return 0
        # # size = target - min(pos)
        # fleets = {}
        # while index <= size:
        #     fleets = {}
        #     for i in range(len(position)):
        #         p = position[i]
        #         p += speed[i]
        #         if p in fleets:
        #             fleets[p].append(i)
        #         else: 
        #             fleets[p] = [i]
        #     index += 1  
        # print(fleets)
        # return len(list(fleets))   
        # fleets = {}
        # for i in range(len(position)):
        #     p = position[i]
        #     while p<= target: 
        #         print(p, ' is p', fleets)
        #         if p in fleets:
        #             fleets[p].append(i)
        #         else: 
        #             fleets[p] = [i]
        #         p += speed[i]
        #     print(fleets, ' is fleets')
        # # print([ i for i in fleets if len(fleets[i]) > 1 ])
                
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
# target = 10
# position = [2, 4]
# speed = [3, 2]
sol = Solution()
print(sol.carFleet(target,position, speed))
# print(c.most_common(1))