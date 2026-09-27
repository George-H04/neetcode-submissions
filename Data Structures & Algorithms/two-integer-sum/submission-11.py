class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, item in enumerate(nums):
            difference = target - item

            if difference in hash:
                return [hash[difference], idx]
            else:
                hash[item] = idx

        