class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, item in enumerate(nums):
            difference = target - item
            
            if str(difference) in hash:
                return sorted([hash[str(difference)], idx])
            else:
                hash[str(item)] = idx

        