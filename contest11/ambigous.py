from typing import *
class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        result = []
        inner = []
        for i in range(S):
            if S[i] == 0