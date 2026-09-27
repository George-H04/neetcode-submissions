class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
;       unordered_map<int, int> hash{};
        vector<int> rv{};

        for (int idx = 0; idx < nums.size(); idx++)
        {
            if (hash.contains(target - nums[idx]))
            {
                rv = {hash[target - nums[idx]], idx};    
                return rv;
            }

            hash[nums[idx]] = idx;
        }

        return rv;
    }
};
