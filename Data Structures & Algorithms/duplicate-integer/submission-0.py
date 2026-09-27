class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = []
        for item in nums:
            if item in newList:
                return True
            newList.append(item)
        return False
         