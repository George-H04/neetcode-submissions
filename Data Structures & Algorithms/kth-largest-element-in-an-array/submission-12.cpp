class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Interesting problem. Naive thought is some sort of counter
        // Actually, what if we just replicate the array, then call max k times, removing the element each time?
        // Horrible, but it'll work! technically, n * k time complexity, so worse than n log k, but this is the first approach

        // Yeah this is actually WAY too slow... the specified time complexity is the bar I need to meet, not a suggestion
        // A datastructure that will only store the top k largest elements... perhaps a type of stack? Loop through, that's O(n), stack is effectively S(k). Let's try it.

        // A monotonic stack was not the right approach. Of course not, the data flow doesn't allow for that. Instead,
        // let's try a min-heap (a data structure I have NOT thought of). Still not exactly sure why this is better than a max-heap though

        // However we must make sure we are always tracking the k LARGEST elements...?

        std::priority_queue<int, std::vector<int>, std::greater<int>> minheap;

        for (const auto num : nums)
        {
            minheap.push(num);

            if (minheap.size() > k)
                minheap.pop();
            
        }

        return minheap.top();
    
    }
};
