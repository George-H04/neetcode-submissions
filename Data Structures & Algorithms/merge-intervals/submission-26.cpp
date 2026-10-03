class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {

            std::sort(intervals.begin(), intervals.end(), [](vector<int> a, 
                                                             vector<int> b) { return a[0] < b[0]; });

            vector<vector<int>> rv;

            rv.push_back(intervals[0]);

            for (auto& interval : intervals)
            {
                vector<int> recent_end = rv.back();
                if (interval[0] <= rv.back()[1])
                {
                    // alter existing interval if end is greater than last appended end
                    if (interval[1] > rv.back()[1])
                    rv.back()[1] = interval[1];

                }
                else rv.push_back(interval);
            }

            return rv;
    }
};
