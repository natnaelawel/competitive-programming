class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        years_logs = []
        for start, end in logs:
            years_logs.append((start, +1))
            years_logs.append((end, -1))
        years_logs.sort()
        max_val = 0
        curr_val = 0
        vals = {}
        for year, v in years_logs:
            curr_val += v
            if curr_val + v > max_val:
                max_val = curr_val + v
                vals[max_val] = year
                
        return vals[max_val]
                
            