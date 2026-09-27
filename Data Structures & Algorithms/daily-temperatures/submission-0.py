class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        decreasing_stack = []

        for i, temp in enumerate(temperatures):
            if not decreasing_stack or temp < temperatures[decreasing_stack[-1]]:
                print(f"{temp} is not increasing, we push it to the stack")
                decreasing_stack.append(i)
            else:
                print(f"{temp} IS increasing, we must pop from stack")
                pop_counter = 0
                while decreasing_stack and temp > temperatures[decreasing_stack[-1]]:
                    if output[decreasing_stack[-1]] == 0:
                        output[decreasing_stack[-1]] = i - decreasing_stack[-1]
                    decreasing_stack.pop()
                    pop_counter += 1
                print(f"performed {pop_counter} pop(s).")
                decreasing_stack.append(i)
                print(f"The number of days at index {output[decreasing_stack[-1]]} is {i - decreasing_stack[-1]}")
                output[decreasing_stack[-1]] = i - decreasing_stack[-1]

                current_stack = [temperatures[index] for index in decreasing_stack]
                print(f"Current stack is: {current_stack}")

        return output