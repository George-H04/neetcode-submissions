from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums)):
            prod_array = nums[:i] + nums[i+1:]
            output.append(int(prod(prod_array)))

        return output
        