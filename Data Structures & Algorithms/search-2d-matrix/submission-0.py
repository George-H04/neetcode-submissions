class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            low = 0
            high = len(row) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    # ignore left half, retry on right
                    low = mid + 1
                else:
                    high = mid - 1

        return False