class Solution {
public:
    vector<int>
    twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash;
        hash.reserve(nums.size());
        vector<int> rv{};
        int i, j;

        for (int i = 0; i < nums.size(); i++)
        {
            auto it = hash.find(target - nums[i]);

            if (it != hash.end())
                return {it->second, i};

            hash[nums[i]] = i;
        }

        return rv;
    }
};
