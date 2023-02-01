class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        size, min_ops, ops = 0, float("inf"), 0
        for i, block in enumerate(blocks):
            if block == "W":
                ops += 1
            size += 1
            if size == k:
                size -= 1
                min_ops = min(min_ops, ops)
                if blocks[i-k+1] == "W":
                    ops -= 1

        return min_ops