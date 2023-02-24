class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        active_mins = collections.defaultdict(set) 
        active_count = collections.defaultdict(int) 
        
        for user_id, time in logs:
            active_mins[user_id].add(time)
            active_count[user_id] = len(active_mins[user_id])

        result = {i: 0 for i in range(k)}
        for user_id in active_count:
            unique_minutes = active_count[user_id]
            result[unique_minutes - 1] += 1
        
        return result.values()
