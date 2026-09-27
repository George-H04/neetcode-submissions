class Solution {
public:
    vector<int>
    twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        vector<int> rv{};
        int i, j;

        for (int i = 0; i < nums.size(); i++)
        {
            if (hash.count(target - nums[i]))
            {
                j = hash[target - nums[i]];
                return {j, i};
            }

            hash[nums[i]] = i;
        }

        return rv;
    }
};
