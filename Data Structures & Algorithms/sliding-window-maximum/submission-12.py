from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0

        output = []

        window = deque()

        while r < len(nums):
            while window and nums[r] > nums[window[-1]]:
                window.pop()
            window.append(r)

            if window[0] < r - k + 1:
                window.popleft()

            if r >= k - 1:
                output.append(nums[window[0]])
            
            
            r += 1

        return output
