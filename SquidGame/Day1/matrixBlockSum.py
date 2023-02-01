from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        pref_sum = [[mat[i][j] for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                pref_sum[i][j] += pref_sum[i-1][j] if i > 0 else 0
        
        for i in range(m):
            for j in range(n):
                pref_sum[i][j] += pref_sum[i][j-1] if j > 0 else 0
                        
        for i in range(m):
            for j in range(n):
                x1, x2 = max(0, j-k), min(j+k, n-1)
                y1, y2 = max(0, i-k), min(i+k, m-1)
                pref_a = pref_sum[y1-1][x1-1] if (x1 > 0 and y1 > 0) else 0
                pref_b = pref_sum[y2][x1-1] if x1 > 0 else 0
                pref_c = pref_sum[y1-1][x2] if y1 > 0 else 0
                pref_d = pref_sum[y2][x2]
                mat[i][j] = pref_d  - pref_b - pref_c + pref_a

        return mat