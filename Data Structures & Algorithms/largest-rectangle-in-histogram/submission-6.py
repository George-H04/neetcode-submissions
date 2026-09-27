class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        stack = []

        for i in range(len(heights)):
            if not stack or stack[-1][1] <= heights[i]:
                stack.append((i, heights[i]))
            else:
                start_index = float('inf')
                while stack and stack[-1][1] > heights[i]:
                    area = stack[-1][1] * (i - stack[-1][0])
                    if area > largest_area:
                        largest_area = area
                    if stack[-1][0] < i:
                        start_index = stack[-1][0]
                    stack.pop()
                stack.append((start_index, heights[i]))
        for bar in stack:
            area = bar[1] * (len(heights) - bar[0])

            if area > largest_area:
                largest_area = area

        return largest_area