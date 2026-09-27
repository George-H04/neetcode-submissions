class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        max_streak = 0
        for n in num_set:
            current_streak = 0
            if n - 1 not in num_set:
                start = n
                current_streak += 1

                while start + 1 in num_set:
                    start += 1
                    current_streak += 1

                if current_streak > max_streak:
                    max_streak = current_streak

        return max_streak
