class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2

            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(pile / mid)

            if curr_h > h:
                low = mid + 1
            else:
                high = mid - 1

        return low